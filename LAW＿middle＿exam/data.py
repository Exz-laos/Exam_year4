# -*- coding: utf-8 -*-


flashcard_data = {
    "授業計画概要": "第1回:法とは何か。第2回:実定法分類(公法/私法/社会法)。第4-7回:私法(民法)の基本原理、物権、債権。第8回:中間試験。第13-15回:知的財産。",
    "法と道徳の違い": "道徳違反は非難や冷たい視線 (社会的制裁)。法違反は国家権力による制裁 (例: 刑罰、損害賠償)。法は「最小限の道徳」。 (slide 1回、p.6, p.7)",
    "「法の支配」と「法治主義」": "【法治主義】: 法律に基づき行政を行う (法律の内容は問わない)。【法の支配】: 法律内容の正義を求め、国家権力(立法・行政)も法に拘束される。目的は国民の権利保障。 (slide 2回、p.16, p.17)",
    "制定法 (実定法) の種類": "【法律】: 国会が制定。【条例】: 地方自治体(都道府県、市町村)が制定。【政令】: 政府(内閣)が法律の委任に基づき定める細則。【省令】: 省庁が法律の委任に基づき定める細則。 (slide 1回、p.8, p.10)",
    "権力分立": "国家権力を【国会 (立法)】、【内閣 (行政)】、【裁判所 (司法)】の三権に分け、相互に抑制させる仕組み。例: 裁判所は違憲立法審査権。 (slide 4回、p.2-10)",
    "判例の法源性": "最高裁判所の判例は、下級裁判所(高裁・地裁)を事実上拘束する。民事訴訟法325条3項で差戻し審は最高裁の判断に拘束されると規定。 (slide 3回、p.14, p.29)",
    "制定法の読み方": "法律の構成は「編」、「章」、「節」、「款」。条文の構成は「条」→「項」(番号なしor ②, ③...)→「号」(一, 二, 三...)。 (slide 4回、p.14-15)",
    "公法・私法・社会法": "【私法】: 市民間同士の「対等関係」 (例: 民法、商法)。【公法】: 国家と国民の「命令関係」 (例: 刑法、行政法)。【社会法】: 私法の対等関係が崩れたため国家が介入 (例: 労働法、社会保障法)。 (slide 4回、p.17-23)",
    "私法(民法)の基本原理": "①【私的自治の原則】（意思自治の原則）、②【私的所有権の保障】、③【自己責任の原則】。 (slide 1回、p.2, p.3 の授業計画より)",
    "実体法と手続法": "【実体法】: 権利や義務の内容を定める法 (例: 民法、刑法)。【手続法】: 実体法上の権利を実現する手続きを定める法 (例: 民事訴訟法、刑事訴訟法)。 (slide 6回、p.24)",
    "民事訴訟 vs 刑事訴訟": "【民事】: 当事者は原告vs被告。形式的真実主義。証明は「高度な蓋然性」。【刑事】: 当事者は検察官vs被告人。実体的真実の発見。証明は「合理的疑いなき程度」。 (slide 6回、p.14, p.15, p.20, p.21)",
    "刑事手続 (逮捕・起訴)": "警察官は逮捕後48時間以内に検察官に送検。検察官は24時間以内に勾留請求。勾留は原則10日+延長10日。検察官の裁量で起訴/不起訴を決めることを「起訴便宜主義」という。 (slide 6回、p.17, p.19)"
}

english_translations = {
    "授業計画概要": {
        "question": "Course Plan Overview",
        "answer": "1st: What is law? 2nd: Law classification (Public/Private/Social). 4-7: Private law principles, property, contracts. 8th: Midterm exam. 13-15: Intellectual property."
    },
    "法と道徳の違い": {
        "question": "Difference Between Law and Morals",
        "answer": "Breaking morals leads to social sanctions (blame, cold shoulder). Breaking the law leads to state-enforced sanctions (e.g., penalties, compensation). Law is the 'minimum standard of morals'. (Slide 1, p.6, p.7)"
    },
    "「法の支配」と「法治主義」": {
        "question": "'Rule of Law' vs 'Rechtsstaat (Rule by Law)'",
        "answer": "[Rule by Law (法治主義)]: Administration based on written law (content not questioned). [Rule of Law (法の支配)]: Demands justice in the law itself; state power (legislative/executive) is also bound by the law. Aims to protect citizens' rights. (Slide 2, p.16, p.17)"
    },
    "制定法 (実定法) の種類": {
        "question": "Types of Enacted (Positive) Law",
        "answer": "[Act/Statute]: Enacted by the Diet. [Ordinance]: Enacted by local governments (prefectures, cities). [Cabinet Order (Seirei)]: Detailed rules set by the Cabinet under the law. [Ministerial Ordinance (Shorei)]: Detailed rules set by ministries under the law. (Slide 1, p.8, p.10)"
    },
    "権力分立": {
        "question": "Separation of Powers",
        "answer": "A system dividing state power into [Diet (Legislature)], [Cabinet (Executive)], and [Courts (Judiciary)], with mutual checks and balances. E.g., Courts have judicial review. (Slide 4, p.2-10)"
    },
    "判例の法源性": {
        "question": "Precedent (as a source of law)",
        "answer": "Supreme Court precedents effectively bind lower courts (High/District Courts). Code of Civil Procedure Art. 325(3) states a court hearing a case on remand is bound by the higher court's judgment. (Slide 3, p.14, p.29)"
    },
    "制定法の読み方": {
        "question": "How to Read Enacted Laws",
        "answer": "Law structure: 'Part' (編), 'Chapter' (章), 'Section' (節), 'Subsection' (款). Article structure: 'Article' (条) → 'Paragraph' (項) (no number or ②, ③...) → 'Item' (号) (一, 二, 三...). (Slide 4, p.14-15)"
    },
    "公法・私法・社会法": {
        "question": "Public / Private / Social Law",
        "answer": "[Private Law]: Governs 'equal relationships' between citizens (e.g., Civil Code, Commercial Code). [Public Law]: Governs 'command relationships' between state and citizens (e.g., Penal Code, Administrative Law). [Social Law]: State intervenes where private law equality fails (e.g., Labor Law, Social Security Law). (Slide 4, p.17-23)"
    },
    "私法(民法)の基本原理": {
        "question": "Basic Principles of Private Law (Civil Code)",
        "answer": "1. [Principle of Private Autonomy] (Autonomy of Will). 2. [Guarantee of Private Property]. 3. [Principle of Self-Responsibility]. (from Slide 1, p.2, p.3 course plan)"
    },
    "実体法と手続法": {
        "question": "Substantive Law vs Procedural Law",
        "answer": "[Substantive Law]: Defines rights and obligations (e.g., Civil Code, Penal Code). [Procedural Law]: Defines the process for enforcing those rights (e.g., Code of Civil Procedure, Code of Criminal Procedure). (Slide 6, p.24)"
    },
    "民事訴訟 vs 刑事訴訟": {
        "question": "Civil vs Criminal Procedure",
        "answer": "[Civil]: Parties are Plaintiff vs. Defendant. Formal truth (based on party allegations). Proof: 'High probability'. [Criminal]: Parties are Prosecutor vs. Accused. Substantive truth (inquisitorial). Proof: 'Beyond a reasonable doubt'. (Slide 6, p.14, p.15, p.20, p.21)"
    },
    "刑事手続 (逮捕・起訴)": {
        "question": "Criminal Procedure (Arrest/Prosecution)",
        "answer": "Police transfer to prosecutor within 48h of arrest. Prosecutor requests detention within 24h. Detention is 10 days + 10-day extension. Prosecutor's discretion to prosecute/not is 'Discretionary Prosecution'. (Slide 6, p.17, p.19)"
    }
}

thai_translations = {
    "授業計画概要": {
        "question": "ภาพรวมแผนการสอน",
        "answer": "ครั้งที่ 1: กฎหมายคืออะไร ครั้งที่ 2: การจำแนกประเภทกฎหมาย (มหาชน/เอกชน/สังคม) ครั้งที่ 4-7: หลักกฎหมายเอกชน, ทรัพย์สิทธิ์, หนี้ ครั้งที่ 8: สอบกลางภาค ครั้งที่ 13-15: ทรัพย์สินทางปัญญา"
    },
    "法と道徳の違い": {
        "question": "ความแตกต่างของกฎหมายและศีลธรรม",
        "answer": "ฝ่าฝืนศีลธรรมจะถูกสังคมตำหนิ/มองไม่ดี ฝ่าฝืนกฎหมายจะถูกลงโทษโดยอำนาจรัฐ (เช่น ลงโทษ, ชดใช้ค่าเสียหาย) กฎหมายคือ 'ศีลธรรมขั้นต่ำสุด' (สไลด์ 1, หน้า 6, 7)"
    },
    "「法の支配」と「法治主義」": {
        "question": "'หลักนิติธรรม' (Rule of Law) vs 'หลักนิติรัฐ' (Rule by Law)",
        "answer": "[นิติรัฐ (法治主義)]: การปกครองโดยกฎหมายที่ตราขึ้น (ไม่คำนึงถึงเนื้อหา) [นิติธรรม (法の支配)]: กฎหมายต้องเป็นธรรม และอำนาจรัฐ (นิติบัญญัติ/บริหาร) ต้องอยู่ภายใต้กฎหมาย มุ่งประกันสิทธิของประชาชน (สไลด์ 2, หน้า 16, 17)"
    },
    "制定法 (実定法) の種類": {
        "question": "ประเภทของกฎหมายลายลักษณ์อักษร",
        "answer": "[พระราชบัญญัติ]: ตราโดยรัฐสภา [ข้อบัญญัติท้องถิ่น]: ตราโดยองค์กรปกครองส่วนท้องถิ่น (จังหวัด, เมือง) [กฤษฎีกาคณะรัฐมนตรี]: กฎรายละเอียดที่คณะรัฐมนตรีกำหนดโดยอาศัยอำนาจตามกฎหมาย [กฎกระทรวง]: กฎรายละเอียดที่กระทรวงกำหนดโดยอาศัยอำนาจตามกฎหมาย (สไลด์ 1, หน้า 8, 10)"
    },
    "権力分立": {
        "question": "การแบ่งแยกอำนาจ",
        "answer": "การแบ่งอำนาจรัฐเป็น [รัฐสภา (นิติบัญญัติ)], [คณะรัฐมนตรี (บริหาร)], และ [ศาล (ตุลาการ)] เพื่อตรวจสอบและถ่วงดุลซึ่งกันและกัน เช่น ศาลมีอำนาจทบทวนความชอบด้วยรัฐธรรมนูญ (สไลด์ 4, หน้า 2-10)"
    },
    "判例の法源性": {
        "question": "บรรทัดฐานคำพิพากษา (ฐานะแหล่งที่มาของกฎหมาย)",
        "answer": "คำพิพากษาของศาลฎีกาผูกพันศาลล่าง (ศาลสูง/ศาลชั้นต้น) ในทางปฏิบัติ ป.วิ.แพ่ง มาตรา 325(3) กำหนดว่าศาลที่รับคดีที่ถูกย้อนสำนวนต้องผูกพันตามคำวินิจฉัยของศาลสูง (สไลด์ 3, หน้า 14, 29)"
    },
    "制定法の読み方": {
        "question": "วิธีอ่านกฎหมายลายลักษณ์อักษร",
        "answer": "โครงสร้างกฎหมาย: 'ภาค' (編), 'ลักษณะ' (章), 'หมวด' (節), 'ส่วน' (款) โครงสร้างมาตรา: 'มาตรา' (条) → 'วรรค' (項) (ไม่มีเลข หรือ ②, ③...) → 'อนุมาตรา' (号) (一, 二, 三...) (สไลด์ 4, หน้า 14-15)"
    },
    "公法・私法・社会法": {
        "question": "กฎหมายมหาชน / เอกชน / สังคม",
        "answer": "[กฎหมายเอกชน]: ควบคุม 'ความสัมพันธ์ที่เท่าเทียม' ระหว่างเอกชน (เช่น ป.แพ่ง, ป.พาณิชย์) [กฎหมายมหาชน]: ควบคุม 'ความสัมพันธ์แบบบังคับบัญชา' ระหว่างรัฐกับเอกชน (เช่น ป.อาญา, กฎหมายปกครอง) [กฎหมายสังคม]: รัฐเข้าแทรกแซงเมื่อความเท่าเทียมทางเอกชนล้มเหลว (เช่น กฎหมายแรงงาน, กฎหมายประกันสังคม) (สไลด์ 4, หน้า 17-23)"
    },
    "私法(民法)の基本原理": {
        "question": "หลักการพื้นฐานของกฎหมายเอกชน (ป.พ.)",
        "answer": "1. [หลักความเป็นอิสระของเอกชน] (หลักเจตนาเสรี) 2. [การรับรองทรัพย์สินส่วนบุคคล] 3. [หลักความรับผิดชอบต่อตนเอง] (จากแผนการสอน สไลด์ 1, หน้า 2, 3)"
    },
    "実体法と手続法": {
        "question": "กฎหมายสารบัญญัติ vs กฎหมายวิธีสบัญญัติ",
        "answer": "[กฎหมายสารบัญญัติ]: กำหนดเนื้อหาของสิทธิและหน้าที่ (เช่น ป.แพ่ง, ป.อาญา) [กฎหมายวิธีสบัญญัติ]: กำหนดกระบวนการเพื่อบังคับใช้สิทธิ (เช่น ป.วิ.แพ่ง, ป.วิ.อาญา) (สไลด์ 6, หน้า 24)"
    },
    "民事訴訟 vs 刑事訴訟": {
        "question": "คดีแพ่ง vs คดีอาญา",
        "answer": "[คดีแพ่ง]: คู่ความคือ โจทก์ vs จำเลย ค้นหาความจริงแบบทางการ (ตามที่คู่ความกล่าวอ้าง) พิสูจน์: 'ความน่าจะเป็นสูง' [คดีอาญา]: คู่ความคือ อัยการ vs จำเลย ค้นหาความจริงแท้ (ระบบไต่สวน) พิสูจน์: 'ปราศจากข้อสงสัยอันสมควร' (สไลด์ 6, หน้า 14, 15, 20, 21)"
    },
    "刑事手続 (逮捕・起訴)": {
        "question": "กระบวนการทางอาญา (การจับกุม/ฟ้องคดี)",
        "answer": "ตำรวจส่งตัวให้อัยการภายใน 48 ชม. หลังจับกุม อัยการยื่นขอฝากขังต่อศาลภายใน 24 ชม. การฝากขังคือ 10 วัน + ต่อได้อีก 10 วัน อัยการมีดุลยพินิจในการสั่งฟ้อง/ไม่ฟ้อง เรียกว่า 'หลักดุลยพินิจในการฟ้องคดี' (สไลด์ 6, หน้า 17, 19)"
    }
}