# -*- coding: utf-8 -*-

# --- 試験問題の質問文を変数として定義 ---
# (注: Pythonの文字列ではバックスラッシュ(\)をエスケープする必要があるため、\n や \r と表記します)

# --- ネットワーク構成論 - 上位プロトコル・インターネットサービス（統合版）---

q_f1_0 = """
【ネットワーク構成論II - 期末試験対策問題集 インデックス】

■ 1-23: TCP/IP基礎・トランスポート層 (基本)
   - 語句選択 (TCP/UDP, FTP, ポート番号)
   - 記述 (フロー制御 vs 輻輳制御, ハンドシェイク)

■ 24-34: インターネットサービス基盤 (7章)
   - DHCPの仕組み, DNS (再帰問い合わせ)
   - P2P vs クライアント・サーバ

■ 35-40: メールサービス詳細 (7-2)
   - SMTP, POP3, IMAP, SMTP認証

■ 41-46: Webサービス詳細 (7-3)
   - HTTPメソッド, ステータスコード, Cookie

■ 47-53: セキュリティの基礎 (8-1)
   - 情報セキュリティ3要素 (CIA), 攻撃手法 (DoS/SQLi)

■ 54-60: 暗号技術 (8-2)
   - 共通鍵 vs 公開鍵, 電子署名, PKI

■ 61-66: セキュア通信プロトコル (8-3)
   - SSL/TLS, IPsec (モードと機能)

■ 67-72: 防御技術 (8-4)
   - ファイアウォール, DMZ, IDS/IPS

■ 73-85: 【重要】演習課題・過去問重点対策
   - 過去問頻出の記述問題まとめ (計算問題含む)

■ 86-91: 【予想】2025年度期末試験 予想問題
   - 応用的な語句選択・記述問題

■ 92-98: 【直前】演習課題4 完全網羅
   - セキュリティ・暗号化の総復習

■ 99-105: OSI参照モデル 各層の役割
   - 物理層〜アプリケーション層の定義
"""

# --- 1. 語句選択問題 (TCP/UDP, FTP, DNS, DHCP) ---
q_f1_1 = "1. (1) OSI参照モデルの第4層であるトランスポート層が管理する、送受信ホスト間の仮想的な通信路を何と呼ぶか。 ( final1.pdf p.3 )"
q_f1_2 = "1. (2) TCPが提供する通信サービスの種類はコネクション型だが、UDPが提供する通信サービスの種類は何か。 ( final1.pdf p.9 )"
q_f1_3 = "1. (3) 受信側のオーバフローを防ぐため、受信可能データ量を送信側に通知するTCPの制御機能は何か。 ( final1.pdf p.18, p.22 )"
q_f1_4 = "1. (4) コネクションの解放要求に使われるTCP制御フラグはどれか。 ( final1.pdf p.21 )"
q_f1_5 = "1. (5) IPアドレスとポート番号の組み合わせでアプリケーションを識別するためのインターフェースを何と呼ぶか。 ( final1.pdf p.29 )"
q_f1_6 = "1. (6) HTTP(80)やSMTP(25)など、主要なサービスに割り当てられているポート番号の範囲（1〜1023番）を何と呼ぶか。 ( final1.pdf p.31, p.32 )"
q_f1_7 = "1. (7) FTPのデータ転送で、クライアントがサーバへコネクションを確立するモードは何か。 ( final1.pdf p.44, p.46 )"
q_f1_8 = "1. (8) FTPでクライアントがファイルを送信する際に用いるコマンドは何か。 ( final1.pdf p.47 )"

q_f1_12 = "3. (1) TCPの輻輳制御では、通信開始時やタイムアウト後に輻輳ウィンドウサイズを指数関数的に増加させる（ A ）を行う。その後、スロースタート閾値（ssthresh）を超えると、ウィンドウサイズを線形に増加させる（ B ）フェーズに移行し、ネットワークの混雑を回避しつつ帯域を有効利用しようとする。 ( final1.pdf p.35, p.36 )"
q_f1_13 = "3. (2) アプリケーションはトランスポート層のポート番号によって識別される。例えば、Webサーバ（HTTP）は通常（ C ）番、メール転送を行うSMTPは（ D ）番を使用する。0〜1023番の範囲のポート番号は（ E ）ポートと呼ばれ、IANAによって管理されている。 ( final1.pdf p.31, p.32 )"
q_f1_14 = "3. (3) ファイル転送プロトコルFTPでは、制御用とデータ転送用の2つのコネクションを使用する。データ転送用コネクションをサーバ側からクライアント側へ確立する方式を（ F ）モード、逆にクライアント側からサーバ側へ確立する方式を（ G ）モードと呼ぶ。 ( final1.pdf p.44, p.45, p.46 )"
q_f1_15 = "3. (4) UDPは（ H ）型のプロトコルであり、信頼性よりも（ I ）性を重視する用途（音声や映像のストリーム配信など）に向いている。TCPヘッダが通常20バイトであるのに対し、UDPヘッダは（ J ）バイトと軽量である。 ( final1.pdf p.9, p.23 )"

q_f1_16 = "4. (1) TCPヘッダ内の制御フラグにおいて、コネクションの強制切断（リセット）を意味するのは（ A ）、緊急に処理すべきデータが含まれていることを示すのは（ B ）である。また、確認応答番号フィールドが有効であることを示す（ C ）フラグは、コネクション確立後のすべてのセグメントでセットされる。 ( final1.pdf p.21, p.24 )"
q_f1_17 = "4. (2) TCPの順序制御において、送信されるセグメントの先頭バイトが全データ中のどの位置にあるかを示す番号を（ D ）番号と呼ぶ。一方、受信側が次に受信を期待するデータの開始位置を示す番号を（ E ）番号と呼ぶ。 ( final1.pdf p.22 )"
q_f1_18 = "4. (3) 安全な通信のために、TELNETの代わりに（ F ）が用いられることが多い。（ F ）はポート番号（ G ）番を使用し、通信路を暗号化する。また、WebブラウジングにおいてHTTPをSSL/TLSで暗号化するHTTPSは、ポート番号（ H ）番を使用する。 ( final1.pdf p.32, p.43 )"
q_f1_19 = "4. (4) 名前解決サービスである（ I ）はポート番号53番を使用し、ホスト名とIPアドレスの変換を行う。また、ネットワークに接続したホストへ動的にIPアドレスを割り当てるプロトコルを（ J ）と呼ぶ。 ( final1.pdf p.12, p.32 )"
q_f1_20 = "4. (5) ファイル転送においてセキュリティを高める手法として、SSHの仕組みを利用してファイルを転送する（ K ）や、FTPの通信そのものをSSL/TLSで暗号化する（ L ）がある。 ( final1.pdf p.49 )"


# --- 2. 記述・説明問題 (メカニズムと理由) ---

q_f1_9 = """2. (1) TCPの「フロー制御」と「輻輳制御」の違いを、それぞれが\<\<どのウィンドウサイズ\>\>を基に\<\<何を防ぐ\>\>ために行われるかという観点から簡潔に説明せよ。 ( final1.pdf p.33, p.34 )"""
q_f1_10 = """2. (2) TCPコネクション確立における「スリーウェイハンドシェイク」の目的と、その最初のステップでクライアントが送信する制御フラグについて説明せよ。 ( final1.pdf p.25, p.21 )"""
q_f1_11 = "2. (3) アプリケーション層プロトコルである TELNET と SSH の機能的な違いを、「通信路の安全性」に注目して説明せよ。 ( final1.pdf p.43 )"
q_f1_21 = """5. (1) TCPのスロースタートフェーズにおいて、輻輳ウィンドウサイズ（cwnd）はどのように増加していくか。「ACKを受信するごと」と「1ラウンドトリップタイム（RTT）ごと」の2つの観点から説明せよ。 ( final1.pdf p.35 )"""
q_f1_22 = """5. (2) FTPにおいて、制御用コネクション（ポート21）とデータ転送用コネクション（ポート20など）が分けられている理由を、それぞれの役割に触れて簡潔に説明せよ。 ( final1.pdf p.45 )"""
q_f1_23 = """5. (3) UDPデータグラムのヘッダサイズは8バイトと非常に小さい。このヘッダに含まれる4つのフィールド名をすべて答えよ。 ( final1.pdf p.24 )"""

# --- 3. 記述・説明問題 (インターネットサービス/新規追加) ---

q_f1_24 = "6. (1) DHCPクライアントがIPアドレス設定情報を受け取る際の手順は、クライアントがサーバを見つける（ A ）、サーバが割り当て情報を通知する（ B ）、クライアントがリース要求を行う（ C ）、サーバが許可を通知する（ D ）の4段階である。 ( 7-1インターネット.pdf p.21 )"

q_f1_25 = "6. (2) クライアント・サーバモデルとP2Pモデルについて、**負荷分散**と**規模拡張性**の観点から機能の違いを説明せよ。 ( 7-1インターネット.pdf p.11, p.12 )"

q_f1_26 = "6. (3) インターネットアーキテクチャの特徴として、「ネットワーク内はシンプルな通信モデル」である理由を、ネットワークが重視する機能と端末が負う役割に触れて説明せよ。 ( 7-1インターネット.pdf p.13 )"

q_f1_27 = "6. (4) OSI参照モデルの各層が持つアドレスは異なる。アプリケーション層では（ K ）、トランスポート層では（ L ）、ネットワーク層では（ M ）、データリンク層では（ N ）が使われる。 ( 7-1インターネット.pdf p.15 )"

q_f1_28 = "6. (5) ドメイン名とIPアドレスを相互変換する仕組みであるDNSについて、最上位に位置し世界全体で13個存在するサーバを何と呼ぶか。 ( 7-1インターネット.pdf p.18 )"

q_f1_29 = "6. (6) DNSによる名前解決の際、クライアントからルートDNSサーバへ問い合わせを行う前に、クライアントが自ドメインのDNSサーバ（リゾルバ）へ行う問い合わせ方式を何と呼ぶか。 ( 7-1インターネット.pdf p.19 )"

q_f1_30 = "7. (1) インターネットの起源は、1969年に米国で開発された（ A ）であるとされる。これは特定の箇所が故障しても通信を維持できる（ B ）ネットワークの研究として始まった。 ( 7-1インターネット.pdf p.7 )"

q_f1_31 = "7. (2) ドメイン名において、最も右側に位置する部分をトップレベルドメイン（TLD）と呼ぶ。このうち、`.jp` や `.uk` のように国ごとに割り当てられるものを（ C ）、`.com` や `.org` のように分野別に割り当てられるものを（ D ）と呼ぶ。 ( 7-1インターネット.pdf p.17 )"

q_f1_32 = "7. (3) DNSサーバへの問い合わせ負荷やネットワークトラフィックを軽減するため、一度問い合わせて得た名前解決の結果を一定期間保存しておく仕組みを（ E ）と呼ぶ。 ( 7-1インターネット.pdf p.18 )"

q_f1_33 = "7. (4) DHCPがクライアントに自動設定する情報はIPアドレスだけではない。ネットワークの範囲を定義する（ F ）や、他のネットワーク（インターネット等）への出口となるルータのIPアドレスである（ G ）、名前解決を行うための（ H ）のアドレスなども通知される。 ( 7-1インターネット.pdf p.20 )"

q_f1_34 = "7. (5) 特定のサーバを経由せず、接続されたコンピュータ（ピア）同士が対等に通信を行うモデルを（ I ）モデルと呼ぶ。このモデルは、サーバに負荷が集中しないため高い（ J ）性（スケーラビリティ）を持つことが特徴である。 ( 7-1インターネット.pdf p.10, p.12 )"


# --- 4. メールサービス詳細 (7-2メールサービス.pdf) ---

q_f1_35 = "8. (1) メール配送において、送信・転送には（ A ）というプロトコルが使われ、受信には（ B ）や（ C ）というプロトコルが使われる。（ A ）はポート番号（ D ）番、（ B ）は（ E ）番、（ C ）は（ F ）番を主に使用する。 ( 7-2メールサービス.pdf p.24, p.26, p.32, p.37 )"

q_f1_36 = "8. (2) 電子メールの宛先となるメールサーバをDNSで特定する際、通常のホスト名解決（Aレコード）ではなく、（ G ）レコードを参照する。この仕組みにより、ドメイン名（例: @kitakyu-u.ac.jp）と実際のメールサーバ名（例: mail.kitakyu-u.ac.jp）を紐付けることができる。 ( 7-2メールサービス.pdf p.26 )"

q_f1_37 = "8. (3) メール送信プロトコルSMTPにおける「SMTP認証（SMTP-AUTH）」の必要性について、**スパムメール対策**の観点から簡潔に説明せよ。 ( 7-2メールサービス.pdf p.29, p.30 )"

q_f1_38 = "8. (4) メール受信プロトコルである POP3 と IMAP の機能的な違いを、「メールの管理場所」と「複数端末での利用」という観点から説明せよ。 ( 7-2メールサービス.pdf p.37 )"

q_f1_39 = "8. (5) メール受信時のユーザ認証において、パスワードを平文で送るPOP認証に対し、サーバから送られる**チャレンジ文字列**とパスワードを組み合わせてハッシュ値を計算し、その結果（レスポンス）のみを送信することで安全性を高める方式を（ H ）認証と呼ぶ。 ( 7-2メールサービス.pdf p.36 )"

q_f1_40 = "8. (6) 電子メールのヘッダ情報には、送信元を表す（ I ）、宛先を表す（ J ）、件名を表す（ K ）などが含まれる。また、実際の配送経路（経由したメールサーバの情報）は（ L ）フィールドに記録されるため、これを確認することでメールの出自を追跡できる。 ( 7-2メールサービス.pdf p.41, p.42 )"


# --- 5. Webサービス詳細 (7-3Web サービス.pdf) ---

q_f1_41 = "9. (1) WWW (World Wide Web) はインターネット上のハイパーテキストシステムであり、リソースの場所を示す（ A ）、文書の記述言語である（ B ）、通信プロトコルの（ C ）の3つの要素で構成される。 ( 7-3Web サービス.pdf p.44 )"

q_f1_42 = "9. (2) Webブラウザ（クライアント）がWebサーバに対して「このページをください」と送るメッセージを（ D ）、それに対してサーバが返すメッセージを（ E ）と呼ぶ。これらは（ F ）行、ヘッダ、（ G ）の3つの部分で構成される。 ( 7-3Web サービス.pdf p.50, p.51 )"

q_f1_43 = "9. (3) HTTPリクエストの（ F ）行にはメソッドが含まれる。Webページを取得するメソッドは（ H ）、ヘッダ情報のみを取得するのは（ I ）、フォームデータなどを送信するのは（ J ）である。 ( 7-3Web サービス.pdf p.52 )"

q_f1_44 = "9. (4) HTTPレスポンスの（ F ）行にはステータスコードが含まれる。リクエスト成功を表すコードは（ K ）、ページが見つからない場合は（ L ）、アクセス権がない場合は（ M ）、サーバ内部エラーは500番台である。 ( 7-3Web サービス.pdf p.53 )"

q_f1_45 = "9. (5) ステートレスなプロトコルであるHTTPにおいて、ショッピングカートやログイン状態などの「状態」を維持するために、サーバがブラウザに保存させる小さなテキストデータを（ N ）と呼ぶ。 ( 7-3Web サービス.pdf p.55 )"

q_f1_46 = "9. (6) Webページを動的に生成する仕組みとして、サーバ側でプログラムを実行して結果を返す仕組みを（ O ）と呼ぶ。一方、JavaScriptなどを用いてクライアント（ブラウザ）側で実行されるプログラムを（ P ）アプリケーションと呼ぶことがある。 ( 7-3Web サービス.pdf p.45 )"




# --- 6. ネットワークセキュリティ詳細 (8-1ネットワークセキュリティ.pdf 再構築版) ---

# --- まとめページ (p.18) や各スライドの重要ポイントに基づく問題 ---

q_f1_47 = "10. (1) 情報セキュリティの定義として、維持すべき情報の3つの性質（CIA）を答えよ。権利を持つ人だけがアクセスできる（ A ）、内容が正確かつ完全である（ B ）、必要なときにいつでもアクセスできる（ C ）である。 ( 8-1ネットワークセキュリティ.pdf p.7, p.18 )"

q_f1_48 = "10. (2) セキュリティに対する脅威として、機密性を脅かす（ D ）、完全性を脅かす（ E ）、可用性を脅かす（ F ）などがある。 ( 8-1ネットワークセキュリティ.pdf p.8 )"

q_f1_49 = "10. (3) サービスの可用性を侵害する攻撃として、大量のパケットを送りつけてサーバをダウンさせる攻撃を（ G ）攻撃と呼ぶ。また、複数のコンピュータが協調して一斉に攻撃を行うものを（ H ）攻撃と呼ぶ。 ( 8-1ネットワークセキュリティ.pdf p.12 )"

q_f1_50 = "10. (4) Webアプリケーションの脆弱性を狙った攻撃について説明せよ。データベースへの命令文を構成する入力値に不正な値を送信し、データベースを不正に操作する攻撃を（ I ）と呼ぶ。 ( 8-1ネットワークセキュリティ.pdf p.14 )"

q_f1_51 = "10. (5) 同じくWebサイトの脆弱性を利用し、閲覧者のブラウザ上で不正なスクリプトを実行させる攻撃を（ J ）と呼ぶ。これによりCookie情報の不正取得などが可能になる。 ( 8-1ネットワークセキュリティ.pdf p.15 )"

q_f1_52 = "10. (6) 技術的な脆弱性ではなく、人間の心理的な隙や行動のミス（パスワードの管理不備など）につけ込んで情報を盗む攻撃手法を（ K ）と呼ぶ。 ( 8-1ネットワークセキュリティ.pdf p.13 )"

q_f1_53 = "10. (7) 機器の動作状況（電力変動や漏れ電波など）を物理的手段で観察し、内部情報を取得する攻撃を（ L ）攻撃、または（ M ）攻撃と呼ぶ。 ( 8-1ネットワークセキュリティ.pdf p.16 )"


# --- 7. 暗号技術詳細 (8-2 暗号.pdf 再構築版) ---

# --- 重要事項（まとめ）に基づく問題 ---

q_f1_54 = "11. (1) 暗号技術は情報セキュリティの（ A ）と（ B ）を確保するための基盤技術である。平文を暗号文に変換することを（ C ）、暗号文を元の平文に戻すことを（ D ）と呼ぶ。 ( 8-2 暗号.pdf p.22 )"

q_f1_55 = "11. (2) 現代の暗号は「アルゴリズムは公開し、（ E ）のみを秘密にする」という（ F ）の原理に基づいている。これにより、アルゴリズムの安全性が世界中で検証される。 ( 8-2 暗号.pdf p.24 )"

q_f1_56 = "11. (3) 共通鍵暗号方式は、暗号化と復号に（ G ）鍵を用いる。処理が（ H ）という長所があるが、通信相手ごとに異なる鍵が必要となるため（ I ）の問題がある。代表的なアルゴリズムは（ J ）である。 ( 8-2 暗号.pdf p.25, p.26 )"

q_f1_57 = "11. (4) 公開鍵暗号方式は、誰でも使える（ K ）鍵で暗号化し、本人しか持っていない（ L ）鍵で復号する。処理は（ M ）が、鍵の配送が容易である。代表的なアルゴリズムである（ N ）は、素因数分解の困難性を安全性の根拠としている。 ( 8-2 暗号.pdf p.26, p.27 )"

q_f1_58 = "11. (5) データの完全性を確認するために、元データから生成される固定長の値を（ O ）と呼ぶ。これを利用した（ P ）は、送信者が自分の（ Q ）鍵で暗号化（署名）し、受信者が送信者の（ R ）鍵で復号（検証）することで、本人確認と改ざん検知を行う。 ( 8-2 暗号.pdf p.29 )"

q_f1_59 = "11. (6) 公開鍵が正当な持ち主のものであることを証明するために、信頼できる第三者機関である（ S ）が発行するデータを（ T ）と呼ぶ。これを用いた社会的なセキュリティ基盤を（ U ）と呼ぶ。 ( 8-2 暗号.pdf p.30 )"

q_f1_60 = "11. (7) 実際のセキュア通信（SSL/TLSなど）では、処理速度の問題を解決するためにハイブリッド方式をとる。鍵の交換や認証には（ V ）暗号方式を用い、大量のデータの暗号化には処理が高速な（ W ）暗号方式を用いる。 ( 8-2 暗号.pdf p.31 )"

# --- 8. セキュア通信プロトコル詳細 (8-3セキュア通信プロトコル.pdf 再構築版) ---

# --- 重要事項（まとめ・機能・IPsec）に基づく問題 ---

q_f1_61 = "13. (1) セキュア通信において満たすべき性質として、盗聴を防ぐ（ A ）、なりすましを防ぐ（ B ）、改ざんを防ぐ（ C ）、そして事実を否定できないことを証明する（ D ）などがある。 ( 8-3セキュア通信プロトコル.pdf p.36, p.42 )"

q_f1_62 = "13. (2) トランスポート層（第4層）で動作するセキュア通信プロトコルを（ E ）と呼ぶ。これをWebブラウザの通信（HTTP）に適用したものが（ F ）であり、ポート番号（ G ）番を使用する。 ( 8-3セキュア通信プロトコル.pdf p.37 )"

q_f1_63 = "13. (3) SSL/TLSでは、通信性能を確保するためにハイブリッドな仕組みをとる。セッション鍵（共通鍵）の交換には（ H ）暗号などを利用し、実際のデータ通信の暗号化には処理が高速な（ I ）暗号を利用する。また、改ざん検知には（ J ）が用いられる。 ( 8-3セキュア通信プロトコル.pdf p.38 )"

q_f1_64 = "13. (4) インターネット層（第3層）で動作するセキュア通信プロトコルを（ K ）と呼ぶ。ネットワーク間接続である（ L ）の構築によく利用される。 ( 8-3セキュア通信プロトコル.pdf p.40, p.42 )"

q_f1_65 = "13. (5) IPsecの動作モードにおいて、データ部（ペイロード）のみを暗号化しホスト間通信で使うモードを（ M ）モード、IPパケット全体を暗号化・カプセル化しゲートウェイ間通信で使うモードを（ N ）モードと呼ぶ。 ( 8-3セキュア通信プロトコル.pdf p.40 )"

q_f1_66 = "13. (6) IPsecを構成するプロトコルのうち、認証と改ざん防止のみを提供するものを（ O ）、それに加えてデータの暗号化機能も提供するものを（ P ）と呼ぶ。 ( 8-3セキュア通信プロトコル.pdf p.40 )"



# --- 9. 防御技術詳細 (8-4防御技術.pdf) ---

# --- まとめページ (p.50) および重要語句に基づく問題 ---

q_f1_67 = "14. (1) 外部からの不正なパケットの侵入を防ぐ装置を（ A ）と呼ぶ。パケットフィルタリングには、特定のIPアドレスやポート番号で遮断する（ B ）フィルタリングや、内部から発信した通信の応答のみを許可する（ C ）フィルタリングなどがある。 ( 8-4防御技術.pdf p.45 )"

q_f1_68 = "14. (2) Webサーバやメールサーバなど、外部に公開する必要があるサーバを設置するための、インターネットと内部ネットワークの中間に位置する領域を（ D ）と呼ぶ。 ( 8-4防御技術.pdf p.46 )"

q_f1_69 = "14. (3) パケットの内容やログを分析し、DoS攻撃やポートスキャンなどの攻撃の兆候を検知して通報するシステムを（ E ）、検知だけでなく遮断などの防御措置まで行うシステムを（ F ）と呼ぶ。 ( 8-4防御技術.pdf p.47 )"

q_f1_70 = "14. (4) 内部クライアントの代理としてインターネットへアクセスする中継サーバを（ G ）と呼ぶ。アドレス変換による隠蔽や有害情報のフィルタリングで安全性を高めるほか、一度アクセスした情報を保存する（ H ）機能により通信効率を向上させる。 ( 8-4防御技術.pdf p.48 )"

q_f1_71 = "14. (5) 社内に持ち込まれたPCを内部LANに接続する前に、検査専用のネットワークに接続してセキュリティ状態（ウイルス対策など）を確認する仕組みを（ I ）と呼ぶ。 ( 8-4防御技術.pdf p.49 )"

q_f1_72 = "14. (6) インシデント発生時に、法的な原因究明に必要なデータ（ログや通信パケットなど）を収集し、分析・保全する技術や仕組みを（ J ）と呼ぶ。 ( 8-4防御技術.pdf p.49 )"



# --- 10. 演習課題・過去問重点対策 (Flashcard 1-13) ---

# Flashcard 1: P2P vs Client-Server (Kadai 3)
q_f1_73 = "15. (1) 【演習/過去問】クライアント・サーバモデルとP2Pモデルの特徴を、以下の観点から比較し、記号または語句で答えよ。\n・サービス形態: (a) 中央集中型 / (b) 自律分散型\n・耐故障性: (c) 高い / (d) 低い\n・規模拡張性: (e) 高い / (f) 低い"

# Flashcard 2: DNS Definition (Kadai 3, Exam 2025)
q_f1_74 = "15. (2) 【演習/2025問1】DNSの主な役割は、( a ) を ( b ) に変換することであり、これを ( c ) という。"

# Flashcard 3: DHCP Definition (Kadai 3, Exam 2023, 2024)
q_f1_75 = "15. (3) 【演習/2023-24問1】IPアドレスが設定されていないクライアントがネットワークに接続したとき、( a ) 機能を利用して通信に必要な設定を自動的に行うためのプロトコルを ( b ) という。"

# Flashcard 4: Mail Delivery Protocols (Kadai 3, All Exam\s)
q_f1_76 = "15. (4) 【全過去問頻出】メール配送の各矢印で使用されるプロトコルを答えよ。\n①メールクライアント → 送信サーバ\n②メールサーバ → メールサーバ (転送)\n③受信サーバ → メールクライアント\n④Webブラウザ ⇔ Webメールサーバ"

# Flashcard 5: POP3 vs IMAP (ユーザー提供の完璧な回答)
q_f1_77 = "15. (5) 【全過去問頻出】メール受信プロトコルであるPOP3とIMAPについて、それぞれの機能の違いを説明せよ。"

# Flashcard 6: TCP Basic Features (All Exams)
q_f1_78 = "15. (6) 【全過去問頻出】TCPは ( a ) 型プロトコルである。受信側では送達確認のために ( b ) 番号を付与してACKを返す。また、順序制御には ( c ) 番号を使用する。"

# Flashcard 7: Flow vs Congestion Control (ユーザー提供の完璧な回答)
q_f1_79 = "15. (7) 【全過去問頻出】TCPの「フロー制御」と「輻輳制御」について、目的や制御方法の違いがわかるように説明せよ。"

# Flashcard 8: Congestion Window Algorithm (ユーザー提供の完璧な回答)
q_f1_80 = "15. (8) 【全過去問頻出】TCPにおける輻輳ウィンドウの制御方法（スロースタートフェーズ、輻輳回避フェーズ）を具体的に説明せよ。"


# Flashcard 9: TCP Bitrate Calculation (All Exams)
q_f1_81 = """15. (9) 【全過去問頻出:計算】RTT=10ms、セグメントサイズ=1000Byte (8000bit)、広告ウィンドウ=15セグメントとする。\n(a) 輻輳ウィンドウ=5 の時の送信ビットレート(bps)\n(b) 輻輳ウィンドウ=25 の時の送信ビットレート(bps)\nを求めよ。"""

# Flashcard 10: Security CIA (All Exams)
q_f1_82 = "15. (10) 【全過去問頻出】情報セキュリティの3要素（CIA）である「機密性」「完全性」「可用性」の定義を、それぞれ簡潔に記述せよ。"

# Flashcard 11: SSL/TLS vs IPsec (All Exams)
q_f1_83 = "15. (11) 【全過去問頻出】\n(1) SSL/TLSは ( a ) 層のプロトコルであり、暗号化により盗聴を、メッセージ認証により ( b ) を防ぐ。\n(2) IPsecは ( c ) 層のプロトコルであり、トランスポートモードでは ( d ) を、トンネルモードでは ( e ) を暗号化する。"

# Flashcard 12: SSL/TLS Handshake (All Exams)
q_f1_84 = "15. (12) 【全過去問頻出】SSL/TLSの手順における空欄を埋めよ。\nii. クライアントはサーバ証明書を ( a ) を用いて検証する。\niii. セッション鍵用データを ( b ) を用いて暗号化して送る。\niv. サーバは ( c ) を用いて復号する。"

# Flashcard 13: Defense Terminology (Exams)
q_f1_85 = "15. (13) 【過去問】以下のネットワーク防御用語を説明せよ。\n・DMZ\n・IDS と IPS の違い\n・パケットフィルタリング（静的・動的・ステートフル）"


# --- 11. 2025年度期末試験 予想問題 (Flashcard 16-) ---

# 予想問題 A: WebサービスとHTTP (7-3Web サービス.pdf)
q_f1_86 = "16. (1) 【予想:語句選択】WWWの通信プロトコルには ( a ) が用いられる。( a ) はステートレスであるため、状態維持には ( b ) が利用される。また、クライアントがデータを送信するメソッドには ( c ) などがある。"

# 予想問題 B: 暗号技術の基礎 (8-2 暗号.pdf)
q_f1_87 = "16. (2) 【予想:語句選択】暗号化と復号に同じ鍵を用いる方式を ( a ) 方式と呼ぶ。処理が ( b ) という利点があるが、( c ) の問題がある。対となる2つの鍵を用いる方式を ( d ) 方式と呼び、代表例に ( e ) がある。"

# 予想問題 C: 攻撃手法の分類 (8-1ネットワークセキュリティ.pdf)
q_f1_88 = "16. (3) 【予想:語句選択】DBへの命令文に不正な入力値を混入させる攻撃を ( a )、悪意あるスクリプトをWebページに埋め込む攻撃を ( b )、大量パケットでサービスを妨害する攻撃を ( c ) と呼ぶ。"

# 予想問題 D: ファイアウォールのフィルタリング機能 (8-4防御技術.pdf)
q_f1_89 = "16. (4) 【予想:記述】ファイアウォールの「静的フィルタリング」「動的フィルタリング」「ステートフルインスペクション」の機能の違いを説明せよ。"

# 予想問題 E: 電子署名の仕組み (8-2 暗号.pdf)
q_f1_90 = "16. (5) 【予想:記述】電子署名において、「誰が」「どの鍵」を使って暗号化・復号を行うか。また、それによって何（2つの性質）が確認できるか説明せよ。"

# 予想問題 F: IDSとIPSの違い (8-4防御技術.pdf)
q_f1_91 = "16. (6) 【予想:記述】IDS（侵入検知システム）と IPS（侵入防止システム）の役割の違いを簡潔に説明せよ。"

# --- 12. 演習課題4 (期末直前対策) ---

# 問1: 情報セキュリティと暗号の基礎
q_f1_92 = "17. (1) 【演習4-1】情報セキュリティの3要素とは、権利をもつ人だけが情報にアクセスできる ( a )、情報の内容や処理が正確かつ完全である ( b )、必要なときに情報にアクセスできる ( c ) である。 ( 演習課題4-解答.pdf p.1 )"

q_f1_93 = "17. (2) 【演習4-1】数学的に安全な暗号を使用したとしても、( d ) により鍵が盗まれる場合がある。 ( 演習課題4-解答.pdf p.1 )"

q_f1_94 = "17. (3) 【演習4-1】共通鍵方式を用いて電文を暗号化して送る場合、暗号鍵と復号鍵には ( e ) を用いるため、利用者間で事前に ( f ) しておく必要がある。 ( 演習課題4-解答.pdf p.1 )"

# 問2: 公開鍵方式の使い分け
q_f1_95 = "17. (4) 【演習4-2】公開鍵方式において、電文を「暗号化」して送る場合（機密性）、暗号鍵には ( a ) を用い、復号鍵には ( b ) を用いる。 ( 演習課題4-解答.pdf p.1 )"

q_f1_96 = "17. (5) 【演習4-2】公開鍵方式において、「電子署名」を行う場合（認証・改ざん検知）、電文のハッシュ値を ( c ) を用いて暗号化して添付する。受信者は ( d ) を用いて復号し、検証する。 ( 演習課題4-解答.pdf p.1 )"

# 問3: SSL/TLSの手順
q_f1_97 = "17. (6) 【演習4-3】SSL/TLSの手順の空欄を埋めよ。\n(1) サーバは ( a ) とサーバ証明書をクライアントへ送る。\n(2) クライアントはサーバ証明書を ( b ) を用いて検証する。\n(3) クライアントはセッション鍵用データを ( c ) を用いて暗号化して送る。\n(4) サーバは ( d ) を用いて復号する。 ( 演習課題4-解答.pdf p.2 )"

# 問4: IDS/IPSの機能
q_f1_98 = "17. (7) 【演習4-4】IDS（侵入検知システム）とIPS（侵入防止システム）について、それぞれの機能を説明せよ。 ( 演習課題4-解答.pdf p.2 )",


# --- 13. OSI参照モデル 各層の役割 (Roles of OSI Layers) ---
# [cite_start]Based on final1.pdf Page 3 [cite: 253]

# 物理層 (Physical Layer)
q_f1_99 = "18. (1) 【物理層】物理層の役割を述べよ。 ( final1.pdf p.3 )"

# データリンク層 (Data Link Layer)
q_f1_100 = "18. (2) 【データリンク層】データリンク層の役割を述べよ。 ( final1.pdf p.3 )"

# ネットワーク層 (Network Layer)
q_f1_101 = "18. (3) 【ネットワーク層】ネットワーク層の役割を述べよ。 ( final1.pdf p.3 )"

# トランスポート層 (Transport Layer)
q_f1_102 = "18. (4) 【トランスポート層】トランスポート層の役割を述べよ。 ( final1.pdf p.3 )"

# セッション層 (Session Layer)
q_f1_103 = "18. (5) 【セッション層】セッション層の役割を述べよ。 ( final1.pdf p.3 )"

# プレゼンテーション層 (Presentation Layer)
q_f1_104 = "18. (6) 【プレゼンテーション層】プレゼンテーション層の役割を述べよ。 ( final1.pdf p.3 )"

# アプリケーション層 (Application Layer)
q_f1_105 = "18. (7) 【アプリケーション層】アプリケーション層の役割を述べよ。 ( final1.pdf p.3 )"



flashcard_data = {
    q_f1_0: "Final Exam Flashcards - Network Architecture 2",
    # 1. 語句選択問題 (基本)
    q_f1_1: "論理的なコネクション", q_f1_2: "コネクションレス型", q_f1_3: "フロー制御", q_f1_4: "FIN", q_f1_5: "ソケット",
    q_f1_6: "Well-known ポート", q_f1_7: "パッシブモード", q_f1_8: "STOR",
    # 2. 説明問題 (基本)
    q_f1_9: "フロー制御は、**広告ウィンドウサイズ**（受信ホストが通知）を基に、**受信側のオーバフローを防ぐ**。輻輳制御は、**輻輳ウィンドウサイズ**（送信ホストが管理）を基に、**ネットワーク内の輻輳を軽減する**。",
    q_f1_10: "目的：データ転送に先立ち、送受信ホスト間で通信が可能であることを相互に確認し、コネクションを確立すること。利用フラグ：最初のステップでクライアントは**SYN**（コネクション確立要求）フラグを送信する。",
    q_f1_11: "TELNETは**通信路が暗号化されない**ため盗聴のリスクがあるが、SSH (Secure Shell) は**SSL/TLSによる通信路の暗号化**を行い安全性が高い。",
    # 3. 穴埋め問題 (応用)
    q_f1_12: "(A) スロースタート\n(B) 輻輳回避",
    q_f1_13: "(C) 80\n(D) 25\n(E) Well-known (ウェルノウン)",
    q_f1_14: "(F) アクティブ\n(G) パッシブ",
    q_f1_15: "(H) コネクションレス\n(I) リアルタイム\n(J) 8",
    q_f1_16: "(A) RST\n(B) URG\n(C) ACK",
    q_f1_17: "(D) シーケンス\n(E) 確認応答 (または ACK)",
    q_f1_18: "(F) SSH\n(G) 22\n(H) 443",
    q_f1_19: "(I) DNS\n(J) DHCP",
    q_f1_20: "(K) SFTP (または SCP)\n(L) FTPS",
    # 4. 記述・説明問題 (応用)
    q_f1_21: "ACKを受信するごとに1セグメント分増加し、結果として1ラウンドトリップタイム（RTT）ごとに2倍に増加する（指数的増加）。",
    q_f1_22: "制御用コネクションはコマンドや応答コードの送受信（制御情報のやり取り）に専念し、データ転送用コネクションは実際のファイルデータの送受信を行うため。",
    q_f1_23: "送信元ポート番号、宛先ポート番号、長さ、チェックサム",
    # 5. 新規追加 (7章)
    q_f1_24: "(A) DHCP DISCOVER\n(B) DHCP OFFER\n(C) DHCP REQUEST\n(D) DHCP ACK",
    q_f1_25: "クライアント・サーバモデルは、サーバに負荷が集中し規模拡張性も低い。P2Pモデルは、ピアによる負荷分散と、高い耐故障性および高い規模拡張性を持つ。",
    q_f1_26: "ネットワークは**接続性**（データを相手に届けること）を重視し、**信頼性やセキュリティ**など複雑な処理は**端末（通信ホスト）**に任せるという設計思想に基づいている。",
    q_f1_27: "(K) ドメイン名\n(L) ポート番号\n(M) IPアドレス\n(N) MACアドレス",
    q_f1_28: "ルートDNSサーバ",
    q_f1_29: "再帰問い合わせ",
    q_f1_30: "(A) ARPANET\n(B) 分散型",
    q_f1_31: "(C) ccTLD (country code TLD)\n(D) gTLD (generic TLD)",
    q_f1_32: "(E) キャッシュ (Caching)",
    q_f1_33: "(F) サブネットマスク\n(G) デフォルトゲートウェイ\n(H) DNSサーバ",
    q_f1_34: "(I) P2P (Peer-to-Peer)\n(J) 規模拡張 (または 耐故障)",

    q_f1_35: "(A) SMTP\n(B) POP3\n(C) IMAP\n(D) 25\n(E) 110\n(F) 143",
    q_f1_36: "(G) MX (Mail eXchange)",
    q_f1_37: "従来のSMTPにはユーザ認証機能がなく、誰でも自由にメールを送信できたため、第三者による不正中継（スパムメールの踏み台）を防ぐために、メール送信時にユーザ認証を行う仕組みが必要となった。",
    q_f1_38: "POP3はメールをサーバからクライアントへダウンロードして管理するため、複数端末での同期が難しい。一方、IMAPはメールをサーバ上で管理し、クライアントはキャッシュのみを持つため、複数端末から同じメールボックスを操作・閲覧できる。",
    q_f1_39: "(H) APOP",
    q_f1_40: "(I) From\n(J) To\n(K) Subject\n(L) Received",

    q_f1_41: "(A) URL (または URI)\n(B) HTML\n(C) HTTP",
    q_f1_42: "(D) リクエスト (HTTPリクエスト)\n(E) レスポンス (HTTPレスポンス)\n(F) ステータス (または リクエスト/レスポンス)\n(G) メッセージボディ",
    q_f1_43: "(H) GET\n(I) HEAD\n(J) POST",
    q_f1_44: "(K) 200 (OK)\n(L) 404 (Not Found)\n(M) 403 (Forbidden)",
    q_f1_45: "(N) Cookie (クッキー)",
    q_f1_46: "(O) CGI (Common Gateway Interface)\n(P) Helper (または クライアントサイド)",
    q_f1_47: "(A) 機密性 (Confidentiality)\n(B) 完全性 (Integrity)\n(C) 可用性 (Availability)",
    q_f1_48: "(D) 盗聴 (または 不正アクセス)\n(E) 改ざん\n(F) サービス不能攻撃 (DoS攻撃)",
    q_f1_49: "(G) DoS (Denial of Service)\n(H) DDoS (Distributed DoS)",
    q_f1_50: "(I) SQLインジェクション",
    q_f1_51: "(J) クロスサイトスクリプティング (XSS)",
    q_f1_52: "(K) ソーシャルエンジニアリング",
    q_f1_53: "(L) サイドチャネル (Side Channel)\n(M) 実装 (Implementation)",
    q_f1_54: "(A) 機密性\n(B) 完全性\n(C) 暗号化\n(D) 復号",
    q_f1_55: "(E) 鍵\n(F) ケルクホフス (Kerckhoffs)",
    q_f1_56: "(G) 同じ (共通の)\n(H) 高速\n(I) 鍵配送 (または 鍵管理)\n(J) AES",
    q_f1_57: "(K) 公開\n(L) 秘密\n(M) 遅い\n(N) RSA",
    q_f1_58: "(O) ハッシュ値\n(P) 電子署名 (デジタル署名)\n(Q) 秘密\n(R) 公開",
    q_f1_59: "(S) 認証局 (CA)\n(T) 電子証明書\n(U) PKI (公開鍵暗号基盤)",
    q_f1_60: "(V) 公開鍵\n(W) 共通鍵",

    q_f1_61: "(A) 機密性\n(B) 認証\n(C) メッセージ完全性\n(D) 否認不可能性",
    q_f1_62: "(E) SSL/TLS\n(F) HTTPS\n(G) 443",
    q_f1_63: "(H) 公開鍵\n(I) 共通鍵\n(J) メッセージ認証コード (MAC)",
    q_f1_64: "(K) IPsec\n(L) VPN (Virtual Private Network)",
    q_f1_65: "(M) トランスポート\n(N) トンネル",
    q_f1_66: "(O) AH (Authentication Header)\n(P) ESP (Encapsulated Security Payload)",

    q_f1_67: "(A) ファイアウォール (Firewall)\n(B) 静的 (Static)\n(C) 動的 (Dynamic)",
    q_f1_68: "(D) DMZ (非武装地帯)",
    q_f1_69: "(E) IDS (侵入検知システム)\n(F) IPS (侵入防止システム)",
    q_f1_70: "(G) プロキシ (Proxy)\n(H) キャッシュ (Cache)",
    q_f1_71: "(I) 検疫ネットワーク",
    q_f1_72: "(J) ディジタルフォレンジクス (Digital Forensics)",


    q_f1_73: "クライアント・サーバ: (a) 中央集中型, (d) 低い, (f) 低い\nP2P: (b) 自律分散型, (c) 高い, (e) 高い",
    q_f1_74: "(a) ドメイン名\n(b) IPアドレス\n(c) 名前解決",
    q_f1_75: "(a) ブロードキャスト\n(b) DHCP",
    q_f1_76: "① SMTP\n② SMTP\n③ POP3 または IMAP\n④ HTTP",
    q_f1_77: "POP3はメールをダウンロードして処理することを前提としたシンプルなプロトコルである。\nIMAPはメールをサーバで管理することを前提としており、複数クライアントからのアクセスなどを可能にした高機能なプロトコルである。",
    q_f1_78: "(a) コネクション\n(b) 確認応答 (ACK)\n(c) シーケンス",
    #q_f1_79: "フロー制御: 受信側のバッファ溢れを防ぐ。受信側が通知する「広告ウィンドウ」を使用。\n輻輳制御: ネットワークの混雑を防ぐ。送信側が計算する「輻輳ウィンドウ」を使用。",
    #q_f1_80: "(a) スロースタート\n(b) 輻輳回避",
    q_f1_79: "フロー制御では受信ホストの処理能力を超えないように、受信ホストから通知される受信可能バッファサイズに応じて、送信レートを調整する。\n一方、輻輳制御ではネットワークの処理能力を超えないように、ネットワークの輻輳状態に応じて、送信レートを調整する。",
    
    q_f1_80: "スロースタートフェーズでは指数的に増加（送信レートを速やかに増加）させ、スロースタートフェーズの閾値を超えた後に、輻輳回避フェーズに移り、線形的に増加（送信レートを緩やかに増加）させながら適切な輻輳ウィンドウを探る。",
    q_f1_81: """(a) 4 Mbps (b) 12 Mbps【解説】
       ■ 計算式 (Formula)
       実際のウィンドウサイズ = min(広告ウィンドウ, 輻輳ウィンドウ)
       送信レート(bps) = (実際のウィンドウ × セグメントサイズ × 8) ÷ RTT

        ■ 変数 (Variables)
        ・RTT = 10ms = 0.01秒
        ・セグメントサイズ = 1000 Byte = 8000 bit (×8bit変換)
        ・広告ウィンドウ (受信側限界) = 15

        --------------------------------
        (a) 輻輳ウィンドウが 5 の場合
        1. ウィンドウ決定: min(15, 5) = 5 セグメント
        2. データ量: 5 × 8000 bit = 40,000 bit
        3. レート計算: 40,000 ÷ 0.01 = 4,000,000 bps
        → 答え: 4 Mbps

        (b) 輻輳ウィンドウが 25 の場合
        1. ウィンドウ決定: min(15, 25) = 15 セグメント
        ※受信側の限界(広告ウィンドウ)で頭打ちになります
        2. データ量: 15 × 8000 bit = 120,000 bit
        3. レート計算: 120,000 ÷ 0.01 = 12,000,000 bps
        → 答え: 12 Mbps""",

    q_f1_82: "機密性: 許可された人だけがアクセスできること。\n完全性: 情報が正確で改ざんされていないこと。\n可用性: 必要な時にいつでも使えること。",
    q_f1_83: "(1) (a) トランスポート, (b) 改ざん (および なりすまし)\n(2) (c) インターネット, (d) データ部 (ペイロード), (e) IPパケット全体 (ヘッダ含む)",
    q_f1_84: "(a) 認証局の公開鍵\n(b) サーバの公開鍵\n(c) サーバの秘密鍵",
    q_f1_85: "DMZ: 公開サーバ（Web/Mail等）を配置する、外部と内部の中間領域。\nIDS/IPS: IDSは検知・通報、IPSは検知・防御（遮断）を行う。\nフィルタリング: 静的(固定ルール)、動的(戻りパケット許可)、ステートフル(手順・状態も確認)。",

    q_f1_86: "(a) HTTP\n(b) Cookie (クッキー)\n(c) POST",
    q_f1_87: "(a) 共通鍵暗号\n(b) 高速\n(c) 鍵配送 (または鍵管理)\n(d) 公開鍵暗号\n(e) RSA",
    q_f1_88: "(a) SQLインジェクション\n(b) クロスサイトスクリプティング (XSS)\n(c) DoS攻撃",
    q_f1_89: "静的: IPやポート番号の固定ルールで判断。\n動的: 内部からの通信に対する応答のみ許可。\nステートフル: プロトコルの手順や通信状態（コンテキスト）まで監視して判断。",
    q_f1_90: "暗号化: 送信者が「送信者の秘密鍵」で行う。\n復号: 受信者が「送信者の公開鍵」で行う。\n確認事項: 送信者が本人であること（認証）、データが改ざんされていないこと（完全性）。",
    q_f1_91: "IDS: 攻撃の兆候を「検知」して「通報」する（遮断はしないことが多い）。\nIPS: 検知に加えて、通信を「遮断」するなどして「防御」する。",
    q_f1_92: "(a) 機密性\n(b) 完全性\n(c) 可用性",
    q_f1_93: "(d) 実装攻撃 (または サイドチャネル攻撃)",
    q_f1_94: "(e) 共通鍵\n(f) 共有 (または 配布)",
    q_f1_95: "(a) 受信者の公開鍵\n(b) 受信者の秘密鍵",
    q_f1_96: "(c) 送信者の秘密鍵\n(d) 送信者の公開鍵",
    q_f1_97: "(a) サーバの公開鍵\n(b) 認証局の公開鍵\n(c) サーバの公開鍵\n(d) サーバの秘密鍵",
    q_f1_98: "IDS: パケットの内容やログを分析し、攻撃の兆候を検知・通報する。\nIPS: IDSの機能に加えて遮断などの処置もできる。",
    q_f1_99: "電気信号レベルやコネクタ形状などのハードウェア機能。",
    q_f1_100: "伝送メディアを介した通信ノード間でデータを正しく伝送するための制御機能。",
    q_f1_101: "複数の中継ノードを介した経路選択(ルーティング)やデータの中継・転送機能。",
    q_f1_102: "送受信ホスト間の論理的なコネクションの管理,通信品質や信頼性の保証機能。",
    q_f1_103: "アプリケーション間の通信開始・維持・終了などデータ伝送の同期制御機能。",
    q_f1_104: "データの表現形式(符号化,暗号化など)に関する制御機能。",
    q_f1_105: "具体的なサービス(電子メールなど)に応じた各種通信機能。"

    



 
    


    


    


    
    

}

# --- 英語翻訳 ---

english_translations = {
    q_f1_0: "Final Exam Flashcards - Network Architecture 2",
    # 1. 語句選択問題 (基本)
    q_f1_1: {"question": "1. (1) What is the term for the virtual communication path managed by the Transport Layer (OSI Layer 4)? ( final1.pdf p.3 )", "answer": "Logical Connection"},
    q_f1_2: {"question": "1. (2) TCP provides a connection-oriented service. What type of communication service does UDP provide? ( final1.pdf p.9 )", "answer": "Connectionless Service"},
    q_f1_3: {"question": "1. (3) What TCP control function prevents receiver overflow by notifying the sender of the maximum receivable data amount? ( final1.pdf p.18, p.22 )", "answer": "Flow Control"},
    q_f1_4: {"question": "1. (4) Which TCP control flag is used for a connection release request? ( final1.pdf p.21 )", "answer": "FIN"},
    q_f1_5: {"question": "1. (5) What is the interface, identified by the combination of an IP address and a port number, used to identify an application? ( final1.pdf p.29 )", "answer": "Socket"},
    q_f1_6: {"question": "1. (6) What are the port numbers (range 1 to 1023) called that are assigned to major services like HTTP (80) and SMTP (25)? ( final1.pdf p.31, p.32 )", "answer": "Well-known Port"},
    q_f1_7: {"question": "1. (7) What FTP data transfer mode involves the client establishing the connection to the server? ( final1.pdf p.44, p.46 )", "answer": "Passive Mode"},
    q_f1_8: {"question": "1. (8) What command does the client use in FTP to send (upload) a file? ( final1.pdf p.47 )", "answer": "STOR"},
    
    # 2. 説明問題 (基本)
    q_f1_9: {"question": "2. (1) Briefly explain the difference between **TCP Flow Control** and **Congestion Control**, focusing on which window size is used as the basis and **what** each aims to prevent. ( final1.pdf p.33, p.34 )", "answer": "Flow Control uses the **Advertised Window Size** (receiver notified) to prevent **receiver overflow**. Congestion Control uses the **Congestion Window Size** (sender managed) to prevent **network congestion**."},
    q_f1_10: {"question": "2. (2) Explain the purpose of the **TCP 3-Way Handshake** and the control flag sent by the client in the first step. ( final1.pdf p.25, p.21 )", "answer": "Purpose: To **mutually confirm** communication capability and **establish the connection** before data transfer. Flag: The client sends the **SYN** (synchronize) flag in the first step."},
    q_f1_11: {"question": "2. (3) Explain the functional difference between the application layer protocols **TELNET** and **SSH**, focusing on **communication path security**. ( final1.pdf p.43 )", "answer": "TELNET is a virtual terminal protocol where the **communication path is not encrypted**, posing a risk of eavesdropping. SSH (Secure Shell) uses **SSL/TLS encryption** for the communication path, ensuring high security."},
    # 3. 穴埋め問題 (応用)
    q_f1_12: {"question": "3. (1) In TCP congestion control, the ( A ) phase exponentially increases the congestion window size at the start of communication or after a timeout. Once the slow start threshold (ssthresh) is exceeded, it transitions to the ( B ) phase, where the window size increases linearly to utilize bandwidth effectively while avoiding congestion. ( final1.pdf p.35, p.36 )", "answer": "(A) Slow Start\n(B) Congestion Avoidance"},
    q_f1_13: {"question": "3. (2) Applications are identified by transport layer port numbers. For example, Web servers (HTTP) typically use port ( C ), and SMTP for mail transfer uses port ( D ). Port numbers in the range 0-1023 are called ( E ) ports and are managed by IANA. ( final1.pdf p.31, p.32 )", "answer": "(C) 80\n(D) 25\n(E) Well-known"},
    q_f1_14: {"question": "3. (3) The file transfer protocol FTP uses two connections: one for control and one for data transfer. The mode where the server establishes the data connection to the client is called ( F ) mode, while the mode where the client establishes the connection to the server is called ( G ) mode. ( final1.pdf p.44, p.45, p.46 )", "answer": "(F) Active\n(G) Passive"},
    q_f1_15: {"question": "3. (4) UDP is a ( H ) protocol, suitable for applications prioritizing ( I ) over reliability (such as audio and video streaming). While the TCP header is typically 20 bytes, the UDP header is lightweight at only ( J ) bytes. ( final1.pdf p.9, p.23 )", "answer": "(H) Connectionless\n(I) Real-time\n(J) 8"},
    q_f1_16: {"question": "4. (1) In TCP control flags, ( A ) indicates a forced connection reset, and ( B ) indicates that the segment contains urgent data. The ( C ) flag, which indicates that the acknowledgment number field is valid, is set in all segments after the connection is established. ( final1.pdf p.21, p.24 )", "answer": "(A) RST\n(B) URG\n(C) ACK"},
    q_f1_17: {"question": "4. (2) In TCP sequencing, the number indicating the position of the first byte of the segment in the entire data stream is called the ( D ) number. Meanwhile, the number indicating the start position of the data the receiver expects next is called the ( E ) number. ( final1.pdf p.22 )", "answer": "(D) Sequence\n(E) Acknowledgment"},
    q_f1_18: {"question": "4. (3) For secure communication, ( F ) is often used instead of TELNET. ( F ) uses port number ( G ) and encrypts the communication channel. Additionally, HTTPS, which encrypts HTTP using SSL/TLS for web browsing, uses port number ( H ). ( final1.pdf p.32, p.43 )", "answer": "(F) SSH\n(G) 22\n(H) 443"},
    q_f1_19: {"question": "4. (4) The name resolution service ( I ) uses port 53 and translates between hostnames and IP addresses. The protocol that dynamically assigns IP addresses to hosts connected to a network is called ( J ). ( final1.pdf p.12, p.32 )", "answer": "(I) DNS\n(J) DHCP"},
    q_f1_20: {"question": "4. (5) Methods to enhance security in file transfer include ( K ), which uses the SSH mechanism to transfer files, and ( L ), which encrypts the FTP communication itself using SSL/TLS. ( final1.pdf p.49 )", "answer": "(K) SFTP (or SCP)\n(L) FTPS"},
    # 4. 記述・説明問題 (応用)
    q_f1_21: {"question": "5. (1) In the TCP Slow Start phase, how does the Congestion Window size (cwnd) increase? Explain from two perspectives: 'every time an ACK is received' and 'every Round Trip Time (RTT)'. ( final1.pdf p.35 )", "answer": "It increases by 1 segment every time an ACK is received, resulting in a doubling of the size every Round Trip Time (RTT) (Exponential Increase)."},
    q_f1_22: {"question": "5. (2) Briefly explain why FTP separates the Control Connection (Port 21) and the Data Transfer Connection (Port 20, etc.), touching on their respective roles. ( final1.pdf p.45 )", "answer": "Because the Control Connection is dedicated to exchanging commands and response codes (control information), while the Data Transfer Connection handles the actual transmission of file data."},
    q_f1_23: {"question": "5. (3) The UDP datagram header size is very small, at 8 bytes. List all 4 fields contained in this header. ( final1.pdf p.24 )", "answer": "Source Port Number, Destination Port Number, Length, Checksum"},
    # 5. 新規追加 (7章)
    q_f1_24: {"question": "6. (1) The DHCP procedure for a client to receive IP address settings consists of four stages: ( A ) for the client to broadcast to find a server, ( B ) for the server to notify the allocation information, ( C ) for the client to request the lease, and ( D ) for the server to confirm the permission. ( 7-1インターネット.pdf p.21 )", "answer": "(A) DHCP DISCOVER\n(B) DHCP OFFER\n(C) DHCP REQUEST\n(D) DHCP ACK"},
    q_f1_25: {"question": "6. (2) Explain the functional differences between the Client-Server model and the P2P model from the perspective of **load distribution** and **scalability**. ( 7-1インターネット.pdf p.11, p.12 )", "answer": "The Client-Server model concentrates the load on the server and has low scalability. The P2P model achieves load distribution through peers and has high fault tolerance and high scalability."},
    q_f1_26: {"question": "6. (3) Explain why the internet architecture features a 'simple communication model within the network,' addressing the function the network prioritizes and the role assumed by the hosts. ( 7-1インターネット.pdf p.13 )", "answer": "It is based on the design philosophy that the network prioritizes **connectivity** (delivering data) and delegates complex processing like **reliability and security** to the **end-host devices** (communication hosts)."},
    q_f1_27: {"question": "6. (4) The addresses used by each layer of the OSI model are different. ( K ) is used in the Application Layer, ( L ) in the Transport Layer, ( M ) in the Network Layer, and ( N ) in the Data Link Layer. ( 7-1インターネット.pdf p.15 )", "answer": "(K) Domain Name\n(L) Port Number\n(M) IP Address\n(N) MAC Address"},
    q_f1_28: {"question": "6. (5) What is the name of the server that is located at the top of DNS hierarchy and has 13 instances worldwide for translating domain names and IP addresses? ( 7-1インターネット.pdf p.18 )", "answer": "Root DNS Server"},
    q_f1_29: {"question": "6. (6) In DNS name resolution, what is the querying method called when the client first queries its local DNS server (resolver) before that resolver queries the root DNS server? ( 7-1インターネット.pdf p.19 )", "answer": "Recursive Query"},
    q_f1_30: {
        "question": "7. (1) The origin of the Internet is considered to be ( A ), developed in the US in 1969. It started as research into ( B ) networks that can maintain communication even if specific parts fail. ( 7-1インターネット.pdf p.7 )",
        "answer": "(A) ARPANET\n(B) Distributed"
    },
    q_f1_31: {
        "question": "7. (2) In a domain name, the rightmost part is called the Top Level Domain (TLD). Those assigned by country, such as `.jp` or `.uk`, are called ( C ), and those assigned by category, such as `.com` or `.org`, are called ( D ). ( 7-1インターネット.pdf p.17 )",
        "answer": "(C) ccTLD (country code TLD)\n(D) gTLD (generic TLD)"
    },
    q_f1_32: {
        "question": "7. (3) To reduce the query load on DNS servers and network traffic, the mechanism of storing the results of name resolution for a certain period is called ( E ). ( 7-1インターネット.pdf p.18 )",
        "answer": "(E) Caching"
    },
    q_f1_33: {
        "question": "7. (4) DHCP automatically configures more than just the IP address. It also notifies the client of the ( F ) which defines the network range, the ( G ) which is the router's IP address serving as the exit to other networks, and the address of the ( H ) for name resolution. ( 7-1インターネット.pdf p.20 )",
        "answer": "(F) Subnet Mask\n(G) Default Gateway\n(H) DNS Server"
    },
    q_f1_34: {
        "question": "7. (5) A model where connected computers (peers) communicate directly with each other without going through a specific server is called the ( I ) model. This model is characterized by high ( J ) (scalability) because the load is not concentrated on a server. ( 7-1インターネット.pdf p.10, p.12 )",
        "answer": "(I) P2P (Peer-to-Peer)\n(J) Scalability (or Fault Tolerance)"
    },
    q_f1_35: {
        "question": "8. (1) In email delivery, the protocol used for sending and forwarding is ( A ), while the protocols used for receiving are ( B ) and ( C ). ( A ) typically uses port number ( D ), ( B ) uses ( E ), and ( C ) uses ( F ). ( 7-2メールサービス.pdf p.24, p.26, p.32, p.37 )",
        "answer": "(A) SMTP\n(B) POP3\n(C) IMAP\n(D) 25\n(E) 110\n(F) 143"
    },
    q_f1_36: {
        "question": "8. (2) When identifying the destination mail server using DNS, the ( G ) record is referenced instead of the standard hostname resolution (A record). This mechanism links the domain name (e.g., @kitakyu-u.ac.jp) to the actual mail server name. ( 7-2メールサービス.pdf p.26 )",
        "answer": "(G) MX (Mail eXchange)"
    },
    q_f1_37: {
        "question": "8. (3) Briefly explain the necessity of 'SMTP Authentication (SMTP-AUTH)' in the SMTP protocol from the perspective of **spam prevention**. ( 7-2メールサービス.pdf p.29, p.30 )",
        "answer": "Since traditional SMTP lacked user authentication, allowing anyone to send emails freely, a mechanism to authenticate users upon sending became necessary to prevent unauthorized relaying by third parties (spam relaying)."
    },
    q_f1_38: {
        "question": "8. (4) Explain the functional differences between the email receiving protocols POP3 and IMAP from the perspectives of 'email management location' and 'usage on multiple devices'. ( 7-2メールサービス.pdf p.37 )",
        "answer": "POP3 downloads emails from the server to the client for management, making synchronization across multiple devices difficult. In contrast, IMAP manages emails on the server, with the client holding only a cache, allowing access and manipulation of the same mailbox from multiple devices."
    },
    q_f1_39: {
        "question": "8. (5) In user authentication during email reception, unlike POP authentication which sends the password in plain text, the method that enhances security by combining a **challenge string** sent from the server with the password to calculate a hash value and sending only that result (response) is called ( H ) authentication. ( 7-2メールサービス.pdf p.36 )",
        "answer": "(H) APOP"
    },
    q_f1_40: {
        "question": "8. (6) Email header information includes ( I ) indicating the sender, ( J ) indicating the recipient, and ( K ) indicating the subject. Additionally, the actual delivery route (information of mail servers passed through) is recorded in the ( L ) field, allowing tracing of the email's origin. ( 7-2メールサービス.pdf p.41, p.42 )",
        "answer": "(I) From\n(J) To\n(K) Subject\n(L) Received"
    },

    q_f1_41: {
        "question": "9. (1) The WWW (World Wide Web) is a hypertext system on the Internet consisting of three elements: ( A ) which indicates the location of resources, ( B ) which is the document description language, and ( C ) which is the communication protocol. ( 7-3Web サービス.pdf p.44 )",
        "answer": "(A) URL (or URI)\n(B) HTML\n(C) HTTP"
    },
    q_f1_42: {
        "question": "9. (2) The message sent by a web browser (client) to a web server saying 'please give me this page' is called a ( D ), and the message returned by the server is called a ( E ). These are composed of three parts: the ( F ) line, the header, and the ( G ). ( 7-3Web サービス.pdf p.50, p.51 )",
        "answer": "(D) Request (HTTP Request)\n(E) Response (HTTP Response)\n(F) Status (or Request/Response)\n(G) Message Body"
    },
    q_f1_43: {
        "question": "9. (3) The ( F ) line of an HTTP request contains a method. The method to retrieve a web page is ( H ), to retrieve only header information is ( I ), and to send form data is ( J ). ( 7-3Web サービス.pdf p.52 )",
        "answer": "(H) GET\n(I) HEAD\n(J) POST"
    },
    q_f1_44: {
        "question": "9. (4) The ( F ) line of an HTTP response contains a status code. The code indicating a successful request is ( K ), if the page is not found it is ( L ), if access is denied it is ( M ), and internal server errors are in the 500 range. ( 7-3Web サービス.pdf p.53 )",
        "answer": "(K) 200 (OK)\n(L) 404 (Not Found)\n(M) 403 (Forbidden)"
    },
    q_f1_45: {
        "question": "9. (5) In HTTP, which is a stateless protocol, the small text data saved by the server on the browser to maintain 'state' such as shopping carts or login status is called ( N ). ( 7-3Web サービス.pdf p.55 )",
        "answer": "(N) Cookie"
    },
    q_f1_46: {
        "question": "9. (6) As a mechanism to dynamically generate web pages, the mechanism that executes a program on the server side and returns the result is called ( O ). On the other hand, programs executed on the client (browser) side using JavaScript etc. are sometimes called ( P ) applications. ( 7-3Web サービス.pdf p.45 )",
        "answer": "(O) CGI (Common Gateway Interface)\n(P) Helper (or Client-side)"
    },
    q_f1_47: {
        "question": "10. (1) As the definition of information security, answer the three properties of information (CIA) that must be maintained. They are ( A ) meaning only authorized persons can access it, ( B ) meaning the content is accurate and complete, and ( C ) meaning it can be accessed whenever needed. ( 8-1ネットワークセキュリティ.pdf p.7, p.18 )",
        "answer": "(A) Confidentiality\n(B) Integrity\n(C) Availability"
    },
    q_f1_48: {
        "question": "10. (2) Threats to security include ( D ) which threatens confidentiality, ( E ) which threatens integrity, and ( F ) which threatens availability. ( 8-1ネットワークセキュリティ.pdf p.8 )",
        "answer": "(D) Eavesdropping (or Unauthorized Access)\n(E) Tampering\n(F) Denial of Service (DoS) attack"
    },
    q_f1_49: {
        "question": "10. (3) An attack that infringes on service availability by sending massive amounts of packets to down a server is called a ( G ) attack. Also, one where multiple computers coordinate to attack simultaneously is called a ( H ) attack. ( 8-1ネットワークセキュリティ.pdf p.12 )",
        "answer": "(G) DoS (Denial of Service)\n(H) DDoS (Distributed DoS)"
    },
    q_f1_50: {
        "question": "10. (4) Explain attacks targeting vulnerabilities in web applications. An attack that illegally manipulates a database by sending illegal values in the input that constructs database commands is called ( I ). ( 8-1ネットワークセキュリティ.pdf p.14 )",
        "answer": "(I) SQL Injection"
    },
    q_f1_51: {
        "question": "10. (5) Similarly, an attack that exploits website vulnerabilities to execute malicious scripts on the viewer's browser is called ( J ). This enables unauthorized acquisition of Cookie information, etc. ( 8-1ネットワークセキュリティ.pdf p.15 )",
        "answer": "(J) Cross Site Scripting (XSS)"
    },
    q_f1_52: {
        "question": "10. (6) An attack method that steals information by taking advantage of human psychological gaps or behavioral mistakes (such as poor password management) rather than technical vulnerabilities is called ( K ). ( 8-1ネットワークセキュリティ.pdf p.13 )",
        "answer": "(K) Social Engineering"
    },
    q_f1_53: {
        "question": "10. (7) An attack that acquires internal information by observing the operating conditions of a device (such as power fluctuations or leaked electromagnetic waves) using physical means is called a ( L ) attack or an ( M ) attack. ( 8-1ネットワークセキュリティ.pdf p.16 )",
        "answer": "(L) Side Channel\n(M) Implementation"
    },
    q_f1_54: {
        "question": "11. (1) Cryptography is a fundamental technology for ensuring ( A ) and ( B ) in information security. Converting plaintext to ciphertext is called ( C ), and restoring ciphertext to original plaintext is called ( D ). ( 8-2 暗号.pdf p.22 )",
        "answer": "(A) Confidentiality\n(B) Integrity\n(C) Encryption\n(D) Decryption"
    },
    q_f1_55: {
        "question": "11. (2) Modern cryptography is based on ( F )'s principle, which states that 'the algorithm is public, and only the ( E ) is kept secret'. This allows the security of the algorithm to be verified worldwide. ( 8-2 暗号.pdf p.24 )",
        "answer": "(E) Key\n(F) Kerckhoffs"
    },
    q_f1_56: {
        "question": "11. (3) Symmetric key encryption uses the ( G ) key for encryption and decryption. It has the advantage of ( H ) processing, but has the problem of ( I ) because a different key is required for each communication partner. A representative algorithm is ( J ). ( 8-2 暗号.pdf p.25, p.26 )",
        "answer": "(G) Same (Common)\n(H) Fast\n(I) Key Distribution (or Key Management)\n(J) AES"
    },
    q_f1_57: {
        "question": "11. (4) Public key encryption uses a ( K ) key that anyone can use for encryption, and a ( L ) key that only the owner has for decryption. Processing is ( M ), but key distribution is easy. A representative algorithm, ( N ), relies on the difficulty of prime factorization for security. ( 8-2 暗号.pdf p.26, p.27 )",
        "answer": "(K) Public\n(L) Private\n(M) Slow\n(N) RSA"
    },
    q_f1_58: {
        "question": "11. (5) A fixed-length value generated from original data to verify data integrity is called a ( O ). ( P ) using this allows the sender to encrypt (sign) with their ( Q ) key and the receiver to decrypt (verify) with the sender's ( R ) key, performing identity verification and tamper detection. ( 8-2 暗号.pdf p.29 )",
        "answer": "(O) Hash Value\n(P) Digital Signature\n(Q) Private\n(R) Public"
    },
    q_f1_59: {
        "question": "11. (6) Data issued by a trusted third-party organization, ( S ), to prove that a public key belongs to a legitimate owner is called a ( T ). The social security infrastructure using this is called ( U ). ( 8-2 暗号.pdf p.30 )",
        "answer": "(S) Certificate Authority (CA)\n(T) Digital Certificate\n(U) PKI (Public Key Infrastructure)"
    },
    q_f1_60: {
        "question": "11. (7) Actual secure communication (such as SSL/TLS) uses a hybrid method to solve processing speed issues. ( V ) encryption is used for key exchange and authentication, and ( W ) encryption, which is fast, is used for encrypting large amounts of data. ( 8-2 暗号.pdf p.31 )",
        "answer": "(V) Public Key\n(W) Symmetric Key"
    },

    q_f1_61: {
        "question": "13. (1) Properties that secure communication must satisfy include ( A ) to prevent eavesdropping, ( B ) to prevent spoofing, ( C ) to prevent tampering, and ( D ) to prove that facts cannot be denied. ( 8-3セキュア通信プロトコル.pdf p.36, p.42 )",
        "answer": "(A) Confidentiality\n(B) Authentication\n(C) Message Integrity\n(D) Non-repudiation"
    },
    q_f1_62: {
        "question": "13. (2) The secure communication protocol that operates at the Transport Layer (Layer 4) is called ( E ). When applied to web browser communication (HTTP), it is called ( F ) and uses port number ( G ). ( 8-3セキュア通信プロトコル.pdf p.37 )",
        "answer": "(E) SSL/TLS\n(F) HTTPS\n(G) 443"
    },
    q_f1_63: {
        "question": "13. (3) SSL/TLS uses a hybrid mechanism to ensure communication performance. It uses ( H ) encryption for exchanging the session key (symmetric key), and fast ( I ) encryption for encrypting actual data communication. Also, ( J ) is used for tamper detection. ( 8-3セキュア通信プロトコル.pdf p.38 )",
        "answer": "(H) Public Key\n(I) Symmetric Key\n(J) Message Authentication Code (MAC)"
    },
    q_f1_64: {
        "question": "13. (4) The secure communication protocol that operates at the Internet Layer (Layer 3) is called ( K ). It is often used to build ( L ) for connecting networks. ( 8-3セキュア通信プロトコル.pdf p.40, p.42 )",
        "answer": "(K) IPsec\n(L) VPN (Virtual Private Network)"
    },
    q_f1_65: {
        "question": "13. (5) In IPsec operation modes, the mode that encrypts only the data part (payload) and is used for host-to-host communication is called ( M ) mode, while the mode that encrypts and encapsulates the entire IP packet and is used for gateway-to-gateway communication is called ( N ) mode. ( 8-3セキュア通信プロトコル.pdf p.40 )",
        "answer": "(M) Transport\n(N) Tunnel"
    },
    q_f1_66: {
        "question": "13. (6) Among the protocols constituting IPsec, the one that provides only authentication and tamper prevention is called ( O ), and the one that additionally provides data encryption functions is called ( P ). ( 8-3セキュア通信プロトコル.pdf p.40 )",
        "answer": "(O) AH (Authentication Header)\n(P) ESP (Encapsulated Security Payload)"
    },

    q_f1_67: {
        "question": "14. (1) A device that prevents the intrusion of unauthorized packets from the outside is called a ( A ). Packet filtering methods include ( B ) filtering, which blocks based on specific IP addresses or port numbers, and ( C ) filtering, which allows only response packets to communication initiated internally. ( 8-4防御技術.pdf p.45 )",
        "answer": "(A) Firewall\n(B) Static\n(C) Dynamic"
    },
    q_f1_68: {
        "question": "14. (2) An area located between the Internet and the internal network, used for placing servers that need to be open to the public (such as web servers and mail servers), is called a ( D ). ( 8-4防御技術.pdf p.46 )",
        "answer": "(D) DMZ (DeMilitarized Zone)"
    },
    q_f1_69: {
        "question": "14. (3) A system that analyzes packet contents and logs to detect and report signs of attacks such as DoS attacks or port scans is called ( E ), while a system that not only detects but also takes defensive measures such as blocking is called ( F ). ( 8-4防御技術.pdf p.47 )",
        "answer": "(E) IDS (Intrusion Detection System)\n(F) IPS (Intrusion Prevention System)"
    },
    q_f1_70: {
        "question": "14. (4) A relay server that accesses the Internet on behalf of internal clients is called a ( G ). It improves security through address translation and filtering of harmful information, and improves communication efficiency with its ( H ) function that saves previously accessed information. ( 8-4防御技術.pdf p.48 )",
        "answer": "(G) Proxy\n(H) Cache"
    },
    q_f1_71: {
        "question": "14. (5) A mechanism that connects a PC brought into the company to a specialized inspection network to check its security status (virus protection, etc.) before connecting it to the internal LAN is called a ( I ). ( 8-4防御技術.pdf p.49 )",
        "answer": "(I) Quarantine Network"
    },
    q_f1_72: {
        "question": "14. (6) The technology or mechanism for collecting, analyzing, and preserving data (such as logs and communication packets) necessary for determining the legal cause when an incident occurs is called ( J ). ( 8-4防御技術.pdf p.49 )",
        "answer": "(J) Digital Forensics"
    },


    q_f1_73: {
        "question": "15. (1) Compare Client-Server and P2P models in terms of Service Type (Centralized/Distributed), Fault Tolerance (High/Low), and Scalability (High/Low).",
        "answer": "Client-Server: (a) Centralized, (d) Low Fault Tolerance, (f) Low Scalability.\nP2P: (b) Autonomous Distributed, (c) High Fault Tolerance, (e) High Scalability."
    },
    q_f1_74: {
        "question": "15. (2) The main role of DNS is to convert ( a ) to ( b ), which is called ( c ).",
        "answer": "(a) Domain Name\n(b) IP Address\n(c) Name Resolution"
    },
    q_f1_75: {
        "question": "15. (3) What protocol automatically configures settings when a client connects to a network using the ( a ) function? Protocol is ( b ).",
        "answer": "(a) Broadcast\n(b) DHCP"
    },
    q_f1_76: {
        "question": "15. (4) Name the protocols used in mail delivery:\n1. Client -> Send Server\n2. Server -> Server\n3. Receive Server -> Client\n4. Browser <-> Web Mail",
        "answer": "1. SMTP\n2. SMTP\n3. POP3 or IMAP\n4. HTTP"
    },

    q_f1_77: {
        "question": "15. (5) Explain the functional difference between POP3 and IMAP.",
        "answer": "POP3 is a simple protocol premised on downloading and processing mail.\nIMAP is a high-functionality protocol premised on managing mail on the server, enabling access from multiple clients."
    },
   
    q_f1_78: {
        "question": "15. (6) TCP is a ( a ) type protocol. The receiver sends back an ( b ) number for acknowledgment. ( c ) number is used for sequence control.",
        "answer": "(a) Connection-oriented\n(b) Acknowledgment (ACK)\n(c) Sequence"
    },
    q_f1_79: {
        "question": "15. (7) Explain the difference between Flow Control and Congestion Control so that their purposes and control methods are clear.",
        "answer": "In Flow Control, the transmission rate is adjusted according to the receivable buffer size notified by the receiving host so as not to exceed the receiving host's processing capacity.\nOn the other hand, in Congestion Control, the transmission rate is adjusted according to the network's congestion state so as not to exceed the network's processing capacity."
    },
    q_f1_80: {
        "question": "15. (8) Concretely explain the control method of the Congestion Window.",
        "answer": "In the Slow Start phase, it increases exponentially (quickly increasing the transmission rate). After exceeding the Slow Start threshold, it moves to the Congestion Avoidance phase and increases linearly (slowly increasing the transmission rate) to find the appropriate congestion window."
    },
    q_f1_81: {
        "question": "15. (9) Calculate Transmission Bitrate (RTT=10ms, Segment=8000bits, AdvWin=15).\n(a) Cwnd=5\n(b) Cwnd=25",
        "answer": "(a) 4 Mbps (Effective Window = min(5,15) = 5)\n(b) 12 Mbps (Effective Window = min(25,15) = 15, limited by AdvWin)"
    },
    q_f1_82: {
        "question": "15. (10) Define the 3 elements of Information Security (CIA).",
        "answer": "Confidentiality: Access only by authorized users.\nIntegrity: Information is accurate and complete.\nAvailability: Accessible when needed."
    },
    q_f1_83: {
        "question": "15. (11) (1) SSL/TLS is a ( a ) layer protocol preventing eavesdropping and ( b ). (2) IPsec is a ( c ) layer protocol; Transport mode encrypts ( d ), Tunnel mode encrypts ( e ).",
        "answer": "(1) (a) Transport, (b) Tampering (and Spoofing)\n(2) (c) Internet, (d) Payload (Data), (e) Entire IP Packet"
    },
    q_f1_84: {
        "question": "15. (12) Fill in the blanks for SSL/TLS Handshake:\nii. Verify cert using ( a ).\niii. Encrypt session key using ( b ).\niv. Server decrypts using ( c ).",
        "answer": "(a) CA's Public Key\n(b) Server's Public Key\n(c) Server's Private Key"
    },
    q_f1_85: {
        "question": "15. (13) Briefly explain DMZ, IDS vs IPS, and Packet Filtering types.",
        "answer": "DMZ: Area for public servers.\nIDS: Detect/Report. IPS: Detect/Block.\nFiltering: Static, Dynamic, Stateful."
    },

    q_f1_86: {
        "question": "16. (1) [Prediction] WWW uses ( a ) protocol. Since ( a ) is stateless, ( b ) is used to maintain state. The method for clients to send data is ( c ).",
        "answer": "(a) HTTP\n(b) Cookie\n(c) POST"
    },
    q_f1_87: {
        "question": "16. (2) [Prediction] Encryption using the same key is ( a ). It is ( b ) but has a ( c ) problem. The method using two paired keys is ( d ), and a typical algorithm is ( e ).",
        "answer": "(a) Symmetric Key Encryption (Common Key)\n(b) Fast\n(c) Key Distribution\n(d) Public Key Encryption\n(e) RSA"
    },
    q_f1_88: {
        "question": "16. (3) [Prediction] An attack mixing illegal input into DB commands is ( a ). Embedding malicious scripts in web pages is ( b ). Sending massive packets to disrupt service is ( c ).",
        "answer": "(a) SQL Injection\n(b) Cross Site Scripting (XSS)\n(c) DoS Attack"
    },
    q_f1_89: {
        "question": "16. (4) [Prediction] Explain the difference between Static Filtering, Dynamic Filtering, and Stateful Inspection in firewalls.",
        "answer": "Static: Judges based on fixed rules (IP/Port). Dynamic: Allows only response packets. Stateful: Monitors protocol sequence and communication context."
    },
    q_f1_90: {
        "question": "16. (5) [Prediction] In Digital Signatures, who encrypts/decrypts with which key? What two things are verified?",
        "answer": "Encrypt: Sender uses Sender's Private Key.\nDecrypt: Receiver uses Sender's Public Key.\nVerified: Sender identity (Authentication) and Integrity (No tampering)."
    },
    q_f1_91: {
        "question": "16. (6) [Prediction] Briefly explain the difference between IDS and IPS.",
        "answer": "IDS: Detects and Alerts (usually does not block).\nIPS: Detects and Blocks (Prevents)."
    },
    q_f1_92: {
        "question": "17. (1) [Ex4-1] The 3 elements of InfoSec are ( a ) (access by authorized users only), ( b ) (accurate/complete info), and ( c ) (accessible when needed). ( 演習課題4-解答.pdf p.1 )",
        "answer": "(a) Confidentiality\n(b) Integrity\n(c) Availability"
    },
    q_f1_93: {
        "question": "17. (2) [Ex4-1] Even with mathematically secure encryption, keys may be stolen by ( d ). ( 演習課題4-解答.pdf p.1 )",
        "answer": "(d) Implementation Attack (or Side Channel Attack)"
    },
    q_f1_94: {
        "question": "17. (3) [Ex4-1] In Symmetric Key Encryption, ( e ) is used for both keys, so it is necessary to ( f ) it between users beforehand. ( 演習課題4-解答.pdf p.1 )",
        "answer": "(e) Common Key (Symmetric Key)\n(f) Share (or Distribute)"
    },
    q_f1_95: {
        "question": "17. (4) [Ex4-2] In Public Key Encryption, when 'encrypting' a message (Confidentiality), use ( a ) for encryption and ( b ) for decryption. ( 演習課題4-解答.pdf p.1 )",
        "answer": "(a) Receiver's Public Key\n(b) Receiver's Private Key"
    },
    q_f1_96: {
        "question": "17. (5) [Ex4-2] When performing 'Digital Signature' (Authentication), encrypt the hash using ( c ). The receiver decrypts using ( d ) to verify. ( 演習課題4-解答.pdf p.1 )",
        "answer": "(c) Sender's Private Key\n(d) Sender's Public Key"
    },
    q_f1_97: {
        "question": "17. (6) [Ex4-3] Fill in the blanks for SSL/TLS:\n(1) Server sends ( a ) and cert.\n(2) Client verifies cert using ( b ).\n(3) Client encrypts session key data using ( c ).\n(4) Server decrypts using ( d ). ( 演習課題4-解答.pdf p.2 )",
        "answer": "(a) Server's Public Key\n(b) CA's Public Key\n(c) Server's Public Key\n(d) Server's Private Key"
    },
    q_f1_98: {
        "question": "17. (7) [Ex4-4] Explain the functions of IDS (Intrusion Detection System) and IPS (Intrusion Prevention System). ( 演習課題4-解答.pdf p.2 )",
        "answer": "IDS: Analyzes packets/logs to detect and report signs of attacks.\nIPS: In addition to IDS functions, can take measures such as blocking."
    },
    q_f1_99: {
        "question": "18. (1) [Physical Layer] Describe the role of the Physical Layer.",
        "answer": "Hardware functions such as electrical signal levels and connector shapes."
    },
    q_f1_100: {
        "question": "18. (2) [Data Link Layer] Describe the role of the Data Link Layer.",
        "answer": "Control functions for correctly transmitting data between communication nodes via transmission media."
    },
    q_f1_101: {
        "question": "18. (3) [Network Layer] Describe the role of the Network Layer.",
        "answer": "Route selection (routing) via multiple relay nodes and data relay/forwarding functions."
    },
    q_f1_102: {
        "question": "18. (4) [Transport Layer] Describe the role of the Transport Layer.",
        "answer": "Management of logical connections between sending and receiving hosts, and guarantee of communication quality and reliability."
    },
    q_f1_103: {
        "question": "18. (5) [Session Layer] Describe the role of the Session Layer.",
        "answer": "Synchronization control functions for data transmission, such as starting, maintaining, and ending communication between applications."
    },
    q_f1_104: {
        "question": "18. (6) [Presentation Layer] Describe the role of the Presentation Layer.",
        "answer": "Control functions regarding data representation formats (encoding, encryption, etc.)."
    },
    q_f1_105: {
        "question": "18. (7) [Application Layer] Describe the role of the Application Layer.",
        "answer": "Various communication functions according to specific services (e.g., e-mail)."
    }

  

}

# --- タイ語翻訳 ---

thai_translations = {
    q_f1_0: "แฟลชการ์ดสอบปลายภาค - สถาปัตยกรรมเครือข่าย 2",
    # 1. 語句選択問題 (基本)
    q_f1_1: {"question": "1. (1) สิ่งที่เรียกว่าเส้นทางการสื่อสารเสมือนจริงระหว่างโฮสต์ผู้ส่งและผู้รับซึ่งจัดการโดย Transport Layer (OSI Layer 4) คืออะไร? ( final1.pdf p.3 )", "answer": "การเชื่อมต่อแบบลอจิคัล (Logical Connection)"},
    q_f1_2: {"question": "1. (2) TCP ให้บริการการสื่อสารแบบ connection-oriented แล้ว UDP ให้บริการการสื่อสารประเภทใด? ( final1.pdf p.9 )", "answer": "บริการแบบไร้การเชื่อมต่อ (Connectionless Service)"},
    q_f1_3: {"question": "1. (3) ฟังก์ชันควบคุม TCP ใดที่ป้องกันไม่ให้ผู้รับได้รับข้อมูลมากเกินไป (overflow) โดยการแจ้งผู้ส่งถึงจำนวนข้อมูลสูงสุดที่รับได้? ( final1.pdf p.18, p.22 )", "answer": "การควบคุมการไหลของข้อมูล (Flow Control)"},
    q_f1_4: {"question": "1. (4) แฟล็กควบคุม TCP ใดที่ใช้สำหรับการขอตัดการเชื่อมต่อ? ( final1.pdf p.21 )", "answer": "FIN"},
    q_f1_5: {"question": "1. (5) อินเทอร์เฟซที่ระบุโดยการรวมกันของที่อยู่ IP และหมายเลขพอร์ต ซึ่งใช้เพื่อระบุแอปพลิเคชัน เรียกว่าอะไร? ( final1.pdf p.29 )", "answer": "ซ็อกเก็ต (Socket)"},
    q_f1_6: {"question": "1. (6) หมายเลขพอร์ต (ช่วง 1 ถึง 1023) ที่ถูกกำหนดให้กับบริการหลัก เช่น HTTP (80) และ SMTP (25) เรียกว่าอะไร? ( final1.pdf p.31, p.32 )", "answer": "เวลโนวน์พอร์ต (Well-known Port)"},
    q_f1_7: {"question": "1. (7) โหมดการถ่ายโอนข้อมูล FTP ใดที่ไคลเอนต์เป็นผู้สร้างการเชื่อมต่อกับเซิร์ฟเวอร์? ( final1.pdf p.44, p.46 )", "answer": "โหมดพาสซีฟ (Passive Mode)"},
    q_f1_8: {"question": "1. (8) คำสั่งใดที่ไคลเอนต์ใช้ใน FTP เพื่อส่ง (อัปโหลด) ไฟล์? ( final1.pdf p.47 )", "answer": "STOR"},
    
    # 2. 説明問題 (基本)
    q_f1_9: {"question": "2. (1) อธิบายความแตกต่างระหว่าง **TCP Flow Control** และ **Congestion Control** โดยย่อ โดยเน้นว่าใช้ขนาดหน้าต่างใดเป็นเกณฑ์และ **ป้องกันอะไร** ( final1.pdf p.33, p.34 )", "answer": "Flow Control ใช้ **Advertised Window Size** (แจ้งโดยผู้รับ) เพื่อป้องกัน **ผู้รับได้รับข้อมูลมากเกินไป** (receiver overflow) ส่วน Congestion Control ใช้ **Congestion Window Size** (จัดการโดยผู้ส่ง) เพื่อป้องกัน **ความคับคั่งในเครือข่าย** (network congestion)"},
    q_f1_10: {"question": "2. (2) อธิบายวัตถุประสงค์ของ **TCP 3-Way Handshake** และแฟล็กควบคุมที่ไคลเอนต์ส่งในขั้นตอนแรก ( final1.pdf p.25, p.21 )", "answer": "วัตถุประสงค์: เพื่อ **ยืนยันความสามารถในการสื่อสารร่วมกัน** และ **สร้างการเชื่อมต่อ** ก่อนที่จะมีการถ่ายโอนข้อมูล แฟล็ก: ไคลเอนต์ส่งแฟล็ก **SYN** (synchronize) ในขั้นตอนแรก"},
    q_f1_11: {"question": "2. (3) อธิบายความแตกต่างด้านการทำงานระหว่างโปรโตคอล Application Layer **TELNET** และ **SSH** โดยเน้นที่ **ความปลอดภัยของเส้นทางการสื่อสาร** ( final1.pdf p.43 )", "answer": "TELNET เป็นโปรโตคอลเทอร์มินัลเสมือนที่ **ไม่มีการเข้ารหัสเส้นทางการสื่อสาร** ทำให้เสี่ยงต่อการถูกดักฟังข้อมูล ในขณะที่ SSH (Secure Shell) ใช้ **การเข้ารหัส SSL/TLS** สำหรับเส้นทางการสื่อสาร จึงมีความปลอดภัยสูง"},
    # 3. 穴埋め問題 (応用)
    q_f1_12: {"question": "3. (1) ในการควบคุมความคับคั่งของ TCP (Congestion Control) เฟส ( A ) จะเพิ่มขนาดของหน้าต่างความคับคั่งแบบทวีคูณเมื่อเริ่มการสื่อสารหรือหลังจากหมดเวลา (timeout) หลังจากเกินค่าขีดจำกัด Slow Start (ssthresh) จะเปลี่ยนไปสู่เฟส ( B ) ซึ่งขนาดหน้าต่างจะเพิ่มขึ้นเป็นเส้นตรงเพื่อใช้แบนด์วิดท์อย่างมีประสิทธิภาพและหลีกเลี่ยงความคับคั่ง ( final1.pdf p.35, p.36 )", "answer": "(A) Slow Start (สโลว์สตาร์ท)\n(B) Congestion Avoidance (การหลีกเลี่ยงความคับคั่ง)"},
    q_f1_13: {"question": "3. (2) แอปพลิเคชันจะถูกระบุโดยหมายเลขพอร์ตของ Transport Layer ตัวอย่างเช่น เว็บเซิร์ฟเวอร์ (HTTP) มักใช้พอร์ต ( C ) และ SMTP สำหรับการส่งเมลใช้พอร์ต ( D ) หมายเลขพอร์ตในช่วง 0-1023 เรียกว่า ( E ) พอร์ต และได้รับการจัดการโดย IANA ( final1.pdf p.31, p.32 )", "answer": "(C) 80\n(D) 25\n(E) Well-known (เวลโนวน์)"},
    q_f1_14: {"question": "3. (3) โปรโตคอลการถ่ายโอนไฟล์ FTP ใช้การเชื่อมต่อสองแบบ: แบบควบคุมและแบบถ่ายโอนข้อมูล โหมดที่เซิร์ฟเวอร์สร้างการเชื่อมต่อข้อมูลไปยังไคลเอนต์เรียกว่าโหมด ( F ) ในขณะที่โหมดที่ไคลเอนต์สร้างการเชื่อมต่อข้อมูลไปยังเซิร์ฟเวอร์เรียกว่าโหมด ( G ) ( final1.pdf p.44, p.45, p.46 )", "answer": "(F) Active (แอคทีฟ)\n(G) Passive (พาสซีฟ)"},
    q_f1_15: {"question": "3. (4) UDP เป็นโปรโตคอลแบบ ( H ) ซึ่งเหมาะสำหรับแอปพลิเคชันที่ให้ความสำคัญกับ ( I ) มากกว่าความน่าเชื่อถือ (เช่น การสตรีมเสียงและวิดีโอ) ในขณะที่ส่วนหัวของ TCP โดยทั่วไปมีขนาด 20 ไบต์ ส่วนหัวของ UDP จะมีขนาดเบาเพียง ( J ) ไบต์ ( final1.pdf p.9, p.23 )", "answer": "(H) Connectionless (ไร้การเชื่อมต่อ)\n(I) Real-time (เรียลไทม์)\n(J) 8"},
    q_f1_16: {"question": "4. (1) ในแฟล็กควบคุม TCP ( A ) หมายถึงการบังคับตัดการเชื่อมต่อ (reset) และ ( B ) หมายถึงมีข้อมูลเร่งด่วนรวมอยู่ด้วย นอกจากนี้ แฟล็ก ( C ) ซึ่งระบุว่าฟิลด์หมายเลขการตอบรับนั้นถูกต้อง จะถูกตั้งค่าในทุกเซกเมนต์หลังจากสร้างการเชื่อมต่อแล้ว ( final1.pdf p.21, p.24 )", "answer": "(A) RST\n(B) URG\n(C) ACK"},
    q_f1_17: {"question": "4. (2) ในการจัดลำดับของ TCP หมายเลขที่ระบุตำแหน่งของไบต์แรกของเซกเมนต์ในข้อมูลทั้งหมดเรียกว่าหมายเลข ( D ) ในขณะที่หมายเลขที่ระบุตำแหน่งเริ่มต้นของข้อมูลที่ผู้รับคาดหวังถัดไปเรียกว่าหมายเลข ( E ) ( final1.pdf p.22 )", "answer": "(D) Sequence (ลำดับ)\n(E) Acknowledgment (การตอบรับ)"},
    q_f1_18: {"question": "4. (3) เพื่อความปลอดภัยในการสื่อสาร มักใช้ ( F ) แทน TELNET โดย ( F ) ใช้หมายเลขพอร์ต ( G ) และเข้ารหัสช่องทางการสื่อสาร นอกจากนี้ HTTPS ซึ่งเข้ารหัส HTTP ด้วย SSL/TLS สำหรับการท่องเว็บ ใช้หมายเลขพอร์ต ( H ) ( final1.pdf p.32, p.43 )", "answer": "(F) SSH\n(G) 22\n(H) 443"},
    q_f1_19: {"question": "4. (4) บริการแก้ไขชื่อ ( I ) ใช้พอร์ตหมายเลข 53 และทำการแปลงระหว่างชื่อโฮสต์และที่อยู่ IP และโปรโตคอลที่กำหนดที่อยู่ IP แบบไดนามิกให้กับโฮสต์ที่เชื่อมต่อกับเครือข่ายเรียกว่า ( J ) ( final1.pdf p.12, p.32 )", "answer": "(I) DNS\n(J) DHCP"},
    q_f1_20: {"question": "4. (5) วิธีการเพิ่มความปลอดภัยในการถ่ายโอนไฟล์ ได้แก่ ( K ) ซึ่งใช้กลไก SSH ในการถ่ายโอนไฟล์ และ ( L ) ซึ่งเข้ารหัสการสื่อสาร FTP ด้วย SSL/TLS ( final1.pdf p.49 )", "answer": "(K) SFTP (หรือ SCP)\n(L) FTPS"},
    q_f1_21: {"question": "5. (1) ในเฟส Slow Start ของ TCP ขนาดหน้าต่างความคับคั่ง (cwnd) เพิ่มขึ้นอย่างไร? อธิบายจากสองมุมมอง: 'ทุกครั้งที่ได้รับ ACK' และ 'ทุกรอบเวลาไป-กลับ (RTT)' ( final1.pdf p.35 )", "answer": "เพิ่มขึ้น 1 เซกเมนต์ทุกครั้งที่ได้รับ ACK และส่งผลให้เพิ่มขึ้นเป็น 2 เท่าทุกรอบเวลาไป-กลับ (RTT) (การเพิ่มแบบทวีคูณ)"},
    q_f1_22: {"question": "5. (2) อธิบายสั้นๆ ว่าทำไม FTP ถึงแยกการเชื่อมต่อควบคุม (พอร์ต 21) และการเชื่อมต่อถ่ายโอนข้อมูล (พอร์ต 20 ฯลฯ) โดยกล่าวถึงบทบาทของแต่ละส่วน ( final1.pdf p.45 )", "answer": "เพราะการเชื่อมต่อควบคุมใช้สำหรับแลกเปลี่ยนคำสั่งและรหัสตอบกลับ (ข้อมูลควบคุม) โดยเฉพาะ ในขณะที่การเชื่อมต่อถ่ายโอนข้อมูลใช้สำหรับส่งข้อมูลไฟล์จริง"},
    q_f1_23: {"question": "5. (3) ส่วนหัวของดาต้าแกรม UDP มีขนาดเล็กมากเพียง 8 ไบต์ จงระบุชื่อฟิลด์ทั้ง 4 ที่อยู่ในส่วนหัวนี้ ( final1.pdf p.24 )", "answer": "หมายเลขพอร์ตต้นทาง (Source Port), หมายเลขพอร์ตปลายทาง (Destination Port), ความยาว (Length), เช็คซัม (Checksum)"},
    # 5. 新規追加 (7章)
    q_f1_24: {"question": "6. (1) ขั้นตอน DHCP สำหรับไคลเอนต์เพื่อรับการตั้งค่าที่อยู่ IP ประกอบด้วยสี่ขั้นตอน: ( A ) สำหรับไคลเอนต์ที่จะค้นหาเซิร์ฟเวอร์โดยการบรอดคาสต์, ( B ) สำหรับเซิร์ฟเวอร์ที่จะแจ้งข้อมูลการจัดสรร, ( C ) สำหรับไคลเอนต์ที่จะร้องขอการเช่า, และ ( D ) สำหรับเซิร์ฟเวอร์ที่จะยืนยันการอนุญาต ( 7-1インターネット.pdf p.21 )", "answer": "(A) DHCP DISCOVER\n(B) DHCP OFFER\n(C) DHCP REQUEST\n(D) DHCP ACK"},
    q_f1_25: {"question": "6. (2) อธิบายความแตกต่างของการทำงานระหว่างโมเดล Client-Server และโมเดล P2P จากมุมมองของ **การกระจายโหลด** และ **ความสามารถในการปรับขนาด** ( 7-1インターネット.pdf p.11, p.12 )", "answer": "โมเดล Client-Server โหลดจะกระจุกตัวอยู่ที่เซิร์ฟเวอร์ และมีความสามารถในการปรับขนาดต่ำ โมเดล P2P กระจายโหลดผ่าน peer และมีความทนทานต่อความผิดพลาดสูง และมีความสามารถในการปรับขนาดสูง"},
    q_f1_26: {"question": "6. (3) อธิบายว่าเหตุใดสถาปัตยกรรมอินเทอร์เน็ตจึงมี 'โมเดลการสื่อสารที่เรียบง่ายภายในเครือข่าย' โดยกล่าวถึงฟังก์ชันที่เครือข่ายให้ความสำคัญ และบทบาทที่อุปกรณ์ปลายทางใช้ ( 7-1インターネット.pdf p.13 )", "answer": "เป็นไปตามปรัชญาการออกแบบที่เครือข่ายให้ความสำคัญกับการ **เชื่อมต่อ** (การส่งข้อมูลถึงผู้รับ) และมอบหมายให้การประมวลผลที่ซับซ้อน เช่น **ความน่าเชื่อถือและความปลอดภัย** เป็นหน้าที่ของ **อุปกรณ์โฮสต์ปลายทาง**"},
    q_f1_27: {"question": "6. (4) ที่อยู่ที่ใช้โดยแต่ละเลเยอร์ของโมเดล OSI นั้นแตกต่างกัน ( K ) ใช้ใน Application Layer, ( L ) ใน Transport Layer, ( M ) ใน Network Layer, และ ( N ) ใน Data Link Layer ( 7-1インターネット.pdf p.15 )", "answer": "(K) Domain Name (ชื่อโดเมน)\n(L) Port Number (หมายเลขพอร์ต)\n(M) IP Address (ที่อยู่ IP)\n(N) MAC Address"},
    q_f1_28: {"question": "6. (5) เซิร์ฟเวอร์ที่อยู่ด้านบนสุดของลำดับชั้น DNS และมี 13 อินสแตนซ์ทั่วโลกสำหรับการแปลชื่อโดเมนและที่อยู่ IP เรียกว่าอะไร? ( 7-1インターネット.pdf p.18 )", "answer": "Root DNS Server"},
    q_f1_29: {"question": "6. (6) ในการแก้ไขชื่อ DNS วิธีการสืบค้นที่ไคลเอนต์จะส่งคำถามไปยัง DNS เซิร์ฟเวอร์ท้องถิ่น (resolver) ก่อนที่ resolver จะสืบค้นไปยัง Root DNS Server เรียกว่าอะไร? ( 7-1インターネット.pdf p.19 )", "answer": "Recursive Query (การสืบค้นแบบเรียกซ้ำ)"},

    q_f1_30: {
        "question": "7. (1) ต้นกำเนิดของอินเทอร์เน็ตถือว่าเป็น ( A ) ซึ่งได้รับการพัฒนาในสหรัฐอเมริกาในปี 1969 โดยเริ่มจากการวิจัยเครือข่ายแบบ ( B ) ซึ่งสามารถรักษาการสื่อสารไว้ได้แม้ว่าบางส่วนจะล้มเหลว ( 7-1インターネット.pdf p.7 )",
        "answer": "(A) ARPANET\n(B) Distributed (กระจายศูนย์)"
    },
    q_f1_31: {
        "question": "7. (2) ในชื่อโดเมน ส่วนที่อยู่ทางขวาสุดเรียกว่า Top Level Domain (TLD) ส่วนที่กำหนดโดยประเทศ เช่น `.jp` หรือ `.uk` เรียกว่า ( C ) และส่วนที่กำหนดโดยประเภท เช่น `.com` หรือ `.org` เรียกว่า ( D ) ( 7-1インターネット.pdf p.17 )",
        "answer": "(C) ccTLD (country code TLD)\n(D) gTLD (generic TLD)"
    },
    q_f1_32: {
        "question": "7. (3) เพื่อลดภาระการสอบถามบนเซิร์ฟเวอร์ DNS และการรับส่งข้อมูลในเครือข่าย กลไกในการจัดเก็บผลลัพธ์ของการแปลงชื่อเป็นระยะเวลาหนึ่งเรียกว่า ( E ) ( 7-1インターネット.pdf p.18 )",
        "answer": "(E) Caching (การแคช)"
    },
    q_f1_33: {
        "question": "7. (4) DHCP ไม่ได้กำหนดค่าเพียงที่อยู่ IP โดยอัตโนมัติเท่านั้น แต่ยังแจ้งให้ไคลเอนต์ทราบถึง ( F ) ซึ่งกำหนดขอบเขตของเครือข่าย, ( G ) ซึ่งเป็นที่อยู่ IP ของเราเตอร์ที่เป็นทางออกไปยังเครือข่ายอื่น, และที่อยู่ของ ( H ) สำหรับการแปลงชื่อ ( 7-1インターネット.pdf p.20 )",
        "answer": "(F) Subnet Mask\n(G) Default Gateway\n(H) DNS Server"
    },
    q_f1_34: {
        "question": "7. (5) โมเดลที่คอมพิวเตอร์ที่เชื่อมต่อ (peers) สื่อสารกันโดยตรงโดยไม่ต้องผ่านเซิร์ฟเวอร์เฉพาะ เรียกว่าโมเดล ( I ) โมเดลนี้มีลักษณะเด่นคือมีความ ( J ) (scalability) สูง เนื่องจากภาระงานไม่กระจุกตัวอยู่ที่เซิร์ฟเวอร์ ( 7-1インターネット.pdf p.10, p.12 )",
        "answer": "(I) P2P (Peer-to-Peer)\n(J) Scalability (ความสามารถในการปรับขนาด)"
    },
    q_f1_35: {
        "question": "8. (1) ในการส่งอีเมล โปรโตคอลที่ใช้สำหรับการส่งและส่งต่อคือ ( A ) ในขณะที่โปรโตคอลที่ใช้สำหรับการรับคือ ( B ) และ ( C ) โดยปกติ ( A ) จะใช้หมายเลขพอร์ต ( D ), ( B ) ใช้ ( E ), และ ( C ) ใช้ ( F ) ( 7-2メールサービス.pdf p.24, p.26, p.32, p.37 )",
        "answer": "(A) SMTP\n(B) POP3\n(C) IMAP\n(D) 25\n(E) 110\n(F) 143"
    },
    q_f1_36: {
        "question": "8. (2) เมื่อระบุเซิร์ฟเวอร์อีเมลปลายทางโดยใช้ DNS จะมีการอ้างอิงเรคคอร์ด ( G ) แทนการแก้ไขชื่อโฮสต์มาตรฐาน (A record) กลไกนี้จะเชื่อมโยงชื่อโดเมน (เช่น @kitakyu-u.ac.jp) กับชื่อเซิร์ฟเวอร์อีเมลจริง ( 7-2メールサービス.pdf p.26 )",
        "answer": "(G) MX (Mail eXchange)"
    },
    q_f1_37: {
        "question": "8. (3) อธิบายสั้นๆ ถึงความจำเป็นของ 'SMTP Authentication (SMTP-AUTH)' ในโปรโตคอล SMTP จากมุมมองของ **การป้องกันสแปม** ( 7-2メールサービス.pdf p.29, p.30 )",
        "answer": "เนื่องจาก SMTP แบบดั้งเดิมขาดการตรวจสอบผู้ใช้ ทำให้ใครๆ ก็สามารถส่งอีเมลได้อย่างอิสระ จึงจำเป็นต้องมีกลไกในการตรวจสอบผู้ใช้เมื่อส่งอีเมล เพื่อป้องกันการส่งต่อโดยไม่ได้รับอนุญาตจากบุคคลที่สาม (การใช้เป็นทางผ่านของสแปม)"
    },
    q_f1_38: {
        "question": "8. (4) อธิบายความแตกต่างด้านการทำงานระหว่างโปรโตคอลรับอีเมล POP3 และ IMAP จากมุมมองของ 'สถานที่จัดการอีเมล' และ 'การใช้งานบนอุปกรณ์หลายเครื่อง' ( 7-2メールサービス.pdf p.37 )",
        "answer": "POP3 ดาวน์โหลดอีเมลจากเซิร์ฟเวอร์ไปยังไคลเอนต์เพื่อจัดการ ทำให้การซิงโครไนซ์ข้ามอุปกรณ์หลายเครื่องเป็นเรื่องยาก ในทางกลับกัน IMAP จัดการอีเมลบนเซิร์ฟเวอร์ โดยไคลเอนต์จะเก็บเพียงแคชไว้ ทำให้สามารถเข้าถึงและจัดการกล่องจดหมายเดียวกันได้จากอุปกรณ์หลายเครื่อง"
    },
    q_f1_39: {
        "question": "8. (5) ในการตรวจสอบผู้ใช้ระหว่างการรับอีเมล ต่างจากการตรวจสอบสิทธิ์แบบ POP ที่ส่งรหัสผ่านเป็นข้อความธรรมดา วิธีการที่เพิ่มความปลอดภัยโดยการรวม **challenge string** ที่ส่งจากเซิร์ฟเวอร์เข้ากับรหัสผ่านเพื่อคำนวณค่าแฮช และส่งเฉพาะผลลัพธ์นั้น (response) เรียกว่าการตรวจสอบสิทธิ์แบบ ( H ) ( 7-2メールサービス.pdf p.36 )",
        "answer": "(H) APOP"
    },
    q_f1_40: {
        "question": "8. (6) ข้อมูลส่วนหัวของอีเมลประกอบด้วย ( I ) ระบุผู้ส่ง, ( J ) ระบุผู้รับ, และ ( K ) ระบุหัวเรื่อง นอกจากนี้ เส้นทางการจัดส่งจริง (ข้อมูลของเซิร์ฟเวอร์อีเมลที่ผ่าน) จะถูกบันทึกไว้ในฟิลด์ ( L ) ซึ่งช่วยให้สามารถติดตามที่มาของอีเมลได้ ( 7-2メールサービス.pdf p.41, p.42 )",
        "answer": "(I) From\n(J) To\n(K) Subject\n(L) Received"
    },

    q_f1_41: {
        "question": "9. (1) WWW (World Wide Web) คือระบบไฮเปอร์เท็กซ์บนอินเทอร์เน็ตที่ประกอบด้วย 3 องค์ประกอบ: ( A ) ซึ่งระบุตำแหน่งของทรัพยากร, ( B ) ซึ่งเป็นภาษาอธิบายเอกสาร, และ ( C ) ซึ่งเป็นโปรโตคอลการสื่อสาร ( 7-3Web サービス.pdf p.44 )",
        "answer": "(A) URL (หรือ URI)\n(B) HTML\n(C) HTTP"
    },
    q_f1_42: {
        "question": "9. (2) ข้อความที่เว็บเบราว์เซอร์ (ไคลเอนต์) ส่งไปยังเว็บเซิร์ฟเวอร์เพื่อบอกว่า 'ขอหน้านี้หน่อย' เรียกว่า ( D ) และข้อความที่เซิร์ฟเวอร์ส่งกลับมาเรียกว่า ( E ) สิ่งเหล่านี้ประกอบด้วย 3 ส่วน: บรรทัด ( F ), ส่วนหัว, และ ( G ) ( 7-3Web サービス.pdf p.50, p.51 )",
        "answer": "(D) Request (HTTP Request)\n(E) Response (HTTP Response)\n(F) Status (หรือ Request/Response)\n(G) Message Body (ตัวเนื้อหาข้อความ)"
    },
    q_f1_43: {
        "question": "9. (3) บรรทัด ( F ) ของ HTTP request จะมีเมธอดอยู่ เมธอดในการดึงหน้าเว็บคือ ( H ), ดึงเฉพาะข้อมูลส่วนหัวคือ ( I ), และส่งข้อมูลฟอร์มคือ ( J ) ( 7-3Web サービス.pdf p.52 )",
        "answer": "(H) GET\n(I) HEAD\n(J) POST"
    },
    q_f1_44: {
        "question": "9. (4) บรรทัด ( F ) ของ HTTP response จะมีรหัสสถานะ รหัสที่ระบุว่าคำขอสำเร็จคือ ( K ), หากไม่พบหน้าคือ ( L ), หากถูกปฏิเสธการเข้าถึงคือ ( M ), และข้อผิดพลาดภายในเซิร์ฟเวอร์จะอยู่ในช่วง 500 ( 7-3Web サービス.pdf p.53 )",
        "answer": "(K) 200 (OK)\n(L) 404 (Not Found)\n(M) 403 (Forbidden)"
    },
    q_f1_45: {
        "question": "9. (5) ใน HTTP ซึ่งเป็นโปรโตคอลแบบไร้สถานะ (stateless) ข้อมูลข้อความขนาดเล็กที่เซิร์ฟเวอร์บันทึกไว้ในเบราว์เซอร์เพื่อรักษา 'สถานะ' เช่น ตะกร้าสินค้าหรือสถานะการเข้าสู่ระบบ เรียกว่า ( N ) ( 7-3Web サービス.pdf p.55 )",
        "answer": "(N) Cookie (คุกกี้)"
    },
    q_f1_46: {
        "question": "9. (6) กลไกในการสร้างหน้าเว็บแบบไดนามิกโดยการเรียกใช้โปรแกรมฝั่งเซิร์ฟเวอร์และส่งคืนผลลัพธ์เรียกว่า ( O ) ในทางกลับกัน โปรแกรมที่ทำงานฝั่งไคลเอนต์ (เบราว์เซอร์) โดยใช้ JavaScript ฯลฯ บางครั้งเรียกว่าแอปพลิเคชัน ( P ) ( 7-3Web サービス.pdf p.45 )",
        "answer": "(O) CGI (Common Gateway Interface)\n(P) Helper (หรือ Client-side)"
    },
    q_f1_47: {
        "question": "10. (1) ในฐานะคำจำกัดความของความปลอดภัยของข้อมูล จงตอบคุณสมบัติ 3 ประการของข้อมูล (CIA) ที่ต้องรักษาไว้ ได้แก่ ( A ) หมายถึงเฉพาะผู้ที่มีสิทธิ์เท่านั้นที่สามารถเข้าถึงได้, ( B ) หมายถึงเนื้อหามีความถูกต้องและสมบูรณ์, และ ( C ) หมายถึงสามารถเข้าถึงได้เมื่อต้องการ ( 8-1ネットワークセキュリティ.pdf p.7, p.18 )",
        "answer": "(A) Confidentiality (ความลับ)\n(B) Integrity (ความสมบูรณ์)\n(C) Availability (ความพร้อมใช้งาน)"
    },
    q_f1_48: {
        "question": "10. (2) ภัยคุกคามต่อความปลอดภัย ได้แก่ ( D ) ซึ่งคุกคามความลับ, ( E ) ซึ่งคุกคามความสมบูรณ์, และ ( F ) ซึ่งคุกคามความพร้อมใช้งาน ( 8-1ネットワークセキュリティ.pdf p.8 )",
        "answer": "(D) Eavesdropping (การดักฟัง หรือ Unauthorized Access)\n(E) Tampering (การปลอมแปลงแก้ไข)\n(F) Denial of Service (DoS) attack"
    },
    q_f1_49: {
        "question": "10. (3) การโจมตีที่ละเมิดความพร้อมใช้งานของบริการโดยการส่งแพ็คเก็ตจำนวนมหาศาลเพื่อทำให้เซิร์ฟเวอร์ล่มเรียกว่าการโจมตีแบบ ( G ) นอกจากนี้ การโจมตีที่คอมพิวเตอร์หลายเครื่องร่วมมือกันโจมตีพร้อมกันเรียกว่าการโจมตีแบบ ( H ) ( 8-1ネットワークセキュリティ.pdf p.12 )",
        "answer": "(G) DoS (Denial of Service)\n(H) DDoS (Distributed DoS)"
    },
    q_f1_50: {
        "question": "10. (4) อธิบายการโจมตีที่มุ่งเป้าไปที่ช่องโหว่ในเว็บแอปพลิเคชัน การโจมตีที่จัดการฐานข้อมูลอย่างผิดกฎหมายโดยการส่งค่าที่ผิดกฎหมายในอินพุตที่สร้างคำสั่งฐานข้อมูลเรียกว่า ( I ) ( 8-1ネットワークセキュリティ.pdf p.14 )",
        "answer": "(I) SQL Injection (SQL อินเจคชัน)"
    },
    q_f1_51: {
        "question": "10. (5) ในทำนองเดียวกัน การโจมตีที่ใช้ประโยชน์จากช่องโหว่ของเว็บไซต์เพื่อดำเนินการสคริปต์ที่เป็นอันตรายบนเบราว์เซอร์ของผู้ชมเรียกว่า ( J ) สิ่งนี้ช่วยให้สามารถรับข้อมูล Cookie โดยไม่ได้รับอนุญาต ฯลฯ ( 8-1ネットワークセキュリティ.pdf p.15 )",
        "answer": "(J) Cross Site Scripting (XSS)"
    },
    q_f1_52: {
        "question": "10. (6) วิธีการโจมตีที่ขโมยข้อมูลโดยอาศัยช่องว่างทางจิตวิทยาหรือความผิดพลาดทางพฤติกรรมของมนุษย์ (เช่น การจัดการรหัสผ่านที่ไม่ดี) แทนที่จะเป็นช่องโหว่ทางเทคนิคเรียกว่า ( K ) ( 8-1ネットワークセキュリティ.pdf p.13 )",
        "answer": "(K) Social Engineering (วิศวกรรมสังคม)"
    },
    q_f1_53: {
        "question": "10. (7) การโจมตีที่ได้รับข้อมูลภายในโดยการสังเกตสภาพการทำงานของอุปกรณ์ (เช่น ความผันผวนของพลังงานหรือคลื่นแม่เหล็กไฟฟ้าที่รั่วไหล) โดยใช้วิธีการทางกายภาพเรียกว่าการโจมตีแบบ ( L ) หรือการโจมตีแบบ ( M ) ( 8-1ネットワークセキュリティ.pdf p.16 )",
        "answer": "(L) Side Channel (ไซด์แชนเนล)\n(M) Implementation (การนำไปใช้งาน/อิมพลีเมนเตชัน)"
    },
    q_f1_54: {
        "question": "11. (1) การเข้ารหัสเป็นเทคโนโลยีพื้นฐานสำหรับการรับรอง ( A ) และ ( B ) ในความปลอดภัยของข้อมูล การแปลงข้อความธรรมดาเป็นข้อความที่เข้ารหัสเรียกว่า ( C ) และการกู้คืนข้อความที่เข้ารหัสกลับเป็นข้อความธรรมดาเรียกว่า ( D ) ( 8-2 暗号.pdf p.22 )",
        "answer": "(A) Confidentiality (ความลับ)\n(B) Integrity (ความสมบูรณ์)\n(C) Encryption (การเข้ารหัส)\n(D) Decryption (การถอดรหัส)"
    },
    q_f1_55: {
        "question": "11. (2) การเข้ารหัสสมัยใหม่ใช้หลักการของ ( F ) ซึ่งระบุว่า 'อัลกอริธึมเป็นสาธารณะ และมีเพียง ( E ) เท่านั้นที่ถูกเก็บเป็นความลับ' สิ่งนี้ช่วยให้ความปลอดภัยของอัลกอริธึมได้รับการตรวจสอบทั่วโลก ( 8-2 暗号.pdf p.24 )",
        "answer": "(E) Key (คีย์/กุญแจ)\n(F) Kerckhoffs (เคอร์คอฟ)"
    },
    q_f1_56: {
        "question": "11. (3) การเข้ารหัสแบบกุญแจสมมาตรใช้คีย์ ( G ) สำหรับการเข้ารหัสและถอดรหัส มีข้อดีคือการประมวลผล ( H ) แต่มีปัญหาเรื่อง ( I ) เนื่องจากต้องใช้คีย์ที่แตกต่างกันสำหรับคู่สนทนาแต่ละราย อัลกอริธึมที่เป็นตัวแทนคือ ( J ) ( 8-2 暗号.pdf p.25, p.26 )",
        "answer": "(G) Same (เดียวกัน)\n(H) Fast (เร็ว)\n(I) Key Distribution (การแจกจ่ายคีย์)\n(J) AES"
    },
    q_f1_57: {
        "question": "11. (4) การเข้ารหัสแบบกุญแจสาธารณะใช้คีย์ ( K ) ที่ใครๆ ก็ใช้ได้ในการเข้ารหัส และคีย์ ( L ) ที่เจ้าของเท่านั้นที่มีในการถอดรหัส การประมวลผล ( M ) แต่การแจกจ่ายคีย์นั้นง่าย อัลกอริธึมที่เป็นตัวแทน ( N ) อาศัยความยากของการแยกตัวประกอบจำนวนเฉพาะเพื่อความปลอดภัย ( 8-2 暗号.pdf p.26, p.27 )",
        "answer": "(K) Public (สาธารณะ)\n(L) Private (ส่วนตัว)\n(M) Slow (ช้า)\n(N) RSA"
    },
    q_f1_58: {
        "question": "11. (5) ค่าความยาวคงที่ที่สร้างจากข้อมูลต้นฉบับเพื่อตรวจสอบความสมบูรณ์ของข้อมูลเรียกว่า ( O ) ( P ) ใช้สิ่งนี้โดยผู้ส่งจะเข้ารหัส (ลงชื่อ) ด้วยคีย์ ( Q ) ของตน และผู้รับจะถอดรหัส (ตรวจสอบ) ด้วยคีย์ ( R ) ของผู้ส่ง เพื่อทำการยืนยันตัวตนและตรวจจับการปลอมแปลง ( 8-2 暗号.pdf p.29 )",
        "answer": "(O) Hash Value (ค่าแฮช)\n(P) Digital Signature (ลายเซ็นดิจิทัล)\n(Q) Private (ส่วนตัว)\n(R) Public (สาธารณะ)"
    },
    q_f1_59: {
        "question": "11. (6) ข้อมูลที่ออกโดยองค์กรบุคคลที่สามที่เชื่อถือได้ ( S ) เพื่อพิสูจน์ว่าคีย์สาธารณะเป็นของเจ้าของที่ถูกต้องเรียกว่า ( T ) โครงสร้างพื้นฐานความปลอดภัยทางสังคมที่ใช้สิ่งนี้เรียกว่า ( U ) ( 8-2 暗号.pdf p.30 )",
        "answer": "(S) Certificate Authority (CA)\n(T) Digital Certificate (ใบรับรองดิจิทัล)\n(U) PKI (Public Key Infrastructure)"
    },
    q_f1_60: {
        "question": "11. (7) การสื่อสารที่ปลอดภัยจริง (เช่น SSL/TLS) ใช้วิธีการแบบไฮบริดเพื่อแก้ปัญหาความเร็วในการประมวลผล โดยใช้การเข้ารหัสแบบ ( V ) สำหรับการแลกเปลี่ยนคีย์และการตรวจสอบสิทธิ์ และใช้การเข้ารหัสแบบ ( W ) ซึ่งมีความเร็วสูงสำหรับการเข้ารหัสข้อมูลจำนวนมาก ( 8-2 暗号.pdf p.31 )",
        "answer": "(V) Public Key (กุญแจสาธารณะ)\n(W) Symmetric Key (กุญแจสมมาตร)"
    },
    q_f1_61: {
        "question": "13. (1) คุณสมบัติที่การสื่อสารที่ปลอดภัยต้องมี ได้แก่ ( A ) เพื่อป้องกันการดักฟัง, ( B ) เพื่อป้องกันการปลอมแปลงตัวตน, ( C ) เพื่อป้องกันการแก้ไขข้อมูล, และ ( D ) เพื่อพิสูจน์ว่าข้อเท็จจริงไม่สามารถปฏิเสธได้ ( 8-3セキュア通信プロトコル.pdf p.36, p.42 )",
        "answer": "(A) Confidentiality (ความลับ)\n(B) Authentication (การตรวจสอบสิทธิ์)\n(C) Message Integrity (ความสมบูรณ์ของข้อความ)\n(D) Non-repudiation (การห้ามปฏิเสธความรับผิด)"
    },
    q_f1_62: {
        "question": "13. (2) โปรโตคอลการสื่อสารที่ปลอดภัยซึ่งทำงานที่ Transport Layer (Layer 4) เรียกว่า ( E ) เมื่อนำไปใช้กับการสื่อสารผ่านเว็บเบราว์เซอร์ (HTTP) จะเรียกว่า ( F ) และใช้พอร์ตหมายเลข ( G ) ( 8-3セキュア通信プロトコル.pdf p.37 )",
        "answer": "(E) SSL/TLS\n(F) HTTPS\n(G) 443"
    },
    q_f1_63: {
        "question": "13. (3) SSL/TLS ใช้กลไกแบบไฮบริดเพื่อให้มั่นใจถึงประสิทธิภาพการสื่อสาร โดยใช้การเข้ารหัสแบบ ( H ) สำหรับการแลกเปลี่ยนคีย์เซสชัน (คีย์สมมาตร) และใช้การเข้ารหัสแบบ ( I ) ที่รวดเร็วสำหรับการเข้ารหัสข้อมูลจริง นอกจากนี้ยังใช้ ( J ) สำหรับการตรวจจับการปลอมแปลงแก้ไข ( 8-3セキュア通信プロトコル.pdf p.38 )",
        "answer": "(H) Public Key (กุญแจสาธารณะ)\n(I) Symmetric Key (กุญแจสมมาตร)\n(J) Message Authentication Code (MAC)"
    },
    q_f1_64: {
        "question": "13. (4) โปรโตคอลการสื่อสารที่ปลอดภัยซึ่งทำงานที่ Internet Layer (Layer 3) เรียกว่า ( K ) มักใช้ในการสร้าง ( L ) สำหรับการเชื่อมต่อระหว่างเครือข่าย ( 8-3セキュア通信プロトコル.pdf p.40, p.42 )",
        "answer": "(K) IPsec\n(L) VPN (Virtual Private Network)"
    },
    q_f1_65: {
        "question": "13. (5) ในโหมดการทำงานของ IPsec โหมดที่เข้ารหัสเฉพาะส่วนข้อมูล (payload) และใช้สำหรับการสื่อสารระหว่างโฮสต์เรียกว่าโหมด ( M ) ในขณะที่โหมดที่เข้ารหัสและห่อหุ้ม (encapsulate) แพ็คเก็ต IP ทั้งหมดและใช้สำหรับการสื่อสารระหว่างเกตเวย์เรียกว่าโหมด ( N ) ( 8-3セキュア通信プロトコル.pdf p.40 )",
        "answer": "(M) Transport (ทรานสปอร์ต)\n(N) Tunnel (อุโมงค์)"
    },
    q_f1_66: {
        "question": "13. (6) ในบรรดาโปรโตคอลที่ประกอบกันเป็น IPsec โปรโตคอลที่ให้เฉพาะการตรวจสอบสิทธิ์และการป้องกันการปลอมแปลงแก้ไขเรียกว่า ( O ) และโปรโตคอลที่ให้ฟังก์ชันการเข้ารหัสข้อมูลเพิ่มเติมด้วยเรียกว่า ( P ) ( 8-3セキュア通信プロトコル.pdf p.40 )",
        "answer": "(O) AH (Authentication Header)\n(P) ESP (Encapsulated Security Payload)"
    },

    q_f1_67: {
        "question": "14. (1) อุปกรณ์ที่ป้องกันการบุกรุกของแพ็คเก็ตที่ไม่ได้รับอนุญาตจากภายนอกเรียกว่า ( A ) วิธีการกรองแพ็คเก็ตได้แก่ การกรองแบบ ( B ) ซึ่งบล็อกตามที่อยู่ IP หรือหมายเลขพอร์ตที่ระบุ และการกรองแบบ ( C ) ซึ่งอนุญาตเฉพาะแพ็คเก็ตตอบกลับจากการสื่อสารที่เริ่มต้นจากภายในเท่านั้น ( 8-4防御技術.pdf p.45 )",
        "answer": "(A) Firewall (ไฟร์วอลล์)\n(B) Static (แบบคงที่)\n(C) Dynamic (แบบไดนามิก)"
    },
    q_f1_68: {
        "question": "14. (2) พื้นที่ที่อยู่ระหว่างอินเทอร์เน็ตและเครือข่ายภายใน ซึ่งใช้สำหรับวางเซิร์ฟเวอร์ที่ต้องเปิดเผยต่อสาธารณะ (เช่น เว็บเซิร์ฟเวอร์และเมลเซิร์ฟเวอร์) เรียกว่า ( D ) ( 8-4防御技術.pdf p.46 )",
        "answer": "(D) DMZ (DeMilitarized Zone - เขตปลอดทหาร)"
    },
    q_f1_69: {
        "question": "14. (3) ระบบที่วิเคราะห์เนื้อหาแพ็คเก็ตและบันทึก (log) เพื่อตรวจจับและรายงานสัญญาณของการโจมตี เช่น การโจมตีแบบ DoS หรือการสแกนพอร์ต เรียกว่า ( E ) ในขณะที่ระบบที่ไม่เพียงแค่ตรวจจับแต่ยังดำเนินมาตรการป้องกัน เช่น การบล็อก เรียกว่า ( F ) ( 8-4防御技術.pdf p.47 )",
        "answer": "(E) IDS (Intrusion Detection System)\n(F) IPS (Intrusion Prevention System)"
    },
    q_f1_70: {
        "question": "14. (4) เซิร์ฟเวอร์รีเลย์ที่เข้าถึงอินเทอร์เน็ตในนามของไคลเอนต์ภายในเรียกว่า ( G ) ช่วยเพิ่มความปลอดภัยผ่านการแปลงที่อยู่และการกรองข้อมูลที่เป็นอันตราย และปรับปรุงประสิทธิภาพการสื่อสารด้วยฟังก์ชัน ( H ) ที่บันทึกข้อมูลที่เคยเข้าถึงไว้ ( 8-4防御技術.pdf p.48 )",
        "answer": "(G) Proxy (พร็อกซี)\n(H) Cache (แคช)"
    },
    q_f1_71: {
        "question": "14. (5) กลไกที่เชื่อมต่อพีซีที่นำเข้ามาในบริษัทเข้ากับเครือข่ายตรวจสอบเฉพาะเพื่อตรวจสอบสถานะความปลอดภัย (การป้องกันไวรัส ฯลฯ) ก่อนที่จะเชื่อมต่อกับ LAN ภายในเรียกว่า ( I ) ( 8-4防御技術.pdf p.49 )",
        "answer": "(I) Quarantine Network (เครือข่ายกักกัน)"
    },
    q_f1_72: {
        "question": "14. (6) เทคโนโลยีหรือกลไกในการรวบรวม วิเคราะห์ และเก็บรักษาข้อมูล (เช่น บันทึกและแพ็คเก็ตการสื่อสาร) ที่จำเป็นสำหรับการหาสาเหตุทางกฎหมายเมื่อเกิดเหตุการณ์ขึ้นเรียกว่า ( J ) ( 8-4防御技術.pdf p.49 )",
        "answer": "(J) Digital Forensics (นิติวิทยาศาสตร์ดิจิทัล)"
    },

    q_f1_73: {
        "question": "15. (1) เปรียบเทียบโมเดล Client-Server และ P2P ในหัวข้อ: รูปแบบบริการ (รวมศูนย์/กระจาย), ความทนทาน (สูง/ต่ำ), และการขยายตัว (สูง/ต่ำ)",
        "answer": "Client-Server: (a) รวมศูนย์, (d) ต่ำ, (f) ต่ำ\nP2P: (b) กระจายศูนย์อิสระ, (c) สูง, (e) สูง"
    },
    q_f1_74: {
        "question": "15. (2) บทบาทหลักของ DNS คือการแปลง ( a ) เป็น ( b ) ซึ่งเรียกว่า ( c )",
        "answer": "(a) ชื่อโดเมน (Domain Name)\n(b) ที่อยู่ IP (IP Address)\n(c) การแก้ไขชื่อ (Name Resolution)"
    },
    q_f1_75: {
        "question": "15. (3) โปรโตคอลใดที่ตั้งค่าการสื่อสารอัตโนมัติเมื่อเชื่อมต่อโดยใช้ฟังก์ชัน ( a )? โปรโตคอลคือ ( b )",
        "answer": "(a) บรอดคาสต์ (Broadcast)\n(b) DHCP"
    },
    q_f1_76: {
        "question": "15. (4) ระบุโปรโตคอลที่ใช้ในการส่งอีเมล:\n1. ไคลเอนต์ -> เซิร์ฟเวอร์ส่ง\n2. เซิร์ฟเวอร์ -> เซิร์ฟเวอร์\n3. เซิร์ฟเวอร์รับ -> ไคลเอนต์\n4. เบราว์เซอร์ <-> เว็บเมล",
        "answer": "1. SMTP\n2. SMTP\n3. POP3 หรือ IMAP\n4. HTTP"
    },
    q_f1_77: {
        "question": "15. (5) อธิบายความแตกต่างของฟังก์ชันระหว่าง POP3 และ IMAP",
        "answer": "POP3 เป็นโปรโตคอลที่เรียบง่ายซึ่งมีพื้นฐานมาจากการดาวน์โหลดและประมวลผลเมล\nIMAP เป็นโปรโตคอลที่มีฟังก์ชันการทำงานสูงซึ่งมีพื้นฐานมาจากการจัดการเมลบนเซิร์ฟเวอร์ ทำให้สามารถเข้าถึงได้จากไคลเอนต์หลายเครื่อง"
    },
   
    q_f1_78: {
        "question": "15. (6) TCP เป็นโปรโตคอลแบบ ( a ) ผู้รับส่งกลับหมายเลข ( b ) เพื่อยืนยัน และใช้หมายเลข ( c ) สำหรับการควบคุมลำดับ",
        "answer": "(a) Connection-oriented\n(b) Acknowledgment (ACK)\n(c) Sequence"
    },
    q_f1_79: {
        "question": "15. (7) อธิบายความแตกต่างระหว่าง Flow Control และ Congestion Control ให้เข้าใจถึงวัตถุประสงค์และวิธีการควบคุม",
        "answer": "ใน Flow Control อัตราการส่งข้อมูลจะถูกปรับตามขนาดบัฟเฟอร์ที่รับได้ซึ่งแจ้งโดยโฮสต์ผู้รับ เพื่อไม่ให้เกินความสามารถในการประมวลผลของโฮสต์ผู้รับ\nในทางกลับกัน ใน Congestion Control อัตราการส่งข้อมูลจะถูกปรับตามสถานะความคับคั่งของเครือข่าย เพื่อไม่ให้เกินความสามารถในการประมวลผลของเครือข่าย"
    },
    q_f1_80: {
        "question": "15. (8) การควบคุมความคับคั่ง TCP: ( a ) เพิ่มขนาดหน้าต่างแบบทวีคูณ, ( b ) เพิ่มแบบเส้นตรงหลังจากข้ามขีดจำกัด",
        "answer": "(a) Slow Start\n(b) Congestion Avoidance"
    },
    q_f1_80: {
        "question": "15. (8) อธิบายวิธีการควบคุม Congestion Window อย่างเป็นรูปธรรม",
        "answer": "ในเฟส Slow Start จะเพิ่มขึ้นแบบทวีคูณ (เพิ่มอัตราการส่งอย่างรวดเร็ว) หลังจากเกินขีดจำกัด Slow Start จะย้ายไปสู่เฟส Congestion Avoidance และเพิ่มขึ้นแบบเส้นตรง (เพิ่มอัตราการส่งอย่างช้าๆ) เพื่อหาขนาดหน้าต่างความคับคั่งที่เหมาะสม"
    },
    q_f1_82: {
        "question": "15. (10) นิยามองค์ประกอบ 3 ประการของความปลอดภัยข้อมูล (CIA)",
        "answer": "Confidentiality (เข้าถึงได้เฉพาะผู้ได้รับอนุญาต), Integrity (ข้อมูลถูกต้องครบถ้วน), Availability (ใช้งานได้เมื่อต้องการ)"
    },
    q_f1_83: {
        "question": "15. (11) (1) SSL/TLS อยู่ที่เลเยอร์ ( a ) ป้องกันการดักฟังและ ( b ) (2) IPsec อยู่ที่เลเยอร์ ( c ); โหมด Transport เข้ารหัส ( d ), โหมด Tunnel เข้ารหัส ( e )",
        "answer": "(1) (a) Transport, (b) การปลอมแปลงแก้ไข (Tampering)\n(2) (c) Internet, (d) Payload (ข้อมูล), (e) แพ็คเก็ต IP ทั้งหมด"
    },
    q_f1_84: {
        "question": "15. (12) เติมคำในช่องว่างสำหรับ SSL/TLS Handshake:\nii. ตรวจสอบใบรับรองโดยใช้ ( a )\niii. เข้ารหัสคีย์เซสชันโดยใช้ ( b )\niv. เซิร์ฟเวอร์ถอดรหัสโดยใช้ ( c )",
        "answer": "(a) คีย์สาธารณะของ CA\n(b) คีย์สาธารณะของเซิร์ฟเวอร์\n(c) คีย์ส่วนตัวของเซิร์ฟเวอร์"
    },
    q_f1_85: {
        "question": "15. (13) อธิบายสั้นๆ เกี่ยวกับ DMZ, IDS vs IPS, และประเภทของ Packet Filtering",
        "answer": "DMZ: พื้นที่เซิร์ฟเวอร์สาธารณะ\nIDS: ตรวจจับ/แจ้งเตือน, IPS: ตรวจจับ/ป้องกัน\nFiltering: Static, Dynamic, Stateful"
    },
    q_f1_86: {
        "question": "16. (1) [คาดการณ์] WWW ใช้โปรโตคอล ( a ) เนื่องจาก ( a ) เป็นแบบ stateless จึงใช้ ( b ) เพื่อรักษาสถานะ เมธอดที่ไคลเอนต์ใช้ส่งข้อมูลคือ ( c )",
        "answer": "(a) HTTP\n(b) Cookie (คุกกี้)\n(c) POST"
    },
    q_f1_87: {
        "question": "16. (2) [คาดการณ์] การเข้ารหัสด้วยคีย์เดียวกันคือ ( a ) มีข้อดีคือ ( b ) แต่มีปัญหาเรื่อง ( c ) วิธีที่ใช้คีย์คู่คือ ( d ) ตัวอย่างอัลกอริธึมคือ ( e )",
        "answer": "(a) การเข้ารหัสแบบกุญแจสมมาตร\n(b) เร็ว\n(c) การแจกจ่ายคีย์\n(d) การเข้ารหัสแบบกุญแจสาธารณะ\n(e) RSA"
    },
    q_f1_88: {
        "question": "16. (3) [คาดการณ์] การแทรกอินพุตที่ผิดกฎหมายลงในคำสั่ง DB คือ ( a ) การฝังสคริปต์ที่เป็นอันตรายในหน้าเว็บคือ ( b ) การส่งแพ็คเก็ตจำนวนมากเพื่อขัดขวางบริการคือ ( c )",
        "answer": "(a) SQL Injection\n(b) Cross Site Scripting (XSS)\n(c) DoS Attack"
    },
    q_f1_89: {
        "question": "16. (4) [คาดการณ์] อธิบายความแตกต่างระหว่าง Static Filtering, Dynamic Filtering และ Stateful Inspection ในไฟร์วอลล์",
        "answer": "Static: ตัดสินจากกฎคงที่ (IP/Port)\nDynamic: อนุญาตเฉพาะแพ็คเก็ตตอบกลับ\nStateful: ตรวจสอบลำดับโปรโตคอลและบริบทการสื่อสาร"
    },
    q_f1_90: {
        "question": "16. (5) [คาดการณ์] ในลายเซ็นดิจิทัล ใครเข้ารหัส/ถอดรหัสด้วยคีย์ใด? และตรวจสอบอะไรได้บ้าง?",
        "answer": "เข้ารหัส: ผู้ส่งใช้คีย์ส่วนตัวของผู้ส่ง\nถอดรหัส: ผู้รับใช้คีย์สาธารณะของผู้ส่ง\nตรวจสอบ: ตัวตนผู้ส่ง (Authentication) และความสมบูรณ์ (Integrity)"
    },
    q_f1_91: {
        "question": "16. (6) [คาดการณ์] อธิบายความแตกต่างระหว่าง IDS และ IPS สั้นๆ",
        "answer": "IDS: ตรวจจับและแจ้งเตือน (มักไม่บล็อก)\nIPS: ตรวจจับและบล็อก (ป้องกัน)"
    },
    q_f1_92: {
        "question": "17. (1) [Ex4-1] องค์ประกอบ 3 ประการของความปลอดภัยข้อมูลคือ ( a ) (เข้าถึงได้เฉพาะผู้มีสิทธิ์), ( b ) (ข้อมูลถูกต้องครบถ้วน), และ ( c ) (เข้าถึงได้เมื่อต้องการ) ( 演習課題4-解答.pdf p.1 )",
        "answer": "(a) Confidentiality (ความลับ)\n(b) Integrity (ความสมบูรณ์)\n(c) Availability (ความพร้อมใช้งาน)"
    },
    q_f1_93: {
        "question": "17. (2) [Ex4-1] แม้จะใช้การเข้ารหัสที่ปลอดภัยทางคณิตศาสตร์ แต่คีย์อาจถูกขโมยโดย ( d ) ( 演習課題4-解答.pdf p.1 )",
        "answer": "(d) Implementation Attack (การโจมตีการนำไปใช้งาน / Side Channel)"
    },
    q_f1_94: {
        "question": "17. (3) [Ex4-1] ในการเข้ารหัสแบบกุญแจสมมาตร จะใช้ ( e ) สำหรับทั้งสองคีย์ ดังนั้นจึงจำเป็นต้อง ( f ) ระหว่างผู้ใช้ล่วงหน้า ( 演習課題4-解答.pdf p.1 )",
        "answer": "(e) Common Key (คีย์ร่วม/คีย์สมมาตร)\n(f) Share (แบ่งปัน/แจกจ่าย)"
    },
    q_f1_95: {
        "question": "17. (4) [Ex4-2] ในการเข้ารหัสแบบกุญแจสาธารณะ เมื่อ 'เข้ารหัส' ข้อความ (เพื่อความลับ) ให้ใช้ ( a ) ในการเข้ารหัส และ ( b ) ในการถอดรหัส ( 演習課題4-解答.pdf p.1 )",
        "answer": "(a) คีย์สาธารณะของผู้รับ\n(b) คีย์ส่วนตัวของผู้รับ"
    },
    q_f1_96: {
        "question": "17. (5) [Ex4-2] เมื่อทำ 'ลายเซ็นดิจิทัล' (เพื่อยืนยันตัวตน) ให้เข้ารหัสค่าแฮชโดยใช้ ( c ) ผู้รับจะถอดรหัสโดยใช้ ( d ) เพื่อตรวจสอบ ( 演習課題4-解答.pdf p.1 )",
        "answer": "(c) คีย์ส่วนตัวของผู้ส่ง\n(d) คีย์สาธารณะของผู้ส่ง"
    },
    q_f1_97: {
        "question": "17. (6) [Ex4-3] เติมคำในช่องว่างสำหรับ SSL/TLS:\n(1) เซิร์ฟเวอร์ส่ง ( a ) และใบรับรอง\n(2) ไคลเอนต์ตรวจสอบใบรับรองโดยใช้ ( b )\n(3) ไคลเอนต์เข้ารหัสข้อมูลคีย์เซสชันโดยใช้ ( c )\n(4) เซิร์ฟเวอร์ถอดรหัสโดยใช้ ( d ) ( 演習課題4-解答.pdf p.2 )",
        "answer": "(a) คีย์สาธารณะของเซิร์ฟเวอร์\n(b) คีย์สาธารณะของ CA (ผู้ออกใบรับรอง)\n(c) คีย์สาธารณะของเซิร์ฟเวอร์\n(d) คีย์ส่วนตัวของเซิร์ฟเวอร์"
    },
    q_f1_98: {
        "question": "17. (7) [Ex4-4] อธิบายหน้าที่ของ IDS (ระบบตรวจจับการบุกรุก) และ IPS (ระบบป้องกันการบุกรุก) ( 演習課題4-解答.pdf p.2 )",
        "answer": "IDS: วิเคราะห์แพ็คเก็ต/บันทึกเพื่อตรวจจับและแจ้งเตือนสัญญาณการโจมตี\nIPS: นอกเหนือจากฟังก์ชัน IDS แล้ว ยังสามารถดำเนินมาตรการต่างๆ เช่น การบล็อก ได้"
    },
    q_f1_99: {
        "question": "18. (1) [Physical Layer] จงอธิบายบทบาทของ Physical Layer",
        "answer": "ฟังก์ชันฮาร์ดแวร์ เช่น ระดับสัญญาณไฟฟ้าและรูปร่างของตัวเชื่อมต่อ"
    },
    q_f1_100: {
        "question": "18. (2) [Data Link Layer] จงอธิบายบทบาทของ Data Link Layer",
        "answer": "ฟังก์ชันการควบคุมสำหรับการส่งข้อมูลอย่างถูกต้องระหว่างโหนดการสื่อสารผ่านสื่อกลางการส่งข้อมูล"
    },
    q_f1_101: {
        "question": "18. (3) [Network Layer] จงอธิบายบทบาทของ Network Layer",
        "answer": "การเลือกเส้นทาง (Routing) ผ่านโหนดรีเลย์หลายตัว และฟังก์ชันการรีเลย์/ส่งต่อข้อมูล"
    },
    q_f1_102: {
        "question": "18. (4) [Transport Layer] จงอธิบายบทบาทของ Transport Layer",
        "answer": "การจัดการการเชื่อมต่อทางตรรกะ (Logical Connection) ระหว่างโฮสต์ผู้ส่งและผู้รับ และการรับประกันคุณภาพและความน่าเชื่อถือของการสื่อสาร"
    },
    q_f1_103: {
        "question": "18. (5) [Session Layer] จงอธิบายบทบาทของ Session Layer",
        "answer": "ฟังก์ชันการควบคุมการซิงโครไนซ์สำหรับการส่งข้อมูล เช่น การเริ่ม การคงไว้ และการสิ้นสุดการสื่อสารระหว่างแอปพลิเคชัน"
    },
    q_f1_104: {
        "question": "18. (6) [Presentation Layer] จงอธิบายบทบาทของ Presentation Layer",
        "answer": "ฟังก์ชันการควบคุมเกี่ยวกับรูปแบบการแสดงข้อมูล (เช่น การเข้ารหัส encoding, การเข้ารหัสลับ encryption ฯลฯ)"
    },
    q_f1_105: {
        "question": "18. (7) [Application Layer] จงอธิบายบทบาทของ Application Layer",
        "answer": "ฟังก์ชันการสื่อสารต่างๆ ตามบริการที่ระบุ (เช่น อีเมล)"
    }


    
}