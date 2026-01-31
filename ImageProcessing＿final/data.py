# -*- coding: utf-8 -*-

# --- 試験問題の質問文を変数として定義 (Japanese Question Variables) ---
q_1 = """1. 幾何学的変換後の画像を、再び縦横等間隔に標本化された位置の値の集まりとして表現するために必要な処理を何と呼ぶか。"""
q_2 = """2. 幾何学的変換の逆変換によって求めた入力画像上の位置が画素位置からずれている場合に、周囲の画素位置の値を利用してその位置の値を求める処理を何と呼ぶか。"""
q_3 = """3. 求めたい位置に最も近い画素位置の値を、そのままその位置の値として利用する補間方法を何と呼ぶか。"""
q_4 = """4. 求めたい位置を取り囲む周囲の4点の画素値を用い、計算によって値を求める補間方法を何と呼ぶか。"""
q_5 = """5. 求めたい位置を取り囲む周囲の16点の画素値を用い、3次多項式で近似して値を求める補間方法を何と呼ぶか。"""
q_6 = """6. グレースケール画像の中間値をなくし、白または黒の2値の画像に変換することを何と呼ぶか。"""
q_7 = """7. 2値画像を得るために、ある値以上の画素値を1、それ未満の画素値を0に変換する際の、境界となる値を何と呼ぶか。"""
q_8 = """8. 画像中の文字の占める領域の画素数が、文字の大きさからあらかじめ予測できる場合に、予測された画素数になるようにしきい値を決める方法を何と呼ぶか。"""
q_9 = """9. 黒画素クラスと白画素クラスの分布の分離度が大きくなるように (クラス間分散が最大になるように)しきい値を決める方法を何と呼ぶか。"""
q_10 = """10. あらかじめ標準パターンをテンプレートとして用意しておき、このテンプレートを用いて入力画像とのマッチングを行うことを何と呼ぶか。"""
q_11 = """11. テンプレートマッチングにおいて、画素値の差の2乗和を計算することで類似度を測る手法を何と呼ぶか。値が0に近いほど似ていることを表す。"""
q_12 = """12. テンプレートマッチングにおいて、画素値の差の絶対値の和を計算することで類似度を測る手法を何と呼ぶか。値が0に近いほど似ていることを表す。"""
q_13 = """13. 特徴点検出において、「ここが特徴的だ！」という座標(x, y)を見つけるのが仕事であるものを何と呼ぶか。"""
q_14 = """14. 特徴点検出において、渡された座標の見た目を数値データ (ベクトル)に変換するのが仕事であるものを何と呼ぶか。"""

# --- Additional Exam Questions (Theory & Calculation) ---
q_15 = """15. 画像の視覚的特徴や画素値そのものをパターンとよび、パターンの存在や位置を検出することを何と呼ぶか。"""
q_16 = """16. 左端から水平方向に、それを順次下の行に向かって探索すること（画像全体を総なめにするようにスライドすること）を何と呼ぶか。"""

q_17 = """17. 特徴点検出における「検出器 (Detector)」と「記述子 (Descriptor)」の違いを簡潔に説明せよ。"""
q_18 = """18. Harrisコーナー検出の特徴について、「回転不変性」と「スケール不変性」という言葉を用いて説明せよ。"""
q_19 = """19. SIFT (Scale-Invariant Feature Transform) が「最強のアルゴリズム」と呼ばれる理由を、そのロバスト性の観点から説明せよ。また、デメリットを1つ挙げよ。"""
q_20 = """20. BRIEF記述子の特徴（データ形式と速度）と、その弱点を説明せよ。"""
q_21 = """21. ORBアルゴリズムは、FASTとBRIEFをどのように改良したものか説明せよ。"""

q_22 = """22. 写真のような自然画像を拡大する場合、ニアレストネイバー法を用いるとどのような視覚的な問題（デメリット）が発生するか。「ジャギー」という言葉を用いて説明せよ。"""
q_23 = """23. ドット絵（ピクセルアート）やQRコードのような画像を拡大する場合、最も適している補間手法はどれか。また、その理由を説明せよ。"""
q_24 = """24. バイキュービック補間の特徴を、「画質」と「計算量」の観点から説明せよ。"""

q_25 = """25. モード法の弱点（デメリット）は何か。"""
q_26 = """26. 判別分析法（大津の方法）では、どのような基準でしきい値を自動決定するか。「クラス間分散」という言葉を用いて説明せよ。"""

q_27 = """27. 【計算問題：NN補間】
入力画像の画素値を f(x,y) とし、ニアレストネイバー法は I(x,y) = f([x+0.5], [y+0.5]) とする。[ ]はガウス記号（切り捨て）である。
求めたい座標が (1.6, 2.2) の場合、どの画素座標を参照するか答えよ。"""

q_28 = """28. 【計算問題：バイリニア補間】
周囲4点の画素値が f(0,0)=10, f(1,0)=20, f(0,1)=30, f(1,1)=40 である。
座標 (x,y) = (0.25, 0.75) の画素値を計算せよ。
(ヒント: I = (1-x)(1-y)f00 + x(1-y)f10 + (1-x)yf01 + xyf11 )"""

q_29 = """29. 【計算問題：p-タイル法】
画像の総画素数が40画素で、対象物（黒）が画像全体の25%を占めると分かっている。
ヒストグラムの画素数が「濃度0: 4個, 濃度1: 6個, 濃度2: 10個...」となっている場合、しきい値はいくつになるか。"""

q_30 = """30. 【計算問題：SSD/SAD】
テンプレート T = [[10, 20], [20, 10]]
入力画像領域 I = [[12, 20], [15, 10]]
この2つの領域の SAD (差の絶対値の和) と SSD (差の2乗和) を計算せよ。"""

# --- Mock Exam Questions ---
mock_q_1 = """Q1. 【用語定義】
(1) 「再標本化」を1文で定義せよ。
(2) 「補間」を1文で定義せよ。"""

mock_q_2 = """Q2. 【ニアレストネイバー法】
(1) この手法の意味（何を値として採用するか）を答えよ。
(2) 計算式 (I(x,y)=...) を答えよ。"""

mock_q_3 = """Q3. 【補間法の比較】
(1) バイリニア補間の参照画素数はいくつか。
(2) バイキュービック補間の参照画素数はいくつか。
(3) 写真の拡大に適しているのはどちらか？その理由は？"""

mock_q_4 = """Q4. 【2値化定義】
(1) 「2値化」とは何か。
(2) 「しきい値処理」とは具体的に何をする処理か。"""

mock_q_5 = """Q5. 【しきい値決定法】
以下の手法はどのようにしきい値を決めるか説明せよ。
(1) pタイル法
(2) モード法
(3) 大津法（判別分析法）"""

mock_q_6 = """Q6. 【探索手法】
(1) テンプレートマッチングとは何か。
(2) ラスタスキャンとはどのような探索方法か。"""

mock_q_7 = """Q7. 【結果比較：写真 vs ドット絵】
以下の結果特徴に当てはまる手法（NN / バイリニア / バイキュービック）を答えよ。
[写真の場合]
A：輪郭がブロック状でジャギーが目立つ
B：滑らかだが細部がぼける
C：比較的シャープで自然
[ドット絵の場合]
D：ドットの輪郭が保たれ、元の“ピクセル感”が残る"""

mock_q_8 = """Q8. 【2値化の理論と選択】
(1) 2値化が「情報を捨てる」処理と言われる理由は？
(2) 次の状況に最適な手法を選べ（pタイル/モード/大津）。
 状況Ⅰ：対象面積が「全体の30%」と既知
 状況Ⅱ：ヒストグラムが「2つの山」と「谷」を持つ
 状況Ⅲ：事前情報なし、自動で分離度を最大化したい"""

mock_q_9 = """Q9. 【アルゴリズム選択】
次の要求に最適なアルゴリズム（FAST/BRIEF/SIFT/ORB）を選べ。
(1) とにかく高速に特徴点を検出したい
(2) 記述子同士を高速比較（ハミング距離）したい
(3) 回転・スケール変化に強く、信頼性重視
(4) FASTの速さを活かしつつ、回転への弱点を改善したい"""

mock_q_10 = """Q10. 【計算：NN補間】
式：I(x,y) = f([x+0.5], [y+0.5])
座標 I(1.6, 2.2) は、入力画像のどの画素 f(?, ?) を参照するか。"""

mock_q_11 = """Q11. 【計算：バイリニア補間】
4点の画素値：f(0,0)=10, f(1,0)=20, f(0,1)=30, f(1,1)=40
座標 (x,y)=(0.25, 0.75) の補間値を計算せよ。"""

mock_q_12 = """Q12. 【計算：pタイル法】
ヒストグラム（濃度0〜7）：
0:4, 1:6, 2:10, 3:8, 4:6, 5:4, 6:2, 7:0 (計40画素)
黒領域が p=25% の場合、しきい値 t はいくつか？（どこまでを黒とするか）"""

mock_q_13 = """Q13. 【理論：大津法】
大津法（判別分析法）において、「良いしきい値」とされる基準は何か。"""

mock_q_14 = """Q14. 【計算：SSD/SAD】
入力 I = [[1,4,2], [0,3,1], [2,5,3]]
テンプレ T = [[1,3], [2,4]]
走査位置 (1,1), (1,2), (2,1), (2,2) のSSDとSADを計算し、最小位置（最も似ている場所）を答えよ。"""

# --- Flashcard Data Dictionary (Japanese) ---
flashcard_data = {
    q_1: "再標本化 (Resampling) {{Refer: exam.pdf (Source: 8, 72-75)}}",
    q_2: "補間 (Interpolation) {{Refer: exam.pdf (Source: 9, 76-80)}}",
    q_3: "ニアレストネイバー法 (Nearest Neighbor) {{Refer: exam.pdf (Source: 81-84)}}",
    q_4: "バイリニア補間 (Bilinear Interpolation) {{Refer: exam.pdf (Source: 85-89)}}",
    q_5: "バイキュービック補間 (Bicubic Interpolation) {{Refer: exam.pdf (Source: 90-93)}}",
    q_6: "2値化 (Binarization) {{Refer: exam.pdf (Source: 94-97)}}",
    q_7: "しきい値 (Threshold) {{Refer: exam.pdf (Source: 98-102)}}",
    q_8: "p-タイル法 (P-tile Method) {{Refer: exam.pdf (Source: 103-106)}}",
    q_9: "判別分析法 (Discriminant Analysis / Otsu's Method) {{Refer: exam.pdf (Source: 111-115)}}",
    q_10: "テンプレートマッチング (Template Matching) {{Refer: exam.pdf (Source: 120-124)}}",
    q_11: "SSD (Sum of Squared Differences) {{Refer: exam.pdf (Source: 316-320)}}",
    q_12: "SAD (Sum of Absolute Differences) {{Refer: exam.pdf (Source: 321-324)}}",
    q_13: "検出器 (Detector) {{Refer: exam.pdf (Source: 130-134)}}",
    q_14: "記述子 (Descriptor) {{Refer: exam.pdf (Source: 135-139)}}",
    q_15: "パターンマッチング (Pattern Matching) {{Refer: exam.pdf (Source: 116-119)}}",
    q_16: "ラスタスキャン (Raster Scan) {{Refer: exam.pdf (Source: 125-129, 372)}}",
    q_17: "検出器は「特徴的な場所(座標)」を見つけるもの。記述子は「その場所の見た目」を数値ベクトルに変換するもの。 {{Refer: exam.pdf (Source: 144-147)}}",
    q_18: "回転不変性はある（回してもコーナーはコーナーのまま）。しかしスケール不変性はない（拡大するとコーナーが緩やかなエッジに見えてしまう）。 {{Refer: exam.pdf (Source: 154-158)}}",
    q_19: "理由: 回転・拡大縮小（スケール）・照明変化のすべてに強く（不変性を持ち）、安定しているから。デメリット: 計算量が非常に多く、処理が重い。 {{Refer: exam.pdf (Source: 165-173)}}",
    q_20: "特徴: 0と1のバイナリ列で表現し、ハミング距離で超高速にマッチングできる。弱点: 回転させるとデータが変わり、マッチングできない（回転不変性がない）。 {{Refer: exam.pdf (Source: 175-182)}}",
    q_21: "FASTに「スケール不変性と向き」を追加し、BRIEFを「向きに合わせて回転」させることで回転不変性を持たせた（Rotated BRIEF）。 {{Refer: exam.pdf (Source: 183-187)}}",
    q_22: "画素がブロック状に拡大されるため、斜めの線や曲線に「ジャギー（階段状のギザギザ）」が発生する。 {{Refer: exam.pdf (Source: 205-208)}}",
    q_23: "手法: ニアレストネイバー法。理由: 中間色を作らず画素値をそのまま維持するため、境界（エッジ）がぼやけず、くっきり保てるから。 {{Refer: exam.pdf (Source: 214-219)}}",
    q_24: "画質: 最も自然で滑らか、かつシャープ。計算量: 参照画素が多く式も複雑なため、計算量が最も多く処理時間がかかる。 {{Refer: exam.pdf (Source: 220-224)}}",
    q_25: "ヒストグラムに明確な「谷」がない（単峰性やノイズが多い）画像では、しきい値を決められない。 {{Refer: exam.pdf (Source: 241-244)}}",
    q_26: "「クラス間分散」が最大になる（＝クラスの分離度が最も良くなる）値を計算で求めて決定する。 {{Refer: exam.pdf (Source: 253-257)}}",
    q_27: "参照座標: (2, 2)。 計算: [1.6+0.5]=[2.1]=2, [2.2+0.5]=[2.7]=2。 {{Refer: exam.pdf (Source: 396-400)}}",
    q_28: "答え: 27.5。 計算: (0.75*0.25*10) + (0.25*0.25*20) + (0.75*0.75*30) + (0.25*0.75*40) = 1.875 + 1.25 + 16.875 + 7.5 = 27.5 {{Refer: exam.pdf (Source: 401-407)}}",
    q_29: "しきい値: 2 (または t=1と2の間)。 計算: 黒画素数=40*0.25=10個。濃度0(4個)+濃度1(6個)=10個で累積が達するため、濃度1までを黒とする。 {{Refer: exam.pdf (Source: 408-417)}}",
    q_30: "SAD = 7, SSD = 29。 SAD計算: |12-10|+|20-20|+|15-20|+|10-10| = 2+0+5+0=7。 SSD計算: 2^2+0^2+(-5)^2+0^2 = 4+0+25+0=29。 {{Refer: exam.pdf (Source: 276-284)}}",
    mock_q_1: "(1) 再標本化：変換後の画像を、等間隔の画素格子上に作り直す処理。(2) 補間：小数位置の値を周囲画素から推定して求める処理。 {{Refer: Mock Exam Set A (Model Answer Q1)}}",
    mock_q_2: "(1) 最も近い画素の値をそのまま採用する。(2) I(x,y) = f([x+0.5], [y+0.5]) {{Refer: Mock Exam Set A (Model Answer Q2)}}",
    mock_q_3: "(1) 4点。(2) 16点。(3) バイキュービック（比較的シャープで自然なため）。 {{Refer: Mock Exam Set A (Model Answer Q3)}}",
    mock_q_4: "(1) 画素値を0(黒)と1(白)のみに置換する処理。(2) あるしきい値 t 以上を白、未満を黒（またはその逆）に分ける処理。 {{Refer: Mock Exam Set A (Model Answer Q4)}}",
    mock_q_5: "(1) 対象がp%と分かっている時、累積割合で決める。(2) ヒストグラムが双峰性（2つの山）の時、谷底を値とする。(3) クラス間分散が最大（クラス内分散が最小）となる値を探索する。 {{Refer: Mock Exam Set A (Model Answer Q5)}}",
    mock_q_6: "(1) テンプレートを動かして類似度（SSD/SAD）を計算し一致位置を探す。(2) 画像の左上から右へ、順次下の行へ移動する総なめ探索。 {{Refer: Mock Exam Set A (Model Answer Q6)}}",
    mock_q_7: "[写真] A=NN, B=バイリニア, C=バイキュービック。[ドット絵] D=NN（ピクセル感が残るため）。 {{Refer: Mock Exam Set A (Model Answer Q7)}}",
    mock_q_8: "(1) しきい値一つで0/1に落とすため、中間の濃淡情報が失われるから。(2) Ⅰ=pタイル, Ⅱ=モード, Ⅲ=大津。 {{Refer: Mock Exam Set A (Model Answer Q8)}}",
    mock_q_9: "(1) FAST。(2) BRIEF。(3) SIFT。(4) ORB。 {{Refer: Mock Exam Set A (Model Answer Q9)}}",
    mock_q_10: "参照画素: f(2, 2)。 計算: [1.6+0.5]=2, [2.2+0.5]=2。 {{Refer: Mock Exam Set A (Model Answer Q10)}}",
    mock_q_11: "答え: 27.5。 式: (0.75)(0.25)10 + (0.25)(0.25)20 + (0.75)(0.75)30 + (0.25)(0.75)40。 {{Refer: Mock Exam Set A (Model Answer Q11)}}",
    mock_q_12: "しきい値 t=2 (濃度0と1を黒とする)。 計算: 全体40画素×25%=10画素。濃度0(4個)+濃度1(6個)=10個なので、ここまでが黒。 {{Refer: Mock Exam Set A (Model Answer Q12)}}",
    mock_q_13: "クラス間分散が最大（またはクラス内分散が最小）となるしきい値。 {{Refer: Mock Exam Set A (Model Answer Q13)}}",
    mock_q_14: "最小位置: (2,1)。 (2,1)での値は SSD=2, SAD=2。 {{Refer: Mock Exam Set A (Model Answer Q14)}}"
}

# --- English Translations ---
english_translations = {
    q_1: {
        "question": "1. What is the process called that is required to re-express the transformed image as a collection of values on a regular grid?",
        "answer": "Resampling {{Refer: exam.pdf (Source: 8, 72-75)}}"
    },
    q_2: {
        "question": "2. What is the process called to find the value at a position using surrounding pixels when the inverse geometric transformation lands between pixel positions?",
        "answer": "Interpolation {{Refer: exam.pdf (Source: 9, 76-80)}}"
    },
    q_3: {
        "question": "3. What is the interpolation method that uses the value of the pixel position closest to the desired position as it is?",
        "answer": "Nearest Neighbor {{Refer: exam.pdf (Source: 81-84)}}"
    },
    q_4: {
        "question": "4. What is the interpolation method that calculates the value by using the pixel values of the surrounding 4 points?",
        "answer": "Bilinear Interpolation {{Refer: exam.pdf (Source: 85-89)}}"
    },
    q_5: {
        "question": "5. What is the interpolation method that calculates the value by approximating with a cubic polynomial using the pixel values of the surrounding 16 points?",
        "answer": "Bicubic Interpolation {{Refer: exam.pdf (Source: 90-93)}}"
    },
    q_6: {
        "question": "6. What is it called to convert a grayscale image into a binary image of white or black by eliminating intermediate values?",
        "answer": "Binarization {{Refer: exam.pdf (Source: 94-97)}}"
    },
    q_7: {
        "question": "7. What is the boundary value called that is used to convert pixel values to 1 (if above) or 0 (if below) to obtain a binary image?",
        "answer": "Threshold {{Refer: exam.pdf (Source: 98-102)}}"
    },
    q_8: {
        "question": "8. What is the method called to determine the threshold so that the number of pixels matches a predicted count, used when the area occupied by the object is known in advance?",
        "answer": "P-tile Method {{Refer: exam.pdf (Source: 103-106)}}"
    },
    q_9: {
        "question": "9. What is the method called to determine the threshold so that the separation between the black pixel class and white pixel class distributions is maximized (maximizing between-class variance)?",
        "answer": "Discriminant Analysis (Otsu's Method) {{Refer: exam.pdf (Source: 111-115)}}"
    },
    q_10: {
        "question": "10. What is it called when a standard pattern is prepared as a template in advance and used to perform matching with the input image?",
        "answer": "Template Matching {{Refer: exam.pdf (Source: 120-124)}}"
    },
    q_11: {
        "question": "11. In template matching, what is the method that measures similarity by calculating the sum of squared differences of pixel values? (Values closer to 0 indicate higher similarity)",
        "answer": "SSD (Sum of Squared Differences) {{Refer: exam.pdf (Source: 316-320)}}"
    },
    q_12: {
        "question": "12. In template matching, what is the method that measures similarity by calculating the sum of absolute differences of pixel values? (Values closer to 0 indicate higher similarity)",
        "answer": "SAD (Sum of Absolute Differences) {{Refer: exam.pdf (Source: 321-324)}}"
    },
    q_13: {
        "question": "13. In feature detection, what is the component called whose job is to find the coordinates (x, y) that are \"distinctive\"?",
        "answer": "Detector {{Refer: exam.pdf (Source: 130-134)}}"
    },
    q_14: {
        "question": "14. In feature detection, what is the component called whose job is to convert the appearance at the given coordinates into numerical data (vector)?",
        "answer": "Descriptor {{Refer: exam.pdf (Source: 135-139)}}"
    },
    q_15: {
        "question": "15. What is the process called that detects the presence or position of a pattern (visual features or pixel values themselves)?",
        "answer": "Pattern Matching {{Refer: exam.pdf (Source: 116-119)}}"
    },
    q_16: {
        "question": "16. What is the process called of scanning horizontally from the left edge and sequentially moving to the rows below (sliding across the entire image)?",
        "answer": "Raster Scan {{Refer: exam.pdf (Source: 125-129, 372)}}"
    },
    q_17: {
        "question": "17. Briefly explain the difference between a 'Detector' and a 'Descriptor' in feature point detection.",
        "answer": "A Detector finds the 'distinctive location (coordinates)'. A Descriptor converts the 'appearance' at that location into a numerical vector. {{Refer: exam.pdf (Source: 144-147)}}"
    },
    q_18: {
        "question": "18. Explain the characteristics of Harris Corner Detection using the terms 'Rotation Invariance' and 'Scale Invariance'.",
        "answer": "It HAS Rotation Invariance (corners remain corners when rotated). It does NOT have Scale Invariance (corners look like edges when zoomed in). {{Refer: exam.pdf (Source: 154-158)}}"
    },
    q_19: {
        "question": "19. Explain why SIFT is called the 'strongest algorithm' regarding robustness, and list one demerit.",
        "answer": "Reason: It is robust (invariant) to Rotation, Scale, and Lighting changes. Demerit: Computation is very heavy/slow. {{Refer: exam.pdf (Source: 165-173)}}"
    },
    q_20: {
        "question": "20. Explain the characteristics (data format & speed) and weakness of the BRIEF descriptor.",
        "answer": "Characteristics: Uses binary strings (0s and 1s) and Hamming distance for very fast matching. Weakness: Not Rotation Invariant (fails if rotated). {{Refer: exam.pdf (Source: 175-182)}}"
    },
    q_21: {
        "question": "21. Explain how the ORB algorithm improved upon FAST and BRIEF.",
        "answer": "It added Scale Invariance and Orientation to FAST, and made BRIEF Rotation Invariant (Rotated BRIEF) by steering it according to orientation. {{Refer: exam.pdf (Source: 183-187)}}"
    },
    q_22: {
        "question": "22. When enlarging a natural image (photo) using Nearest Neighbor, what visual problem occurs? Explain using the word 'jaggies'.",
        "answer": "Because pixels are enlarged as blocks, 'jaggies' (staircase-like jagged edges) appear on diagonal lines and curves. {{Refer: exam.pdf (Source: 205-208)}}"
    },
    q_23: {
        "question": "23. Which interpolation method is best for enlarging Pixel Art or QR codes, and why?",
        "answer": "Method: Nearest Neighbor. Reason: It preserves original pixel values without creating intermediate colors, keeping edges sharp and distinct. {{Refer: exam.pdf (Source: 214-219)}}"
    },
    q_24: {
        "question": "24. Explain the characteristics of Bicubic interpolation in terms of 'Image Quality' and 'Computation Cost'.",
        "answer": "Quality: Most natural, smooth, and sharp. Cost: Highest computation cost (slowest) due to using many pixels and complex formulas. {{Refer: exam.pdf (Source: 220-224)}}"
    },
    q_25: {
        "question": "25. What is the weakness of the Mode Method for thresholding?",
        "answer": "It cannot determine a threshold if the histogram does not have a clear 'valley' (e.g., single peak or too much noise). {{Refer: exam.pdf (Source: 241-244)}}"
    },
    q_26: {
        "question": "26. On what basis does Discriminant Analysis (Otsu's Method) automatically determine the threshold? Explain using 'between-class variance'.",
        "answer": "It calculates and selects the threshold that maximizes the 'between-class variance' (best separation between black and white classes). {{Refer: exam.pdf (Source: 253-257)}}"
    },
    q_27: {
        "question": "27. [Calculation: NN Interpolation] Input values are f(x,y). NN uses I(x,y) = f([x+0.5], [y+0.5]). If the desired coordinate is (1.6, 2.2), which pixel coordinate is referenced?",
        "answer": "Reference: (2, 2). Calculation: [1.6+0.5]=2, [2.2+0.5]=2. {{Refer: exam.pdf (Source: 396-400)}}"
    },
    q_28: {
        "question": "28. [Calculation: Bilinear Interpolation] Surrounding 4 pixels are f(0,0)=10, f(1,0)=20, f(0,1)=30, f(1,1)=40. Calculate the value at (0.25, 0.75).",
        "answer": "Answer: 27.5. Calculation: Weighted sum of the 4 points based on distance. {{Refer: exam.pdf (Source: 401-407)}}"
    },
    q_29: {
        "question": "29. [Calculation: P-tile Method] Total pixels = 40. Object (black) = 25%. Histogram counts: Density 0: 4px, Density 1: 6px, Density 2: 10px... What is the threshold?",
        "answer": "Threshold: 2 (separating 0-1 from 2+). Calculation: Black pixels = 40 * 0.25 = 10. Sum of Density 0 (4) + Density 1 (6) = 10. {{Refer: exam.pdf (Source: 408-417)}}"
    },
    q_30: {
        "question": "30. [Calculation: SAD/SSD] Template T=[[10, 20], [20, 10]], Input I=[[12, 20], [15, 10]]. Calculate SAD and SSD.",
        "answer": "SAD = 7, SSD = 29. SAD sums absolute diffs (|2|+0+|5|+0). SSD sums squared diffs (4+0+25+0). {{Refer: exam.pdf (Source: 276-284)}}"
    },
    mock_q_1: {
        "question": "Q1. Define (1) Resampling and (2) Interpolation in one sentence each.",
        "answer": "(1) Resampling: Re-creating the transformed image on a regular pixel grid. (2) Interpolation: Estimating values at non-integer positions using surrounding pixels. {{Refer: Mock Exam Set A}}"
    },
    mock_q_2: {
        "question": "Q2. Nearest Neighbor: (1) What is its meaning? (2) Write the formula.",
        "answer": "(1) Uses the value of the closest pixel directly. (2) I(x,y) = f([x+0.5], [y+0.5]) {{Refer: Mock Exam Set A}}"
    },
    mock_q_3: {
        "question": "Q3. Compare Interpolation: (1) Bilinear uses how many pixels? (2) Bicubic uses how many? (3) Which is better for photos?",
        "answer": "(1) 4 pixels. (2) 16 pixels. (3) Bicubic (because it produces sharper and more natural results). {{Refer: Mock Exam Set A}}"
    },
    mock_q_4: {
        "question": "Q4. Define (1) Binarization and (2) Thresholding.",
        "answer": "(1) Converting pixel values to only 0 (black) and 1 (white). (2) Dividing pixels into white (>= t) and black (< t) based on a threshold t. {{Refer: Mock Exam Set A}}"
    },
    mock_q_5: {
        "question": "Q5. How do these methods determine the threshold? (1) P-tile, (2) Mode, (3) Otsu.",
        "answer": "(1) P-tile: Based on cumulative ratio when object area (p%) is known. (2) Mode: Bottom of the valley between two peaks. (3) Otsu: Maximizes between-class variance. {{Refer: Mock Exam Set A}}"
    },
    mock_q_6: {
        "question": "Q6. Explain (1) Template Matching and (2) Raster Scan.",
        "answer": "(1) Finding a match by moving a template and calculating similarity (SSD/SAD). (2) Scanning strictly from top-left to right, then next row down. {{Refer: Mock Exam Set A}}"
    },
    mock_q_7: {
        "question": "Q7. Match method (NN/Bilinear/Bicubic) to result: [Photo] A: Blocky/Jaggies, B: Blurry, C: Sharp/Natural. [Pixel Art] D: Preserves pixel sharp edges.",
        "answer": "[Photo] A=NN, B=Bilinear, C=Bicubic. [Pixel Art] D=NN (Best for preserving pixel art edges). {{Refer: Mock Exam Set A}}"
    },
    mock_q_8: {
        "question": "Q8. (1) Why does binarization 'lose information'? (2) Choose method for: I. Known Area %, II. Two Peaks, III. Automatic max separation.",
        "answer": "(1) Because it reduces all grayscale data to just 0/1. (2) I=P-tile, II=Mode, III=Otsu. {{Refer: Mock Exam Set A}}"
    },
    mock_q_9: {
        "question": "Q9. Select algorithm (FAST/BRIEF/SIFT/ORB) for: (1) Fastest detection, (2) Fast comparison, (3) Robustness, (4) Fast + Rotation support.",
        "answer": "(1) FAST. (2) BRIEF. (3) SIFT. (4) ORB. {{Refer: Mock Exam Set A}}"
    },
    mock_q_10: {
        "question": "Q10. [Calc: NN Interpolation] Formula: I(x,y) = f([x+0.5], [y+0.5]). For I(1.6, 2.2), which input pixel f(?, ?) is used?",
        "answer": "Pixel: f(2, 2). Calculation: [1.6+0.5]=2, [2.2+0.5]=2. {{Refer: Mock Exam Set A}}"
    },
    mock_q_11: {
        "question": "Q11. [Calc: Bilinear] 4 pixels: 10, 20, 30, 40. Calculate value at (0.25, 0.75).",
        "answer": "Answer: 27.5. Formula: Weighted sum based on distance from the 4 points. {{Refer: Mock Exam Set A}}"
    },
    mock_q_12: {
        "question": "Q12. [Calc: P-tile] Total 40 pixels. Black object = 25%. Histogram: 0:4, 1:6, 2:10... Find threshold t.",
        "answer": "Threshold t=2 (Density 0 and 1 are black). Calculation: 40*0.25=10 pixels. Sum of dens 0(4) + dens 1(6) = 10. {{Refer: Mock Exam Set A}}"
    },
    mock_q_13: {
        "question": "Q13. What is the criterion for a 'good threshold' in Otsu's Method?",
        "answer": "A threshold that maximizes the Between-Class Variance (or minimizes Within-Class Variance). {{Refer: Mock Exam Set A}}"
    },
    mock_q_14: {
        "question": "Q14. [Calc: SSD/SAD] Input I=[[1,4,2],[0,3,1],[2,5,3]], Template T=[[1,3],[2,4]]. Find the (x,y) with minimum SSD/SAD.",
        "answer": "Minimum Position: (2,1). Values at (2,1): SSD=2, SAD=2. {{Refer: Mock Exam Set A}}"
    }
}

# --- Thai Translations ---
thai_translations = {
    q_1: {
        "question": "1. กระบวนการที่จำเป็นในการแสดงภาพที่ถูกแปลงทางเรขาคณิตอีกครั้งเป็นชุดของค่าบนตารางพิกัดปกติเรียกว่าอะไร",
        "answer": "การสุ่มตัวอย่างใหม่ (Resampling) {{Refer: exam.pdf (Source: 8, 72-75)}}"
    },
    q_2: {
        "question": "2. กระบวนการในการหาค่าพิกเซลที่ตำแหน่งซึ่งไม่ใช่จำนวนเต็ม โดยใช้ค่าของพิกเซลรอบข้าง เมื่อการแปลงย้อนกลับทางเรขาคณิตตกลงระหว่างตำแหน่งพิกเซล เรียกว่าอะไร",
        "answer": "การประมาณค่าในช่วง (Interpolation) {{Refer: exam.pdf (Source: 9, 76-80)}}"
    },
    q_3: {
        "question": "3. วิธีการประมาณค่าในช่วงที่ใช้ค่าของตำแหน่งพิกเซลที่ใกล้ที่สุดกับตำแหน่งที่ต้องการโดยตรง เรียกว่าอะไร",
        "answer": "วิธีเพื่อนบ้านที่ใกล้ที่สุด (Nearest Neighbor) {{Refer: exam.pdf (Source: 81-84)}}"
    },
    q_4: {
        "question": "4. วิธีการประมาณค่าในช่วงที่คำนวณค่าโดยใช้ค่าพิกเซลของจุดรอบข้าง 4 จุด เรียกว่าอะไร",
        "answer": "การประมาณค่าในช่วงแบบไบลิเนียร์ (Bilinear Interpolation) {{Refer: exam.pdf (Source: 85-89)}}"
    },
    q_5: {
        "question": "5. วิธีการประมาณค่าในช่วงที่คำนวณค่าโดยการประมาณด้วยพหุนามกำลังสาม โดยใช้ค่าพิกเซลของจุดรอบข้าง 16 จุด เรียกว่าอะไร",
        "answer": "การประมาณค่าในช่วงแบบไบคิวบิก (Bicubic Interpolation) {{Refer: exam.pdf (Source: 90-93)}}"
    },
    q_6: {
        "question": "6. การแปลงภาพระดับเทาให้เป็นภาพแบบไบนารีที่มีแค่สีขาวหรือดำ โดยการกำจัดค่ากึ่งกลาง เรียกว่าอะไร",
        "answer": "การทำภาพไบนารี (Binarization) {{Refer: exam.pdf (Source: 94-97)}}"
    },
    q_7: {
        "question": "7. ค่าขอบเขตที่ใช้ในการแปลงค่าพิกเซลเป็น 1 (ถ้ามากกว่า) หรือ 0 (ถ้าน้อยกว่า) เพื่อให้ได้ภาพแบบไบนารี เรียกว่าอะไร",
        "answer": "ค่าเกณฑ์ (Threshold) {{Refer: exam.pdf (Source: 98-102)}}"
    },
    q_8: {
        "question": "8. วิธีการกำหนดค่าเกณฑ์เพื่อให้จำนวนพิกเซลตรงกับจำนวนที่คาดการณ์ไว้ ซึ่งใช้เมื่อทราบพื้นที่ที่วัตถุครอบครองล่วงหน้า เรียกว่าอะไร",
        "answer": "วิธี P-tile (P-tile Method) {{Refer: exam.pdf (Source: 103-106)}}"
    },
    q_9: {
        "question": "9. วิธีการกำหนดค่าเกณฑ์เพื่อให้การแยกกันระหว่างกลุ่มพิกเซลสีดำและสีขาวมีค่าสูงสุด (ทำให้ความแปรปรวนระหว่างกลุ่มสูงสุด) เรียกว่าอะไร",
        "answer": "วิธีการวิเคราะห์การจำแนกกลุ่ม (Discriminant Analysis / Otsu's Method) {{Refer: exam.pdf (Source: 111-115)}}"
    },
    q_10: {
        "question": "10. การเตรียมรูปแบบมาตรฐานไว้เป็นแม่แบบล่วงหน้า และใช้แม่แบบนี้เพื่อทำการจับคู่กับภาพอินพุต เรียกว่าอะไร",
        "answer": "การจับคู่แม่แบบ (Template Matching) {{Refer: exam.pdf (Source: 120-124)}}"
    },
    q_11: {
        "question": "11. ในการจับคู่แม่แบบ วิธีการวัดความคล้ายคลึงโดยการคำนวณผลรวมของผลต่างยกกำลังสองของค่าพิกเซลเรียกว่าอะไร (ค่ายิ่งใกล้ 0 ยิ่งเหมือนมาก)",
        "answer": "SSD (ผลรวมของผลต่างยกกำลังสอง) {{Refer: exam.pdf (Source: 316-320)}}"
    },
    q_12: {
        "question": "12. ในการจับคู่แม่แบบ วิธีการวัดความคล้ายคลึงโดยการคำนวณผลรวมของผลต่างสัมบูรณ์ของค่าพิกเซลเรียกว่าอะไร (ค่ายิ่งใกล้ 0 ยิ่งเหมือนมาก)",
        "answer": "SAD (ผลรวมของผลต่างสัมบูรณ์) {{Refer: exam.pdf (Source: 321-324)}}"
    },
    q_13: {
        "question": "13. ในการตรวจจับจุดลักษณะเด่น องค์ประกอบที่มีหน้าที่ค้นหาพิกัด (x, y) ที่ \"โดดเด่น\" เรียกว่าอะไร",
        "answer": "ตัวตรวจจับ (Detector) {{Refer: exam.pdf (Source: 130-134)}}"
    },
    q_14: {
        "question": "14. ในการตรวจจับจุดลักษณะเด่น องค์ประกอบที่มีหน้าที่แปลงรูปลักษณ์ที่พิกัดที่กำหนดให้เป็นข้อมูลตัวเลข (เวกเตอร์) เรียกว่าอะไร",
        "answer": "ตัวบรรยายลักษณะ (Descriptor) {{Refer: exam.pdf (Source: 135-139)}}"
    },
    q_15: {
        "question": "15. กระบวนการที่ตรวจจับการมีอยู่หรือตำแหน่งของรูปแบบ (คุณลักษณะทางภาพหรือค่าพิกเซล) เรียกว่าอะไร",
        "answer": "การจับคู่รูปแบบ (Pattern Matching) {{Refer: exam.pdf (Source: 116-119)}}"
    },
    q_16: {
        "question": "16. การสแกนในแนวนอนจากขอบซ้ายและเลื่อนไปยังแถวด้านล่างตามลำดับ (เลื่อนไปทั่วทั้งภาพ) เรียกว่าอะไร",
        "answer": "การสแกนแบบราสเตอร์ (Raster Scan) {{Refer: exam.pdf (Source: 125-129, 372)}}"
    },
    q_17: {
        "question": "17. จงอธิบายความแตกต่างระหว่าง 'ตัวตรวจจับ (Detector)' และ 'ตัวบรรยายลักษณะ (Descriptor)' ในการตรวจจับจุดลักษณะเด่นโดยย่อ",
        "answer": "ตัวตรวจจับทำหน้าที่ค้นหา 'ตำแหน่ง (พิกัด) ที่โดดเด่น' ส่วนตัวบรรยายลักษณะทำหน้าที่แปลง 'รูปลักษณ์' ณ ตำแหน่งนั้นให้เป็นเวกเตอร์ตัวเลข {{Refer: exam.pdf (Source: 144-147)}}"
    },
    q_18: {
        "question": "18. จงอธิบายลักษณะของการตรวจจับมุมแบบแฮร์ริส (Harris Corner) โดยใช้คำว่า 'ความไม่แปรเปลี่ยนต่อการหมุน (Rotation Invariance)' และ 'ความไม่แปรเปลี่ยนต่อขนาด (Scale Invariance)'",
        "answer": "มันมี 'ความไม่แปรเปลี่ยนต่อการหมุน' (หมุนภาพแล้วมุมยังคงเป็นมุม) แต่ไม่มี 'ความไม่แปรเปลี่ยนต่อขนาด' (ซูมเข้าแล้วมุมจะดูเหมือนขอบ) {{Refer: exam.pdf (Source: 154-158)}}"
    },
    q_19: {
        "question": "19. จงอธิบายว่าทำไม SIFT ถึงถูกเรียกว่าเป็น 'อัลกอริทึมที่แข็งแกร่งที่สุด' ในแง่ของความทนทาน (Robustness) และข้อเสีย 1 ประการ",
        "answer": "เหตุผล: ทนทานต่อการหมุน การเปลี่ยนขนาด และการเปลี่ยนแปลงแสง ข้อเสีย: การคำนวณหนักและช้ามาก {{Refer: exam.pdf (Source: 165-173)}}"
    },
    q_20: {
        "question": "20. จงอธิบายลักษณะ (รูปแบบข้อมูลและความเร็ว) และจุดอ่อนของตัวบรรยายลักษณะแบบ BRIEF",
        "answer": "ลักษณะ: ใช้สตริงไบนารี (0 และ 1) และระยะทางแฮมมิงเพื่อการจับคู่ที่เร็วมาก จุดอ่อน: ไม่ทนทานต่อการหมุน (ล้มเหลวถ้าภาพหมุน) {{Refer: exam.pdf (Source: 175-182)}}"
    },
    q_21: {
        "question": "21. อัลกอริทึม ORB ปรับปรุงจาก FAST และ BRIEF อย่างไร",
        "answer": "เพิ่มความทนทานต่อขนาดและทิศทางให้กับ FAST และทำให้ BRIEF ทนทานต่อการหมุน (Rotated BRIEF) โดยการหมุนตามทิศทางของจุด {{Refer: exam.pdf (Source: 183-187)}}"
    },
    q_22: {
        "question": "22. เมื่อขยายภาพธรรมชาติ (ภาพถ่าย) โดยใช้วิธี Nearest Neighbor จะเกิดปัญหาทางสายตาอะไร? จงอธิบายโดยใช้คำว่า 'รอยหยัก (Jaggies)'",
        "answer": "เนื่องจากพิกเซลถูกขยายเป็นบล็อก จึงเกิด 'รอยหยัก (Jaggies)' (ขอบหยักเหมือนบันได) บนเส้นทแยงมุมและเส้นโค้ง {{Refer: exam.pdf (Source: 205-208)}}"
    },
    q_23: {
        "question": "23. วิธีการประมาณค่าในช่วงใดเหมาะสมที่สุดสำหรับการขยายภาพศิลปะพิกเซล (Pixel Art) หรือ QR Code และเพราะเหตุใด",
        "answer": "วิธี: Nearest Neighbor เหตุผล: รักษาค่าพิกเซลเดิมโดยไม่สร้างสีระหว่างกลาง ทำให้ขอบคมชัด {{Refer: exam.pdf (Source: 214-219)}}"
    },
    q_24: {
        "question": "24. จงอธิบายลักษณะของการประมาณค่าแบบ Bicubic ในแง่ของ 'คุณภาพของภาพ' และ 'ต้นทุนการคำนวณ'",
        "answer": "คุณภาพ: เป็นธรรมชาติและคมชัดที่สุด ต้นทุน: การคำนวณสูงที่สุด (ช้าที่สุด) เนื่องจากใช้จุดอ้างอิงและสูตรซับซ้อน {{Refer: exam.pdf (Source: 220-224)}}"
    },
    q_25: {
        "question": "25. จุดอ่อนของวิธี Mode Method ในการหาค่าเกณฑ์คืออะไร",
        "answer": "ไม่สามารถกำหนดค่าเกณฑ์ได้หากฮิสโตแกรมไม่มี 'หุบเขา' ที่ชัดเจน (เช่น มีขุนเขาเดียวหรือมีสัญญาณรบกวนมาก) {{Refer: exam.pdf (Source: 241-244)}}"
    },
    q_26: {
        "question": "26. วิธีการวิเคราะห์การจำแนกกลุ่ม (Otsu's Method) กำหนดค่าเกณฑ์โดยอัตโนมัติบนพื้นฐานใด? จงอธิบายโดยใช้คำว่า 'ความแปรปรวนระหว่างคลาส'",
        "answer": "คำนวณและเลือกค่าเกณฑ์ที่ทำให้ 'ความแปรปรวนระหว่างคลาส' มีค่าสูงสุด (แยกคลาสดำและขาวได้ดีที่สุด) {{Refer: exam.pdf (Source: 253-257)}}"
    },
    q_27: {
        "question": "27. [การคำนวณ: NN Interpolation] ค่าอินพุตคือ f(x,y) วิธี NN ใช้สูตร I(x,y) = f([x+0.5], [y+0.5]) หากพิกัดที่ต้องการคือ (1.6, 2.2) จะอ้างอิงพิกัดพิกเซลใด",
        "answer": "อ้างอิง: (2, 2) การคำนวณ: [1.6+0.5]=[2.1]=2, [2.2+0.5]=[2.7]=2 {{Refer: exam.pdf (Source: 396-400)}}"
    },
    q_28: {
        "question": "28. [การคำนวณ: Bilinear Interpolation] พิกเซลรอบข้าง 4 จุดคือ f(0,0)=10, f(1,0)=20, f(0,1)=30, f(1,1)=40 จงคำนวณค่าที่พิกัด (0.25, 0.75)",
        "answer": "คำตอบ: 27.5 การคำนวณ: ผลรวมถ่วงน้ำหนักของ 4 จุดตามระยะห่าง {{Refer: exam.pdf (Source: 401-407)}}"
    },
    q_29: {
        "question": "29. [การคำนวณ: P-tile Method] พิกเซลทั้งหมด = 40 วัตถุ (สีดำ) = 25% ฮิสโตแกรม: ความเข้ม 0: 4px, ความเข้ม 1: 6px, ความเข้ม 2: 10px... ค่าเกณฑ์คือเท่าใด",
        "answer": "ค่าเกณฑ์: 2 (แบ่งระหว่าง 0-1 และ 2+) การคำนวณ: พิกเซลสีดำ = 40 * 0.25 = 10 ผลรวมความเข้ม 0 (4) + ความเข้ม 1 (6) = 10 พอดี {{Refer: exam.pdf (Source: 408-417)}}"
    },
    q_30: {
        "question": "30. [การคำนวณ: SAD/SSD] แม่แบบ T=[[10, 20], [20, 10]], อินพุต I=[[12, 20], [15, 10]] จงคำนวณ SAD และ SSD",
        "answer": "SAD = 7, SSD = 29. SAD รวมผลต่างสัมบูรณ์ (|2|+0+|5|+0) SSD รวมผลต่างยกกำลังสอง (4+0+25+0) {{Refer: exam.pdf (Source: 276-284)}}"
    },
    mock_q_1: {
        "question": "Q1. นิยาม (1) การสุ่มตัวอย่างใหม่ (Resampling) และ (2) การประมาณค่าในช่วง (Interpolation) มาอย่างละ 1 ประโยค",
        "answer": "(1) การสุ่มตัวอย่างใหม่: การสร้างภาพที่แปลงแล้วขึ้นใหม่บนตารางพิกเซลปกติ (2) การประมาณค่าในช่วง: การประมาณค่าที่ตำแหน่งทศนิยมโดยใช้พิกเซลรอบข้าง {{Refer: Mock Exam Set A}}"
    },
    mock_q_2: {
        "question": "Q2. วิธี Nearest Neighbor: (1) ความหมายคืออะไร (2) เขียนสูตร",
        "answer": "(1) ใช้ค่าของพิกเซลที่อยู่ใกล้ที่สุดโดยตรง (2) I(x,y) = f([x+0.5], [y+0.5]) {{Refer: Mock Exam Set A}}"
    },
    mock_q_3: {
        "question": "Q3. เปรียบเทียบการประมาณค่า: (1) Bilinear ใช้กี่พิกเซล (2) Bicubic ใช้กี่พิกเซล (3) วิธีไหนเหมาะกับภาพถ่าย?",
        "answer": "(1) 4 จุด (2) 16 จุด (3) Bicubic (เพราะให้ภาพที่คมชัดและเป็นธรรมชาติกว่า) {{Refer: Mock Exam Set A}}"
    },
    mock_q_4: {
        "question": "Q4. นิยาม (1) การทำภาพไบนารี (Binarization) และ (2) การกำหนดค่าเกณฑ์ (Thresholding)",
        "answer": "(1) การแปลงค่าพิกเซลเป็น 0 (ดำ) และ 1 (ขาว) เท่านั้น (2) การแบ่งพิกเซลเป็นขาว (>= t) และดำ (< t) ตามค่าเกณฑ์ t {{Refer: Mock Exam Set A}}"
    },
    mock_q_5: {
        "question": "Q5. วิธีเหล่านี้กำหนดค่าเกณฑ์อย่างไร? (1) P-tile (2) Mode (3) Otsu",
        "answer": "(1) P-tile: ใช้สัดส่วนสะสมเมื่อรู้พื้นที่วัตถุ (p%) (2) Mode: ใช้ก้นหุบเขาระหว่างยอดกราฟสองยอด (3) Otsu: หาค่าที่ทำให้ความแปรปรวนระหว่างคลาสสูงสุด {{Refer: Mock Exam Set A}}"
    },
    mock_q_6: {
        "question": "Q6. อธิบาย (1) การจับคู่แม่แบบ (Template Matching) และ (2) การสแกนแบบราสเตอร์ (Raster Scan)",
        "answer": "(1) การหาตำแหน่งที่ตรงกันโดยเลื่อนแม่แบบและคำนวณความเหมือน (SSD/SAD) (2) การสแกนไล่จากซ้ายบนไปขวา แล้วลงบรรทัดถัดไป {{Refer: Mock Exam Set A}}"
    },
    mock_q_7: {
        "question": "Q7. จับคู่วิธี (NN/Bilinear/Bicubic) กับผลลัพธ์: [ภาพถ่าย] A: เป็นบล็อก/รอยหยัก, B: เบลอ, C: คมชัด/ธรรมชาติ [Pixel Art] D: ขอบคมชัด",
        "answer": "[ภาพถ่าย] A=NN, B=Bilinear, C=Bicubic [Pixel Art] D=NN (ดีที่สุดสำหรับรักษาขอบ Pixel Art) {{Refer: Mock Exam Set A}}"
    },
    mock_q_8: {
        "question": "Q8. (1) ทำไมการทำภาพไบนารีถึง 'สูญเสียข้อมูล'? (2) เลือกวิธีสำหรับ: I. รู้พื้นที่ %, II. กราฟสองยอด, III. แยกอัตโนมัติสูงสุด",
        "answer": "(1) เพราะลดข้อมูลเฉดสีเทาทั้งหมดเหลือแค่ 0/1 (2) I=P-tile, II=Mode, III=Otsu {{Refer: Mock Exam Set A}}"
    },
    mock_q_9: {
        "question": "Q9. เลือกอัลกอริทึม (FAST/BRIEF/SIFT/ORB) สำหรับ: (1) ตรวจจับเร็วสุด (2) เปรียบเทียบเร็ว (3) ทนทานสูง (4) เร็ว+รองรับการหมุน",
        "answer": "(1) FAST (2) BRIEF (3) SIFT (4) ORB {{Refer: Mock Exam Set A}}"
    },
    mock_q_10: {
        "question": "Q10. [คำนวณ: NN] สูตร: I(x,y) = f([x+0.5], [y+0.5]) สำหรับ I(1.6, 2.2) จะใช้พิกเซลอินพุต f(?, ?) ใด?",
        "answer": "พิกเซล: f(2, 2) การคำนวณ: [1.6+0.5]=2, [2.2+0.5]=2 {{Refer: Mock Exam Set A}}"
    },
    mock_q_11: {
        "question": "Q11. [คำนวณ: Bilinear] 4 พิกเซล: 10, 20, 30, 40 จงคำนวณค่าที่ (0.25, 0.75)",
        "answer": "คำตอบ: 27.5 คำนวณจากผลรวมถ่วงน้ำหนักของ 4 จุด {{Refer: Mock Exam Set A}}"
    },
    mock_q_12: {
        "question": "Q12. [คำนวณ: P-tile] ทั้งหมด 40 พิกเซล วัตถุดำ = 25% ฮิสโตแกรม: 0:4, 1:6, 2:10... จงหาค่าเกณฑ์ t",
        "answer": "ค่าเกณฑ์ t=2 (ความเข้ม 0 และ 1 เป็นสีดำ) คำนวณ: 40*0.25=10 พิกเซล ผลรวมความเข้ม 0(4) + 1(6) = 10 พอดี {{Refer: Mock Exam Set A}}"
    },
    mock_q_13: {
        "question": "Q13. เกณฑ์สำหรับ 'ค่าเกณฑ์ที่ดี' ในวิธี Otsu คืออะไร?",
        "answer": "ค่าเกณฑ์ที่ทำให้ความแปรปรวนระหว่างคลาส (Between-Class Variance) มีค่าสูงสุด {{Refer: Mock Exam Set A}}"
    },
    mock_q_14: {
        "question": "Q14. [คำนวณ: SSD/SAD] Input I=[[1,4,2],[0,3,1],[2,5,3]], Template T=[[1,3],[2,4]] จงหาตำแหน่ง (x,y) ที่ SSD/SAD ต่ำสุด",
        "answer": "ตำแหน่งต่ำสุด: (2,1) ค่าที่ตำแหน่งนี้: SSD=2, SAD=2 {{Refer: Mock Exam Set A}}"
    }
}