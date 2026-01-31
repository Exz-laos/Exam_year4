# -*- coding: utf-8 -*-
import streamlit as st
from gtts import gTTS
import io
import base64
import random
import re
import html

from data import flashcard_data, thai_translations, english_translations


# --- Configuration for English UI ---
STATUS_MAP_JA_TO_EN = {
    "未確認": "Unchecked",
    "理解済み": "✅Understood",
    "復習が必要": "Needs Review",
}
INITIAL_STATUS_JA = "未確認"
STATUS_UNDERSTOOD_JA = "理解済み"
STATUS_NEEDS_REVIEW_JA = "復習が必要"


# --- Audio ---
@st.cache_data
def generate_audio(text: str):
    """Generates audio and returns a Base64 encoded Data URI."""
    audio_bytes = io.BytesIO()
    try:
        tts = gTTS(text=text, lang="ja", slow=False)
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        b64 = base64.b64encode(audio_bytes.read()).decode("utf-8")
        return f"data:audio/mp3;base64,{b64}"
    except Exception as e:
        print(f"Audio generation error: {e}")
        return None


# --------------------------
# Rendering Helpers
# --------------------------
def render_content_with_latex(content: str):
    """
    Renders Japanese/Answer text:
    - LaTeX parts: $...$ or $$...$$ => st.latex
    - Normal text: preserve line breaks in your """""" strings.
    """
    latex_parts = re.split(r"(\$\$.*?\$\$|\$.*?\$)", content, flags=re.DOTALL)

    for part in latex_parts:
        if not part:
            continue

        if part.startswith("$$") and part.endswith("$$"):
            latex_code = part[2:-2].strip()
            if latex_code:
                st.latex(latex_code)
            continue

        if part.startswith("$") and part.endswith("$"):
            latex_code = part[1:-1].strip()
            if latex_code:
                st.latex(latex_code)
            continue

        safe = html.escape(part).replace("\n", "<br>")
        st.markdown(f'<div class="flashcard-text">{safe}</div>', unsafe_allow_html=True)


def _format_translation_text(text: str) -> str:
    """
    Improve readability for English/Thai translations:
    - Keep newlines
    - If it is one long paragraph, insert line breaks before options:
      English: A. B. C. ...
      Thai: ก. ข. ค. ...
      Also before (1) (2) ...
    """
    t = text.strip()

    # Insert newline before English option markers like "A."
    t = re.sub(r"\s(?=[A-H]\.)", "\n", t)

    # Insert newline before Thai option markers like "ก."
    t = re.sub(r"\s(?=[ก-ฮ]\.)", "\n", t)

    # Insert newline before numbered markers like "(1)"
    t = re.sub(r"\s(?=\(\d+\))", "\n", t)

    return t


def render_translation_block(title: str, text: str):
    """Render translations in a nicer box preserving line breaks."""
    formatted = _format_translation_text(text)
    safe = html.escape(formatted).replace("\n", "<br>")
    st.markdown(
        f"""
        <div class="translation-box">
          <div class="translation-title">{html.escape(title)}</div>
          <div>{safe}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------
# Session State
# --------------------------
def initialize_session_state():
    all_keys = list(flashcard_data.keys())

    if "card_keys_master" not in st.session_state:
        st.session_state.card_keys_master = all_keys

    if "master_deck_size" not in st.session_state:
        st.session_state.master_deck_size = len(st.session_state.card_keys_master)

    if "card_keys_active" not in st.session_state:
        st.session_state.card_keys_active = st.session_state.card_keys_master

    if "total_cards" not in st.session_state:
        st.session_state.total_cards = len(st.session_state.card_keys_active)

    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    if "is_flipped" not in st.session_state:
        st.session_state.is_flipped = False

    if "card_status" not in st.session_state:
        st.session_state.card_status = {key: INITIAL_STATUS_JA for key in all_keys}

    if "shuffle_on" not in st.session_state:
        st.session_state.shuffle_on = False

    if "audio_to_play" not in st.session_state:
        st.session_state.audio_to_play = None

    if "show_thai_translation" not in st.session_state:
        st.session_state.show_thai_translation = None

    if "show_english_translation" not in st.session_state:
        st.session_state.show_english_translation = None


def apply_range(start_num: int, end_num: int):
    start_idx = start_num - 1
    end_idx = end_num

    all_keys = list(flashcard_data.keys())

    if 0 <= start_idx < end_idx <= len(all_keys):
        master_list = all_keys[start_idx:end_idx]

        if st.session_state.shuffle_on:
            random.shuffle(master_list)

        st.session_state.card_keys_master = master_list
        st.session_state.card_keys_active = master_list

        st.session_state.master_deck_size = len(master_list)

        st.session_state.total_cards = len(st.session_state.card_keys_active)
        st.session_state.current_index = 0
        st.session_state.is_flipped = False
    else:
        st.sidebar.error("Invalid range selected.")


def filter_deck_for_review():
    review_keys = [
        key
        for key in st.session_state.card_keys_master
        if st.session_state.card_status.get(key) != STATUS_UNDERSTOOD_JA
    ]

    if not review_keys:
        st.sidebar.success("Great job! No cards left to review in this range. 🎉")
        return

    st.session_state.card_keys_active = review_keys
    st.session_state.total_cards = len(review_keys)
    st.session_state.current_index = 0
    st.session_state.is_flipped = False


def reset_to_master_deck():
    st.session_state.card_keys_active = st.session_state.card_keys_master
    st.session_state.total_cards = len(st.session_state.card_keys_master)
    st.session_state.current_index = 0
    st.session_state.is_flipped = False


def next_card():
    if st.session_state.current_index < st.session_state.total_cards - 1:
        st.session_state.current_index += 1
        st.session_state.is_flipped = False


def prev_card():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1
        st.session_state.is_flipped = False


def mark_status(status_ja: str):
    current_key = st.session_state.card_keys_active[st.session_state.current_index]
    st.session_state.card_status[current_key] = status_ja


# --------------------------
# UI Layout
# --------------------------
st.set_page_config(page_title="ImageProcessing＿final Flashcards", layout="wide", page_icon="🗂️")

st.markdown(
    """
    <style>
        /* General Theme */
        body, .stApp { background-color: #121212; color: #E0E0E0; }
        .stMarkdown, .stText, .stSubheader, .stHeader, .stTitle { color: #E0E0E0 !important; }
        div.stButton > button {
            background-color: #2E2E2E;
            color: #E0E0E0;
            border: 1px solid #444;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-size: 16px;
            font-weight: 500;
        }
        div.stButton > button:hover { background-color: #444; border: 1px solid #666; color: #FFFFFF; }
        section[data-testid="stSidebar"] { background-color: #1A1A1A; border-right: 1px solid #333; }

        /* Japanese/Answer text */
        .flashcard-text {
            font-size: 1.5em;
            line-height: 1.6;
            white-space: pre-wrap;   /* ✅ keep \n */
            word-break: break-word;
        }

        /* Translation box */
        .translation-box {
            background: rgba(80, 120, 200, 0.12);
            border: 1px solid rgba(80, 120, 200, 0.35);
            border-radius: 12px;
            padding: 14px 16px;
            margin-top: 8px;

            font-size: 1.15em;
            line-height: 1.75;

            white-space: pre-wrap;   /* ✅ keep \n */
            word-break: break-word;
        }

        .translation-title {
            font-weight: 700;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
    </style>
""",
    unsafe_allow_html=True,
)

initialize_session_state()

# --- Sidebar Controls ---
with st.sidebar:
    st.header("📊 Progress")

    current_range_total = st.session_state.master_deck_size
    master_keys = st.session_state.card_keys_master

    remembered_count = sum(
        1 for key in master_keys if st.session_state.card_status.get(key) == STATUS_UNDERSTOOD_JA
    )
    repeat_count = sum(
        1 for key in master_keys if st.session_state.card_status.get(key) == STATUS_NEEDS_REVIEW_JA
    )

    st.metric(label="✅ Understood", value=f"{remembered_count} / {current_range_total}")
    st.metric(label="🔄 Needs Review", value=f"{repeat_count} / {current_range_total}")

    if st.button("Reset Progress", use_container_width=True, help="Resets the status for ALL cards."):
        st.session_state.card_status = {key: INITIAL_STATUS_JA for key in list(flashcard_data.keys())}
        st.rerun()

    st.header("⚙️ Settings")
    st.subheader("Card Range")

    total_cards_overall = len(flashcard_data)

    start_num = st.number_input(
        "Start Card #", min_value=1, max_value=total_cards_overall, value=1, step=1
    )
    end_num = st.number_input(
        "End Card #",
        min_value=1,
        max_value=total_cards_overall,
        value=min(10, total_cards_overall),
        step=1,
    )

    st.toggle("Shuffle", key="shuffle_on", help="Shuffle the selected range.")
    if st.button("Apply Range", use_container_width=True):
        apply_range(start_num, end_num)
        st.rerun()

    st.divider()

    st.header("🔄 Review Mode")
    st.button(
        "Show Unmastered Only",
        on_click=filter_deck_for_review,
        use_container_width=True,
        help="Filters to show only 'Unchecked' and 'Needs Review' cards from your active range.",
    )
    st.button(
        "Show All Cards in Range",
        on_click=reset_to_master_deck,
        use_container_width=True,
        help="Resets the deck to show all cards in the range you last applied.",
    )

# --- Main Flashcard Area ---
st.title("ImageProcessing＿finalFlashcards 🗂️")

if not st.session_state.card_keys_active:
    st.warning("No cards loaded or the filtered deck is empty. Please set a range or choose a deck view.")
    if len(st.session_state.card_keys_master) > 0 and len(st.session_state.card_keys_active) == 0:
        st.info(
            "The current filtered deck is empty. All cards in your selected range might be marked as 'Understood'. "
            "Try 'Show All Cards in Range'."
        )
else:
    current_key = st.session_state.card_keys_active[st.session_state.current_index]
    current_answer = flashcard_data[current_key]

    current_status_ja = st.session_state.card_status.get(current_key, INITIAL_STATUS_JA)
    current_status_en = STATUS_MAP_JA_TO_EN.get(current_status_ja, "Unchecked")

    thai_translation = thai_translations.get(current_key, {})
    english_translation = english_translations.get(current_key, {})

    progress_value = (st.session_state.current_index + 1) / st.session_state.total_cards
    st.progress(
        progress_value,
        text=f"Card {st.session_state.current_index + 1} / {st.session_state.total_cards}",
    )

    card_placeholder = st.empty()

    # -------------------- QUESTION SIDE --------------------
    if not st.session_state.is_flipped:
        with card_placeholder.container():
            st.markdown(f"**Status:** {current_status_en}")

            with st.container(height=300, border=True):
                st.subheader("Question (Japanese Term):")
                render_content_with_latex(current_key)

            # Row 1: Actions & Navigation
            action_col1, action_col2, action_col3 = st.columns([1, 2, 1])
            with action_col1:
                st.button(
                    "⬅️ Previous",
                    on_click=prev_card,
                    use_container_width=True,
                    disabled=(st.session_state.current_index == 0),
                )
            with action_col2:
                if st.button("Show Answer ↩️", use_container_width=True):
                    st.session_state.is_flipped = True
                    st.rerun()
            with action_col3:
                st.button(
                    "Next ➡️",
                    on_click=next_card,
                    use_container_width=True,
                    disabled=(st.session_state.current_index == st.session_state.total_cards - 1),
                )

            # Row 2: Translations & Audio
            sec_col1, sec_col2, sec_col3 = st.columns(3)
            with sec_col1:
                if st.button("▶️ Audio", use_container_width=True, help="Play Question Audio"):
                    with st.spinner("Generating audio..."):
                        audio_uri = generate_audio(current_key)
                    st.session_state.audio_to_play = audio_uri
            with sec_col2:
                if st.button("🇹🇭 Thai", use_container_width=True, help="Show Thai Translation"):
                    st.session_state.show_thai_translation = (
                        None if st.session_state.show_thai_translation == "question" else "question"
                    )
                    st.rerun()
            with sec_col3:
                if st.button("🇬🇧 English", use_container_width=True, help="Show English Translation"):
                    st.session_state.show_english_translation = (
                        None if st.session_state.show_english_translation == "question" else "question"
                    )
                    st.rerun()

            # Audio player
            if st.session_state.audio_to_play:
                st.audio(st.session_state.audio_to_play)

            # Better translation render (Question)
            if st.session_state.show_english_translation == "question" and "question" in english_translation:
                render_translation_block("🇬🇧 English Translation (Question)", english_translation["question"])

            if st.session_state.show_thai_translation == "question" and "question" in thai_translation:
                render_translation_block("🇹🇭 Thai Translation (Question)", thai_translation["question"])

    # -------------------- ANSWER SIDE --------------------
    else:
        with card_placeholder.container():
            st.markdown(f"**Status:** {current_status_en}")

            with st.container(height=300, border=True):
                st.subheader("Answer (Japanese Explanation):")
                render_content_with_latex(current_answer)

            # Row 1: Actions & Navigation
            action_col1, action_col2, action_col3 = st.columns([1, 2, 1])
            with action_col1:
                st.button(
                    "⬅️ Previous",
                    on_click=prev_card,
                    use_container_width=True,
                    disabled=(st.session_state.current_index == 0),
                )
            with action_col2:
                if st.button("Hide Answer ↪️", use_container_width=True):
                    st.session_state.is_flipped = False
                    st.rerun()
            with action_col3:
                st.button(
                    "Next ➡️",
                    on_click=next_card,
                    use_container_width=True,
                    disabled=(st.session_state.current_index == st.session_state.total_cards - 1),
                )

            # Row 2: Translations & Audio
            sec_col1, sec_col2, sec_col3 = st.columns(3)
            with sec_col1:
                if st.button("▶️ Audio", use_container_width=True, help="Play Answer Audio"):
                    with st.spinner("Generating audio..."):
                        audio_uri = generate_audio(current_answer)
                    st.session_state.audio_to_play = audio_uri
            with sec_col2:
                if st.button("🇹🇭 Thai", use_container_width=True, help="Show Thai Translation"):
                    st.session_state.show_thai_translation = (
                        None if st.session_state.show_thai_translation == "answer" else "answer"
                    )
                    st.rerun()
            with sec_col3:
                if st.button("🇬🇧 English", use_container_width=True, help="Show English Translation"):
                    st.session_state.show_english_translation = (
                        None if st.session_state.show_english_translation == "answer" else "answer"
                    )
                    st.rerun()

            # Audio player
            if st.session_state.audio_to_play:
                st.audio(st.session_state.audio_to_play)

            # Better translation render (Answer)
            if st.session_state.show_english_translation == "answer" and "answer" in english_translation:
                render_translation_block("🇬🇧 English Translation (Answer)", english_translation["answer"])

            if st.session_state.show_thai_translation == "answer" and "answer" in thai_translation:
                render_translation_block("🇹🇭 Thai Translation (Answer)", thai_translation["answer"])

    st.divider()

    # --- Status buttons ---
    status_col1, status_col2 = st.columns(2)
    with status_col1:
        st.button(
            "✅ Understood",
            on_click=mark_status,
            args=(STATUS_UNDERSTOOD_JA,),
            use_container_width=True,
        )
    with status_col2:
        st.button(
            "🔄 Needs Review",
            on_click=mark_status,
            args=(STATUS_NEEDS_REVIEW_JA,),
            use_container_width=True,
        )
