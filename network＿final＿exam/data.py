# -*- coding: utf-8 -*-

# --- スキルチェック問題 (Skill Check Problems) ---
# Based on file: 10-スキルチェックの模範解答.pdf

q_1 = "問1: IPアドレス 192.168.10.45/24のネットワークアドレスはどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 15 )"
q_2 = "問2: IPアドレス 172.16.50.128/25のネットワークアドレスはどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 16 )"
q_3 = "問3: IPアドレス 10.20.30.64/27のネットワークアドレスはどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 17 )"
q_4 = "問4: IPアドレス 192.168.100.200/28のネットワークアドレスはどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 18 )"
q_5 = "問5: ネットワーク 192.168.1.0/24 で利用可能な最大ホスト数はいくつですか? ( `10-スキルチェックの模範解答.pdf`, p. 11 )"
q_6 = "問6: ネットワーク 172.16.0.0/26で利用可能な最大ホスト数はいくつですか? ( `10-スキルチェックの模範解答.pdf`, p. 12 )"
q_7 = "問7: ネットワーク 10.0.0.0/29 で利用可能な最大ホスト数はいくつですか? ( `10-スキルチェックの模範解答.pdf`, p. 13 )"
q_8 = "問8: ネットワーク 192.168.0.0/22 で利用可能な最大ホスト数はいくつですか? ( `10-スキルチェックの模範解答.pdf`, p. 14 )"
q_9 = "問9: サブネットマスク 255.255.255.0 をCIDR表記で表すとどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 5 )"
q_10 = "問10: サブネットマスク 255.255.255.128 をCIDR表記で表すとどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 6 )"
q_11 = "問11: サブネットマスク 255.255.252.0 をCIDR表記で表すとどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 7 )"
q_12 = "問12: IPアドレス 192.168.10.100/24 において、ホストアドレス部は何ビットですか? ( `10-スキルチェックの模範解答.pdf`, p. 8 )"
q_13 = "問13: IPアドレス 172.16.50.25/26 において、ネットワークアドレス部は何ビットですか? ( `10-スキルチェックの模範解答.pdf`, p. 9 )"
q_14 = "問14: IPアドレスが32ビットで、サブネットマスクが/28の場合、ホストアドレス部は何ビットですか? ( `10-スキルチェックの模範解答.pdf`, p. 10 )"
q_15 = "問15: 異なるネットワーク間でパケットを転送し、経路制御を行う機器はどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 19 )"
q_16 = "問16: MACアドレスを使用してデータフレームを適切なポートに転送する機器はどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 20 )"
q_17 = "問17: 物理層で動作し、信号を増幅・再生して伝送距離を延長する機器はどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 21 )"
q_18 = "問18: データリンク層で動作し、複数のネットワークセグメントを接続する機器はどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 22 )"
q_19 = "問19: IPアドレスとMACアドレスの説明として正しいものはどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 3 )"
q_20 = "問20: MACアドレスの特徴として正しいものはどれですか? ( `10-スキルチェックの模範解答.pdf`, p. 4 )"
q_21 = "問21: Packet Tracerで図のようなネットワーク（PC-ルータ-ルータ-PC）を構成しIPを設定したが通信できない。静的ルーティング未設定の場合に考えられる原因を2つ答えなさい。 ( `Sample Problem 1` )"

q_22 = "問22: 2台のルータを経由する通信でPingが通らない原因を「ルーティング」という語句を使って説明しなさい。また、その解決策を1つ挙げなさい。 ( `Sample Problem 2` )"

q_23 = "問23: ルータに以下のコマンドを設定した時の動作（パケットの通過・破棄）を説明しなさい。\n(config)# access-list 1 deny 192.168.1.1 0.0.0.0\n(config)# access-list 1 permit any\n(config-if)# ip access-group 1 in (Gi0/1に対して) ( `Sample Problem 3` )"

q_24 = "問24: 問23の設定（送信元192.168.1.1を拒否、それ以外を許可）において、送信元IPが「192.168.1.2」のパケットは通過しますか、破棄されますか？ ( `Sample Problem 4` )"

q_25 = "問25: IPアドレス 192.168.100.61/24 が属するネットワークアドレスを求めなさい。 ( `Sample Problem 5` )"

q_26 = "問26: IPアドレス 192.168.100.61/20 が属するネットワークアドレスを求めなさい。 ( `Sample Problem 5` )"

q_27 = "問27: ネットワークアドレス 10.10.10.0/24 で使用することができるホストIPアドレスの個数を求めなさい。 ( `Sample Problem 5` )"

q_28 = "問28: ネットワークアドレス 10.10.10.0/26 で使用することができるホストIPアドレスの個数を求めなさい。 ( `Sample Problem 5` )"

# --- 解答データ (日本語 - 詳細な解説付き) ---

flashcard_data = {
    q_1: """正解: 192.168.10.0
【解説】
ホストアドレス部を0にしたものをネットワークアドレスと呼びます。
CIDR表記で/24だから左から24ビットがネットワークアドレス部です。
残りの8ビットがホストアドレス部だからそれを0にします。
→ 192.168.10.0""",

    q_2: """正解: 172.16.50.128
【解説】
CIDR表記で/25だから左から25ビットがネットワークアドレス部です。
残りの7ビットがホストアドレス部だからそれを0にします。
172.16.50.128 は2進数で 10101100.00010000.00110010.10000000
右から7ビットを0にしても値は変わりません。
→ 172.16.50.128""",

    q_3: """正解: 10.20.30.64
【解説】
CIDR表記で/27だから左から27ビットがネットワークアドレス部です。
残りの5ビットがホストアドレス部だからそれを0にします。
10.20.30.64 は2進数で 00001010.00010100.00011110.01000000
右から5ビットを0にしても値は変わりません。
→ 10.20.30.64""",

    q_4: """正解: 192.168.100.192
【解説】
CIDR表記で/28だから左から28ビットがネットワークアドレス部です。
残りの4ビットがホストアドレス部だからそれを0にします。
192.168.100.200 は2進数で ...01100100.11001000
右から4ビットを0にすると ...11000000 となります。
→ 192.168.100.192""",

    q_5: """正解: 254
【解説】
CIDR表記で/24だから左から24ビットがネットワークアドレス部、残りの8ビットがホストアドレス部です。
8ビットだと256個の数値を作れますが、以下の2つは使えません。
・ホスト部がすべて0（ネットワークアドレス）
・ホスト部がすべて1（ブロードキャストアドレス）
したがって、256 - 2 = 254個となります。""",

    q_6: """正解: 62
【解説】
CIDR表記で/26だから左から26ビットがネットワークアドレス部、残りの6ビットがホストアドレス部です。
6ビットだと64個の数値を作れますが、ネットワークアドレスとブロードキャストアドレスの2つを除外します。
したがって、64 - 2 = 62個となります。""",

    q_7: """正解: 6
【解説】
CIDR表記で/29だから左から29ビットがネットワークアドレス部、残りの3ビットがホストアドレス部です。
3ビットだと8個の数値を作れますが、ネットワークアドレスとブロードキャストアドレスの2つを除外します。
したがって、8 - 2 = 6個となります。""",

    q_8: """正解: 1022
【解説】
CIDR表記で/22だから左から22ビットがネットワークアドレス部、残りの10ビットがホストアドレス部です。
10ビットだと1024個の数値を作れますが、ネットワークアドレスとブロードキャストアドレスの2つを除外します。
したがって、1024 - 2 = 1022個となります。""",

    q_9: """正解: /24
【解説】
サブネットマスクはIPアドレスのネットワーク部を1、ホスト部を0にします。
255.255.255.0は2進数で 11111111.11111111.11111111.00000000
左から24ビットがネットワーク部なので、CIDR表記は /24 です。""",

    q_10: """正解: /25
【解説】
255.255.255.128は2進数で 11111111.11111111.11111111.10000000
左から25ビットがネットワーク部なので、CIDR表記は /25 です。""",

    q_11: """正解: /22
【解説】
255.255.252.0は2進数で 11111111.11111111.11111100.00000000
左から22ビットがネットワーク部なので、CIDR表記は /22 です。""",

    q_12: """正解: 8ビット
【解説】
CIDR表記で/24だから左から24ビットがネットワークアドレス部です。
IPアドレスは合計32ビットなので、残りの 32 - 24 = 8ビット がホストアドレス部です。""",

    q_13: """正解: 26ビット
【解説】
CIDR表記で/26とあるので、左から26ビットがネットワークアドレス部であることを示しています。""",

    q_14: """正解: 4ビット
【解説】
CIDR表記で/28だから左から28ビットがネットワークアドレス部です。
IPアドレスは32ビットなので、残りの 32 - 28 = 4ビット がホストアドレス部です。""",

    q_15: """正解: ルータ
【解説】
ルータは異なるネットワーク間でパケットを転送し、最適な経路を選択する（経路制御を行う）機器です。""",

    q_16: """正解: スイッチングハブ
【解説】
スイッチングハブはMACアドレスを学習し、データフレームを宛先のポートにのみ転送する機器です。""",

    q_17: """正解: リピータ
【解説】
リピータは物理層で動作し、減衰した信号を増幅・再生して伝送距離を延長する機器です。""",

    q_18: """正解: ブリッジ
【解説】
ブリッジはデータリンク層で動作し、複数のネットワークセグメントを接続する機器です。""",

    q_19: """正解: IPアドレスは論理アドレス、MACアドレスは物理アドレスである
【解説】
IPアドレスはネットワーク上の論理的な場所を示し、MACアドレスは機器（ネットワークカード）に固有の物理的な識別番号です。""",

    q_20: """正解: 48ビット(6バイト)で、ネットワークカードに固有の識別番号である
【解説】
MACアドレスは48ビット（6バイト）で構成され、製造時に割り当てられる世界で唯一の識別番号です。""",


q_21: """正解: 1. PCのデフォルトゲートウェイ設定漏れ、2. ルータ間のルーティング情報の欠如
【解説】
1. PCが別ネットワークへ送信するには「出口」であるデフォルトゲートウェイの設定が必要です。
2. ルータは直接接続されていないネットワークへの経路を知らないため、静的ルーティング（または動的ルーティング）の設定がないとパケットを転送できません。""",

    q_22: """正解: 原因：ルータが宛先ネットワークへの「ルーティング（経路）」情報を持っていないため。 解決策：スタティックルーティングを設定する（またはダイナミックルーティングを設定する）。
【解説】
左側のルータは右側のネットワークへの行き方を知らず、右側のルータも戻り道を知りません。管理者が `ip route` コマンド等で経路を教える必要があります。""",

    q_23: """正解: Gi0/1ポートに入ってくるパケットのうち、送信元が 192.168.1.1 のものは破棄され、それ以外はすべて許可（通過）される。
【解説】
`deny 192.168.1.1` で特定のホストを拒否し、`permit any` でその他すべてを許可しています。`in` は受信パケットに対する適用を意味します。""",

    q_24: """正解: 通過する (○)
【解説】
送信元 192.168.1.2 は、拒否リスト（192.168.1.1）には一致しませんが、その後の `permit any`（すべて許可）に合致するため通過します。""",

    q_25: """正解: 192.168.100.0
【解説】
/24 は左から24ビット（第3オクテットまで）がネットワーク部です。ホスト部（第4オクテットの61）を0にします。""",

    q_26: """正解: 192.168.96.0
【解説】
/20 は第3オクテットの左4ビットまでがネットワーク部です。
100 (01100100) の下位4ビットを0にすると 01100000 (96) になります。""",

    q_27: """正解: 254個
【解説】
/24 のホスト部は 8ビットです。
計算式: 2^8 - 2 = 256 - 2 = 254個。""",

    q_28: """正解: 62個
【解説】
/26 のホスト部は 6ビットです。
計算式: 2^6 - 2 = 64 - 2 = 62個。"""
}

# --- 英語翻訳 (English Translations with Detailed Explanation) ---

english_translations = {
    q_1: {
        "question": "Q1: What is the network address for IP address 192.168.10.45/24?",
        "answer": "192.168.10.0\n[Explanation]\nThe network address is found by setting the host address part to 0.\nWith CIDR notation /24, the first 24 bits are the network part.\nThe remaining 8 bits are the host part, so we set them to 0.\n-> 192.168.10.0"
    },
    q_2: {
        "question": "Q2: What is the network address for IP address 172.16.50.128/25?",
        "answer": "172.16.50.128\n[Explanation]\nWith CIDR /25, the first 25 bits are the network part.\nThe remaining 7 bits are the host part. 128 is 10000000 in binary.\nThe last 7 bits are already 0, so the value remains 172.16.50.128."
    },
    q_3: {
        "question": "Q3: What is the network address for IP address 10.20.30.64/27?",
        "answer": "10.20.30.64\n[Explanation]\nWith CIDR /27, the first 27 bits are the network part.\nThe remaining 5 bits are the host part. 64 is 01000000 in binary.\nThe last 5 bits are already 0, so the value remains 10.20.30.64."
    },
    q_4: {
        "question": "Q4: What is the network address for IP address 192.168.100.200/28?",
        "answer": "192.168.100.192\n[Explanation]\nWith CIDR /28, the first 28 bits are the network part.\nThe remaining 4 bits are the host part. 200 is 11001000 in binary.\nSetting the last 4 bits to 0 gives 11000000, which is 192."
    },
    q_5: {
        "question": "Q5: What is the maximum number of available hosts for network 192.168.1.0/24?",
        "answer": "254\n[Explanation]\n/24 means the host part is 32 - 24 = 8 bits.\n8 bits allow for 256 numbers, but the Network Address (all 0s) and Broadcast Address (all 1s) cannot be used.\nTherefore: 256 - 2 = 254."
    },
    q_6: {
        "question": "Q6: What is the maximum number of available hosts for network 172.16.0.0/26?",
        "answer": "62\n[Explanation]\n/26 means the host part is 32 - 26 = 6 bits.\n6 bits allow for 64 numbers. Excluding the network and broadcast addresses:\n64 - 2 = 62."
    },
    q_7: {
        "question": "Q7: What is the maximum number of available hosts for network 10.0.0.0/29?",
        "answer": "6\n[Explanation]\n/29 means the host part is 32 - 29 = 3 bits.\n3 bits allow for 8 numbers. Excluding the network and broadcast addresses:\n8 - 2 = 6."
    },
    q_8: {
        "question": "Q8: What is the maximum number of available hosts for network 192.168.0.0/22?",
        "answer": "1022\n[Explanation]\n/22 means the host part is 32 - 22 = 10 bits.\n10 bits allow for 1024 numbers. Excluding the network and broadcast addresses:\n1024 - 2 = 1022."
    },
    q_9: {
        "question": "Q9: Which CIDR notation represents subnet mask 255.255.255.0?",
        "answer": "/24\n[Explanation]\n255.255.255.0 in binary is 11111111.11111111.11111111.00000000.\nThe first 24 bits are 1s, so it is /24."
    },
    q_10: {
        "question": "Q10: Which CIDR notation represents subnet mask 255.255.255.128?",
        "answer": "/25\n[Explanation]\n255.255.255.128 in binary is 11111111.11111111.11111111.10000000.\nThe first 25 bits are 1s, so it is /25."
    },
    q_11: {
        "question": "Q11: Which CIDR notation represents subnet mask 255.255.252.0?",
        "answer": "/22\n[Explanation]\n255.255.252.0 in binary ends with ...11111100.00000000.\nCounting the 1s gives 22 bits, so it is /22."
    },
    q_12: {
        "question": "Q12: In IP address 192.168.10.100/24, how many bits is the host address part?",
        "answer": "8 bits\n[Explanation]\n/24 means the network part is 24 bits.\nThe total is 32 bits, so the host part is 32 - 24 = 8 bits."
    },
    q_13: {
        "question": "Q13: In IP address 172.16.50.25/26, how many bits is the network address part?",
        "answer": "26 bits\n[Explanation]\nThe CIDR notation /26 directly indicates that the network address part is 26 bits."
    },
    q_14: {
        "question": "Q14: If an IP address is 32 bits and the subnet mask is /28, how many bits is the host address part?",
        "answer": "4 bits\n[Explanation]\n/28 means the network part is 28 bits.\nThe host part is 32 - 28 = 4 bits."
    },
    q_15: {
        "question": "Q15: Which device forwards packets between different networks and performs routing?",
        "answer": "Router\n[Explanation]\nA Router connects different networks and selects the best path (routing) to forward packets."
    },
    q_16: {
        "question": "Q16: Which device uses MAC addresses to forward data frames to the appropriate port?",
        "answer": "Switching Hub\n[Explanation]\nA Switching Hub learns MAC addresses and forwards data frames only to the destination port."
    },
    q_17: {
        "question": "Q17: Which device operates at the physical layer to amplify and regenerate signals?",
        "answer": "Repeater\n[Explanation]\nA Repeater works at the physical layer to amplify and regenerate weak signals to extend transmission distance."
    },
    q_18: {
        "question": "Q18: Which device operates at the data link layer and connects multiple network segments?",
        "answer": "Bridge\n[Explanation]\nA Bridge operates at the data link layer and connects multiple network segments."
    },
    q_19: {
        "question": "Q19: Which statement about IP addresses and MAC addresses is correct?",
        "answer": "IP address is logical, MAC address is physical\n[Explanation]\nAn IP address is a logical address (identifies location), while a MAC address is a physical address unique to the hardware."
    },
    q_20: {
        "question": "Q20: Which is a correct characteristic of a MAC address?",
        "answer": "48 bits (6 bytes), unique ID for network card\n[Explanation]\nA MAC address is 48 bits long and is a unique identification number assigned to a network card at manufacture."
    },
    q_21: {
        "question": "Q21: In a PC-Router-Router-PC network, ping fails despite IP config. Give 2 reasons assuming no static routing.",
        "answer": "1. Missing Default Gateway on PCs.\n2. Lack of routing information between routers.\n[Explanation] PCs need a gateway to exit their subnet. Routers need routing tables (static/dynamic) to find paths to remote networks."
    },
    q_22: {
        "question": "Q22: Explain the cause of ping failure across 2 routers using the term 'routing', and provide one solution.",
        "answer": "Cause: Routers lack 'routing' information to the destination.\nSolution: Configure static routing (or dynamic routing).\n[Explanation] Routers don't inherently know paths to remote networks."
    },
    q_23: {
        "question": "Q23: Explain behavior of: access-list 1 deny 192.168.1.1, permit any, applied 'in' on Gi0/1.",
        "answer": "Packets from 192.168.1.1 entering Gi0/1 are dropped; all others are permitted.\n[Explanation] The ACL filters inbound traffic based on source IP."
    },
    q_24: {
        "question": "Q24: Based on Q23 settings, is a packet from 192.168.1.2 dropped or passed?",
        "answer": "Passed (O)\n[Explanation] It does not match the deny rule but matches 'permit any'."
    },
    q_25: {
        "question": "Q25: Find the network address of 192.168.100.61/24.",
        "answer": "192.168.100.0\n[Explanation] /24 masks the last octet (host part) to 0."
    },
    q_26: {
        "question": "Q26: Find the network address of 192.168.100.61/20.",
        "answer": "192.168.96.0\n[Explanation] 100 in binary is 01100100. Masking /20 keeps top 4 bits (0110xxxx) -> 01100000 = 96."
    },
    q_27: {
        "question": "Q27: Number of usable hosts in 10.10.10.0/24?",
        "answer": "254\n[Explanation] Host bits = 8. 2^8 - 2 = 254."
    },
    q_28: {
        "question": "Q28: Number of usable hosts in 10.10.10.0/26?",
        "answer": "62\n[Explanation] Host bits = 6. 2^6 - 2 = 62."
    }
}

# --- タイ語翻訳 (Thai Translations with Detailed Explanation) ---

thai_translations = {
    q_1: {
        "question": "Q1: Network Address ของ IP address 192.168.10.45/24 คืออะไร?",
        "answer": "192.168.10.0\n[คำอธิบาย]\nNetwork Address หาได้จากการตั้งค่าส่วน Host Address ให้เป็น 0\nCIDR /24 หมายความว่า 24 บิตแรกคือส่วน Network\nส่วนที่เหลือ 8 บิตคือส่วน Host ดังนั้นเราจึงตั้งค่าเป็น 0\n-> 192.168.10.0"
    },
    q_2: {
        "question": "Q2: Network Address ของ IP address 172.16.50.128/25 คืออะไร?",
        "answer": "172.16.50.128\n[คำอธิบาย]\nCIDR /25 หมายถึง 25 บิตแรกเป็นส่วน Network\nส่วน Host คือ 7 บิตที่เหลือ 128 ในเลขฐานสองคือ 10000000\n7 บิตสุดท้ายเป็น 0 อยู่แล้ว ดังนั้นค่าจึงคงเดิมคือ 172.16.50.128"
    },
    q_3: {
        "question": "Q3: Network Address ของ IP address 10.20.30.64/27 คืออะไร?",
        "answer": "10.20.30.64\n[คำอธิบาย]\nCIDR /27 หมายถึง 27 บิตแรกเป็นส่วน Network\nส่วน Host คือ 5 บิตที่เหลือ 64 ในเลขฐานสองคือ 01000000\n5 บิตสุดท้ายเป็น 0 อยู่แล้ว ดังนั้นค่าจึงคงเดิมคือ 10.20.30.64"
    },
    q_4: {
        "question": "Q4: Network Address ของ IP address 192.168.100.200/28 คืออะไร?",
        "answer": "192.168.100.192\n[คำอธิบาย]\nCIDR /28 หมายถึง 28 บิตแรกเป็นส่วน Network\nส่วน Host คือ 4 บิตที่เหลือ 200 ในเลขฐานสองคือ 11001000\nตั้งค่า 4 บิตสุดท้ายเป็น 0 จะได้ 11000000 ซึ่งคือ 192"
    },
    q_5: {
        "question": "Q5: จำนวนโฮสต์สูงสุดที่ใช้งานได้สำหรับเครือข่าย 192.168.1.0/24 คือเท่าไร?",
        "answer": "254\n[คำอธิบาย]\n/24 หมายถึงส่วน Host มีขนาด 32 - 24 = 8 บิต\n8 บิตสร้างตัวเลขได้ 256 ค่า แต่ต้องหัก Network Address (0 ทั้งหมด) และ Broadcast Address (1 ทั้งหมด) ออก\nดังนั้น: 256 - 2 = 254"
    },
    q_6: {
        "question": "Q6: จำนวนโฮสต์สูงสุดที่ใช้งานได้สำหรับเครือข่าย 172.16.0.0/26 คือเท่าไร?",
        "answer": "62\n[คำอธิบาย]\n/26 หมายถึงส่วน Host มีขนาด 32 - 26 = 6 บิต\n6 บิตสร้างตัวเลขได้ 64 ค่า หัก 2 ค่าพิเศษออก\nดังนั้น: 64 - 2 = 62"
    },
    q_7: {
        "question": "Q7: จำนวนโฮสต์สูงสุดที่ใช้งานได้สำหรับเครือข่าย 10.0.0.0/29 คือเท่าไร?",
        "answer": "6\n[คำอธิบาย]\n/29 หมายถึงส่วน Host มีขนาด 32 - 29 = 3 บิต\n3 บิตสร้างตัวเลขได้ 8 ค่า หัก 2 ค่าพิเศษออก\nดังนั้น: 8 - 2 = 6"
    },
    q_8: {
        "question": "Q8: จำนวนโฮสต์สูงสุดที่ใช้งานได้สำหรับเครือข่าย 192.168.0.0/22 คือเท่าไร?",
        "answer": "1022\n[คำอธิบาย]\n/22 หมายถึงส่วน Host มีขนาด 32 - 22 = 10 บิต\n10 บิตสร้างตัวเลขได้ 1024 ค่า หัก 2 ค่าพิเศษออก\nดังนั้น: 1024 - 2 = 1022"
    },
    q_9: {
        "question": "Q9: Subnet mask 255.255.255.0 เขียนแบบ CIDR ได้อย่างไร?",
        "answer": "/24\n[คำอธิบาย]\n255.255.255.0 ในเลขฐานสองคือ 11111111.11111111.11111111.00000000\nมีเลข 1 จำนวน 24 ตัว ดังนั้นคือ /24"
    },
    q_10: {
        "question": "Q10: Subnet mask 255.255.255.128 เขียนแบบ CIDR ได้อย่างไร?",
        "answer": "/25\n[คำอธิบาย]\n255.255.255.128 ในเลขฐานสองมีเลข 1 เพิ่มมาอีก 1 ตัวในออคเทตสุดท้าย\nรวมเป็น 25 ตัว ดังนั้นคือ /25"
    },
    q_11: {
        "question": "Q11: Subnet mask 255.255.252.0 เขียนแบบ CIDR ได้อย่างไร?",
        "answer": "/22\n[คำอธิบาย]\n252 ในเลขฐานสองคือ 11111100\nเมื่อนับเลข 1 ทั้งหมดจะได้ 8+8+6 = 22 ตัว ดังนั้นคือ /22"
    },
    q_12: {
        "question": "Q12: ใน IP address 192.168.10.100/24 ส่วน Host Address มีกี่บิต?",
        "answer": "8 บิต\n[คำอธิบาย]\n/24 หมายถึงส่วน Network มี 24 บิต\nIP ทั้งหมดมี 32 บิต ดังนั้นส่วน Host คือ 32 - 24 = 8 บิต"
    },
    q_13: {
        "question": "Q13: ใน IP address 172.16.50.25/26 ส่วน Network Address มีกี่บิต?",
        "answer": "26 บิต\n[คำอธิบาย]\nสัญลักษณ์ CIDR /26 ระบุโดยตรงว่าส่วน Network Address มีขนาด 26 บิต"
    },
    q_14: {
        "question": "Q14: หาก IP address มี 32 บิตและ Subnet mask คือ /28 ส่วน Host Address มีกี่บิต?",
        "answer": "4 บิต\n[คำอธิบาย]\n/28 หมายถึงส่วน Network มี 28 บิต\nส่วน Host คือ 32 - 28 = 4 บิต"
    },
    q_15: {
        "question": "Q15: อุปกรณ์ใดทำหน้าที่ส่งต่อแพ็กเก็ตระหว่างเครือข่ายและควบคุมเส้นทาง?",
        "answer": "Router (เราเตอร์)\n[คำอธิบาย]\nRouter เชื่อมต่อเครือข่ายที่แตกต่างกันและเลือกเส้นทางที่ดีที่สุด (Routing) ในการส่งต่อแพ็กเก็ต"
    },
    q_16: {
        "question": "Q16: อุปกรณ์ใดใช้ MAC address เพื่อส่งต่อดาต้าเฟรมไปยังพอร์ตที่เหมาะสม?",
        "answer": "Switching Hub (สวิตชิ่งฮับ)\n[คำอธิบาย]\nSwitching Hub เรียนรู้ MAC address และส่งต่อดาต้าเฟรมไปยังพอร์ตปลายทางที่ถูกต้องเท่านั้น"
    },
    q_17: {
        "question": "Q17: อุปกรณ์ใดทำงานใน Physical Layer เพื่อขยายและสร้างสัญญาณใหม่?",
        "answer": "Repeater (รีพีตเตอร์)\n[คำอธิบาย]\nRepeater ทำงานใน Physical Layer เพื่อขยายสัญญาณที่อ่อนลงและส่งต่อไปยังระยะทางที่ไกลขึ้น"
    },
    q_18: {
        "question": "Q18: อุปกรณ์ใดทำงานใน Data Link Layer และเชื่อมต่อเซกเมนต์เครือข่าย?",
        "answer": "Bridge (บริดจ์)\n[คำอธิบาย]\nBridge ทำงานใน Data Link Layer และทำหน้าที่เชื่อมต่อเซกเมนต์ของเครือข่ายเข้าด้วยกัน"
    },
    q_19: {
        "question": "Q19: ข้อความใดถูกต้องเกี่ยวกับ IP address และ MAC address?",
        "answer": "IP address คือ Logical, MAC address คือ Physical\n[คำอธิบาย]\nIP address เป็นที่อยู่ทางตรรกะ (Logical) ที่เปลี่ยนไปตามเครือข่าย ส่วน MAC address เป็นที่อยู่ทางกายภาพ (Physical) ที่ติดมากับฮาร์ดแวร์"
    },
    q_20: {
        "question": "Q20: ลักษณะของ MAC address ที่ถูกต้องคือข้อใด?",
        "answer": "48 บิต (6 ไบต์), เป็น ID เฉพาะของ Network Card\n[คำอธิบาย]\nMAC address มีความยาว 48 บิต (6 ไบต์) และเป็นหมายเลขระบุเฉพาะตัวที่กำหนดให้กับ Network Card ตั้งแต่การผลิต"
    },
    q_21: {
        "question": "Q21: ในเครือข่าย PC-Router-Router-PC การ ping ล้มเหลวแม้ว่าจะตั้งค่า IP แล้ว จงบอกสาเหตุ 2 ประการ (สมมติว่าไม่มี static routing)",
        "answer": "1. PC ไม่ได้ตั้งค่า Default Gateway\n2. เราเตอร์ขาดข้อมูลเส้นทาง (Routing Information)\n[คำอธิบาย] PC ต้องการเกตเวย์เพื่อส่งข้อมูลออกนอกเครือข่าย เราเตอร์ต้องการตารางเส้นทางเพื่อไปยังเครือข่ายปลายทาง"
    },
    q_22: {
        "question": "Q22: อธิบายสาเหตุที่ ping ไม่ผ่านเราเตอร์ 2 ตัว โดยใช้คำว่า 'Routing' และบอกวิธีแก้ปัญหา 1 ข้อ",
        "answer": "สาเหตุ: เราเตอร์ขาดข้อมูล 'Routing' ไปยังปลายทาง\nวิธีแก้: ตั้งค่า Static Routing (หรือ Dynamic Routing)\n[คำอธิบาย] เราเตอร์ไม่รู้จักเส้นทางไปยังเครือข่ายระยะไกลโดยอัตโนมัติ"
    },
    q_23: {
        "question": "Q23: อธิบายการทำงานของคำสั่ง: deny 192.168.1.1, permit any, ใช้แบบ 'in' ที่ Gi0/1",
        "answer": "แพ็กเก็ตจาก 192.168.1.1 ที่เข้ามาทาง Gi0/1 จะถูกทิ้ง (Drop) ส่วนอื่นๆ จะได้รับอนุญาต (Permit)\n[คำอธิบาย] ACL กรองข้อมูลขาเข้าตาม IP ต้นทาง"
    },
    q_24: {
        "question": "Q24: จากการตั้งค่าใน Q23 แพ็กเก็ตจาก 192.168.1.2 จะถูกทิ้งหรือผ่าน?",
        "answer": "ผ่าน (O)\n[คำอธิบาย] ไม่ตรงกับกฎ deny แต่ตรงกับ 'permit any' จึงผ่านได้"
    },
    q_25: {
        "question": "Q25: หา Network Address ของ 192.168.100.61/24",
        "answer": "192.168.100.0\n[คำอธิบาย] /24 ปกปิดออคเทตสุดท้ายให้เป็น 0"
    },
    q_26: {
        "question": "Q26: หา Network Address ของ 192.168.100.61/20",
        "answer": "192.168.96.0\n[คำอธิบาย] 100 ในฐานสองคือ 01100100 มาสก์ /20 เก็บ 4 บิตบนไว้ (0110xxxx) -> 01100000 = 96"
    },
    q_27: {
        "question": "Q27: จำนวนโฮสต์ที่ใช้งานได้ใน 10.10.10.0/24?",
        "answer": "254\n[คำอธิบาย] บิตโฮสต์ = 8, 2^8 - 2 = 254"
    },
    q_28: {
        "question": "Q28: จำนวนโฮสต์ที่ใช้งานได้ใน 10.10.10.0/26?",
        "answer": "62\n[คำอธิบาย] บิตโฮสต์ = 6, 2^6 - 2 = 62"
    }
}