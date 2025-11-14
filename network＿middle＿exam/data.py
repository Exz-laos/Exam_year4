# -*- coding: utf-8 -*-

# --- 試験問題の質問文を変数として定義 ---
# (注: Pythonの文字列ではバックスラッシュ(\)をエスケープする必要があるため、\\n や \\r と表記します)

# --- ネットワーク技術II - 中間試験（シミュレーション1）---



# --- ネットワーク技術II - 中間試験（シミュレーションA）---

q_A_1 = "1. (1) ブラウザで web ページを閲覧する際、Webサーバに「データちょうだい」と送るメッセージをなんというか。 ( `ネ技II-04reqとres.pdf`, p. 3 )"

q_A_2 = "1. (2) (1)はどのようなブロックで構成されているか、次の選択肢から4つ選び書きなさい。ただし、選択肢は（Status Line, Request Line, Message Body, Request Header, An Empry row, Response Header）である。 ( `ネ技II-05RESPONSEのテスト.pdf`, p. 19 )"

q_A_3 = "1. (3) (1)に対して、Webサーバがブラウザに「どーぞー」と返すメッセージをなんというか。 ( `ネ技II-04reqとres.pdf`, p. 3 )"

q_A_4 = "1. (4) (3)はどのようなブロックで構成されているか、(2)の選択肢から4つ選び書きなさい。 ( `ネ技II-05RESPONSEのテスト.pdf`, p. 7 )"

q_A_5 = """2. (1) ( `ネ技II-01python.pdf`, p. 31 )
<pre><code>a = [10, 20, 30, 40, 50]
n = a[2]
</code></pre>"""

q_A_6 = """2. (2) ( `ネ技II-01python.pdf`, p. 31 )
<pre><code>a = [10, 20, 30, 40, 50]
n = a[-1]
</code></pre>"""

q_A_7 = """2. (3) ( `ネ技II-01python.pdf`, p. 31 )
<pre><code>a = [10, 20, 30, 40, 50]
n = a[1:4]
</code></pre>"""

q_A_8 = """2. (4) ( `ネ技II-06REQUESTの受信.pdf`, p. 10 )
<pre><code>req_line = "GET /test.html HTTP/1.1"
parts = req_line.split(" ")
n = parts[1]
</code></pre>"""

q_A_9 = """2. (5) ( `ネ技II-06REQUESTの受信.pdf`, p. 14 )
<pre><code>headers = {}
headers["Content-Type"] = "text/html"
n = headers["Content-Type"]
</code></pre>"""

q_A_10 = """2. (6) ( `ネ技II-06REQUESTの受信.pdf`, p. 19 )
<pre><code>lang = "ja-JP,ja;q=0.9"
n = lang[:2]
</code></pre>"""

q_A_11 = """2. (7) ( `ネ技II-01python.pdf`, p. 30 )
<pre><code>n = len("test")
</code></pre>"""

q_A_12 = """2. (8) ( `ネ技II-01python.pdf`, p. 30 )
<pre><code>n = max(12, 20, 30)
</code></pre>"""

q_A_13 = """2. (9) ( `ネ技II-01python.pdf`, p. 32 )
<pre><code>b = []
b.append(3)
b.append("test")
n = b
</code></pre>"""

q_A_14 = """2. (10) ( `ネ技II-01python.pdf`, p. 35, p. 37 )
<pre><code>a = []
for i in range(3):
    a.append(i)
n = a
</code></pre>"""

q_A_15 = """3. 次の Web サーバから返ってくるステータスコードについて、次の表の(a)~ (d)に正しい数値または Reason-Phrase を入れなさい。 ( `ネ技II-07WebServer完成.pdf`, p. 11 )

| ステータスコード | Reason-Phrase | 意味 |
| :--- | :--- | :--- |
| 200 | ( a ) | 成功 |
| ( b ) | Not Found | ページが見つからない |
| 403 | Forbidden | ( c ) |
| 501 | ( d ) | (サーバが)実装していない |
"""

q_A_16 = """4. 次のソースコードはクライアントがサーバに接続してメッセージを送るものである。空欄\<\<a\>\>~\<\<d\>\>に適切なコードを埋めて完成させなさい。 ( `ネ技II-03-1client.pdf`, pp. 21-22 )
```python
import socket

HOST = "127.0.0.1"
PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.<< a >>((HOST, PORT)) # サーバに接続

msg = "hello from client"
try:
    sock.<< b >>(msg.<< c >>("UTF-8")) # メッセージを送信
except:
    print("sendall function failed.")

sock.<< d >>() # ソケットを閉じる

```"""
# q_A_16 = """5. 次のソースコードは、`webserver.py` で使用する、HTTP Requestを1行ずつ（CRLFまで）抽出する関数である。空欄 `<<a a>>` ~ `<<e e>>` に適切なコードを埋めて完成させなさい。
# (`ネ技II-05RESPONSEのテスト.pdf`, p.25)
# ```python
# import socket

# HOST = "127.0.0.1"
# PORT = 50000

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.<< a >>((HOST, PORT)) # サーバに接続

# msg = "hello from client"
# try:
#     sock.<< b >>(msg.<< c >>("UTF-8")) # メッセージを送信
# except:
#     print("sendall function failed.")

# sock.<< d >>() # ソケットを閉じる
# ```"""

q_A_17 = """5. 次のソースコードはサーバがクライアントからの接続を待って、接続開始後にメッセージを受信して表示するものである。空欄<<a>>~<<h>>に適切なコードを埋めて完成させなさい。 ( ネ技II-02server.pdf, p. 28; ネ技II-03-1client.pdf, p. 23 )
```python
import socket
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.<< a >>(("", 50000))  # IPとポートを登録
sock.<< b >>()            # 接続待ち受け状態にする

print("Waiting for a connection...")
sock_c, addr = sock.<< c >>() # 接続要求を受理

BUFSIZE = 1024
data = sock_c.<< d >>(<< e >>) # データを受信
if data:
    print(data.<< f >>("UTF-8")) # デコードして表示
sock_c.<< g >>() # 通信用ソケットを閉じる
sock.<< h >>() # 待ち受け用ソケットを閉じる

```"""




# --- ネットワーク技術II - 中間試験（シミュレーションB）---

q_B_1 = "1. (1) ネットワーク通信において、サービスや機能を利用する側をなんというか。 ( `ネ技II-02server.pdf`, p. 7 )"

q_B_2 = "1. (2) (1)の処理の基本的な流れとして、3つのステップを書きなさい。ただし、選択肢は(socket, bind, listen, connect, accept, close)である。 ( `ネ技II-03-1client.pdf`, p. 6 )"

q_B_3 = "1. (3) (1)に対して、サービスや機能を提供する側をなんというか。 ( `ネ技II-02server.pdf`, p. 7 )"

q_B_4 = "1. (4) (3)の待ち受け処理の基本的な流れとして、4つのステップを(2)の選択肢から選び、正しい順序で書きなさい。 ( `ネ技II-02server.pdf`, p. 10 )"

q_B_5 = """2. (1) ( `ネ技II-01python.pdf`, p. 15 )
<pre><code>n = 3**5
</code></pre>"""

q_B_6 = """2. (2) ( `ネ技II-01python.pdf`, p. 32 )
<pre><code>b = [1, 2]
b.extend([9, 8, 7])
n = b
</code></pre>"""

q_B_7 = """2. (3) ( `ネ技II-01python.pdf`, p. 33 )
<pre><code>a = (1, 2, 3, 4)
n = a[1:3]
</code></pre>"""

q_B_8 = """2. (4) ( `ネ技II-01python.pdf`, p. 30 )
<pre><code>n = min(12, 20, 30)
</code></pre>"""

q_B_9 = """2. (5) ( `ネ技II-01python.pdf`, p. 30 )
<pre><code>n = type(12)
</code></pre>"""

q_B_10 = """2. (6) ( `ネ技II-01python.pdf`, p. 18 )
<pre><code>n = 'apple' + 'pen'
</code></pre>"""

q_B_11 = """2. (7) ( `ネ技II-01python.pdf`, p. 31 )
<pre><code>a = [10, 20]
a[0] = 5
n = a
</code></pre>"""

q_B_12 = """2. (8) ( `ネ技II-06REQUESTの受信.pdf`, p. 10 )
<pre><code>req_line = "GET /test.html HTTP/1.1"
n = req_line.split(" ")[0]
</code></pre>"""

q_B_13 = """2. (9) ( `ネ技II-01python.pdf`, p. 31 )
<pre><code>a = "abcde"
n = a[2:]
</code></pre>"""

q_B_14 = """2. (10) ( `ネ技II-05RESPONSEのテスト.pdf`, p. 23 )
<pre><code>a = "abcde"
n = a.find("c")
</code></pre>"""

q_B_15 = """3. 次の Web サーバが送る Content-Type（MIME Type）について、次の表の(a)~ (d)に正しい文字列を入れなさい。 ( `ネ技II-07WebServer完成.pdf`, p. 17 )

| Content Type | 種類 | 拡張子 |
| :--- | :--- | :--- |
| ( a ) | テキストファイル | txt |
| text/html | ( b ) | htm, html |
| ( c ) | JPEGファイル | jpg, jpeg |
| image/png | PNGファイル | ( d ) |
"""

q_B_16 = """4. 次のソースコードはクライアントがサーバに接続してメッセージを受信するものである。空欄\<\<a\>\>~\<\<d\>\>に適切なコードを埋めて完成させなさい。 ( `ネ技II-03-1client.pdf`, pp. 9-12 )
```python
import socket

HOST = "127.0.0.1"
PORT = 50000
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.<< a >>)
sock.connect((HOST, << b >>)) # サーバに接続

data = sock.<< c >>(BUFSIZE) # データを受信
if data:
    print(data.<< d >>("UTF-8")) # デコードして表示

sock.close() # ソケットを閉じる

```"""

q_B_17 = """5. 次のソースコードはサーバが受信したHTTP Requestを1行ずつ解析する部分である。空欄<<a>>~<<g>>に適切なコードを埋めて完成させなさい。 ( ネ技II-06REQUESTの受信.pdf, pp. 5, 10, 13, 14 )
```python
import socket

# (extract_row関数は定義済みとする)
CRLF = "\r\n"
sock.<< a >>(1)  # 1秒でタイムアウト

try:
    one_row = extract_row(sock)
    http_req = [one_row.replace(CRLF, "")]

    while << b >>:  # one_row が空になるまで
        one_row = << c >>(sock) # 1行抽出
        http_req.append(one_row.replace(CRLF, ""))

except socket.timeout:
    print("受信ができない状況が1秒間続いた")

print(http_req)

req_line = http_req[<< d >>] # Request Lineを取得
req_method, req_uri, req_protocol = req_line.<< e >>(" ") # 3つに分割

req_headers = {}
for keyvalue in http_req[<< f >>:<< g >>]: # Header部分をループ
    key, value = keyvalue.split(": ")
    req_headers[key] = value

```"""










q_1 = "1. (1) ブラウザがWebページを閲覧する際、Webサーバに送信するデータを何と呼ぶか。 (`ネ技II-04reqとres.pdf`, p.3)"

q_2 = "1. (2) (1)に対して、Webサーバがブラウザに返信するデータを何と呼ぶか。 (`ネ技II-04reqとres.pdf`, p.3)"

q_3 = "1. (3) HTTP Responseの1行目（例: `HTTP/1.1 200 OK`）を何と呼ぶか。 (`ネ技II-05RESPONSEのテスト.pdf`, p.7)"

q_4 = "1. (4) Webサーバがブラウザに応答を返す際の、HTTP Responseの最小構成要素を3つ答えなさい。 (`ネ技II-05RESPONSEのテスト.pdf`, p.7)"

q_5 = "1. (5) Pythonのソケットプログラミングにおいて、`recv()`メソッドがデータを読み取るのは、OSが管理するどの領域からか。 (`ネ技II-03-2buffer.pdf`, p.11)"

q_6 = "1. (6) Pythonのソケットプログラミングにおいて、`sendall()`メソッドがデータを書き込むのは、OSが管理するどの領域からか。 (`ネ技II-03-2buffer.pdf`, p.12)"

q_7 = "1. (7) ネットワーク上で自分自身を示す特別なIPアドレス（ループバックアドレス）を答えなさい。 (`ネ技II-03-1client.pdf`, p.9)"

q_8 = "1. (8) ポート番号 0~65535 のうち、動的・プライベートポートとして自由に利用できる範囲を答えなさい。 (`ネ技II-02server.pdf`, p.14)"

q_9 = """2. (1) (`ネ技II-01python.pdf`, p.15)
<pre><code>n = 3 ** 5</code></pre>"""

q_10 = """2. (2) (ネ技II-01python.pdf, p.18)
<pre><code>a = 'apple'
b = 'pen'
n = a + b</code></pre>"""

q_11 = """2. (3) (ネ技II-01python.pdf, p.31)
<pre><code>a = [10, 20, 30, 40]
n = a[-1]</code></pre>"""

q_12 = """2. (4) (ネ技II-01python.pdf, p.31)
<pre><code>a = [10, 20, 30, 40]
n = a[1:3]</code></pre>"""

q_13 = """2. (5) (ネ技II-01python.pdf, p.35)
<pre><code>err = "IndexError"
n = f"エラー内容:{err}"</code></pre>"""

q_14 = """2. (6) (ネ技II-01python.pdf, p.37)
<pre><code>req = "GET / HTTP/1.1\\r\\nHost: ..."
delim = "\\r\\n"
n = req.find(delim)</code></pre>"""

q_15 = """2. (7) (ネ技II-05RESPONSEのテスト.pdf, p.23)
<pre><code>req = "GET / HTTP/1.1\\r\\nHost: ..."
delim = "\\r\\n"
n = req.find(delim)</code></pre>"""

q_16 = """2. (8) (ネ技II-06REQUESTの受信.pdf, p.19)
<pre><code>lang = "ja-JP,ja;q=0.9"
n = lang[:2]</code></pre>"""

q_17 = """2. (9) (ネ技II-06REQUESTの受信.pdf, p.12, 14)
<pre><code>req_headers = {}
key = "Host"
value = "localhost:50000"
req_headers[key] = value
n = req_headers["Host"]</code></pre>"""

q_18 = """2. (10) (ネ技II-01python.pdf, p.23)
<pre><code>password = ""
if not password:
    n = "Empty"
else:
    n = "Filled"</code></pre>"""

q_19 = """3. 次の Web サーバから返ってくる代表的なステータスコードについて、(a) (b) に正しい Reason-Phrase（理由句）を入れなさい。

| ステータスコード | Reason-Phrase |
| :--- | :--- |
| 200 | (a) |
| 301 | (b) |

(a): (`ネ技II-05RESPONSEのテスト.pdf`, p.11) 
(b): (`ネ技II-04reqとres.pdf`, p.21)"""

q_20 = """4. 次のソースコードは、サーバがクライアントからの接続を待って、接続開始後にメッセージを送信する TCPServer プログラムである。空欄 <<a a>> ~ <<g g>> に適切なコードを埋めて完成させなさい。
(`ネ技II-02server.pdf`, p.12-21)

```python
import socket
import signal

# Ctrl+Cを有効化
signal.signal(signal.SIGINT, signal.SIG_DFL)

# 1. ソケットを作成
sock = socket.socket(socket.AF_INET, <<a___a>>)

# 2. 自分の情報を登録
sock.<<b___ b>>(("", 50000))

# 3. 誰かが接続してくるのを待つ
sock.<<c c>>()

# 4. 接続してきたら接続を許可する
sock_c, addr = sock.<<d___ d>>()

# 5. 通信する
msg = "hello!"
try:
    sock_c.sendall(msg.<<e _____ e>>("UTF-8"))
except:
    print("sendall function failed.")

# 6. ソケットを閉じる
sock_c.<<f _____ f>>()
sock.<<g _____ g>>()
```"""

q_21 = """5. 次のソースコードは、クライアントがサーバに接続してメッセージを受信して表示する TCPClient プログラムである。空欄 `<<a a>>` ~ `<<d d>>` に適切なコードを埋めて完成させなさい。
(`ネ技II-03-1client.pdf`, p.9-13)

```python
import socket

# 接続先情報
HOST = "127.0.0.1"
PORT = 50000

# 1. ソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. サーバへ接続
sock.<<a a>>((HOST, PORT))

# 3. 通信する (受信)
BUFSIZE = 256
data = sock.<<b b>>(BUFSIZE)

# 受信したデータをデコードして表示
if data:
    print(data.<<c c>>("UTF-8"))

# 4. ソケットを閉じる
sock.<<d d>>()
```"""

q_22 = """6. 次のソースコードは、`webserver.py` の `commun` 関数内で、受信したHTTP Request（`http_req` リストに格納済み）を解析する部分である。空欄 `<<a a>>` ~ `<<f f>>` に適切なコードを埋めて完成させなさい。
(`ネ技II-06REQUESTの受信.pdf`, p.10-19)

```python
# Request Lineを解析
req_line = http_req[0]
req_method, req_uri, req_protocol = req_line.<<a a>>(" ")

# Request Headerを解析
req_headers = <<b b>>  # 辞書型変数を初期化

# 1行目(Header)から最後から2行目(Header)までループ
for keyvalue in http_req[1:<<c c>>]:
    key, value = keyvalue.<<a a>>(<<d d>>)
    req_headers[key] = value

print(f"method is {req_method}")
print(f"request header is ...\\n{req_headers}")

# Accept-Languageヘッダの存在確認
if <<e e>> in req_headers:
    # Accept-Languageの値の先頭2文字をチェック
    if req_headers["Accept-Language"][<<f f>>] == "ja":
        message_body = "こんにちはー"
    else:
        message_body = "Hello!"
```"""


# (q_1 から q_22 までは シミュレーション1 で定義済みとします)
# ...

# --- ネットワーク技術II - 中間試験（シミュレーション2）---

q_23 = "1. (1) Pythonでソケットプログラミングを使用する際に `import` が必要なモジュール名を答えなさい。 (`ネ技II-02server.pdf`, p.12)"

q_24 = "1. (2) Pythonでキーボードからの `[Ctrl]+[C]` 割り込みを処理するために `import` が必要なモジュール名を答えなさい。 (`ネ技II-02server.pdf`, p.26)"

q_25 = "1. (3) ポート番号 0〜1023 の範囲は何と呼ばれているか。 (`ネ技II-02server.pdf`, p.14)"

q_26 = "1. (4) HTTP Requestの1行目（リクエストライン）を構成する3つの要素を順に答えなさい。 (`ネ技II-06REQUESTの受信.pdf`, p.9)"

q_27 = "1. (5) HTTP Responseの1行目（ステータスライン）を構成する3つの要素を順に答えなさい。 (`ネ技II-05RESPONSEのテスト.pdf`, p.10)"

q_28 = "1. (6) `sendall` メソッドを `try...except` ブロックで囲むのは、どのような例外(エラー)の発生が想定されるからか。理由を2つ答えなさい。 (`ネ技II-02server.pdf`, p.18)"

q_29 = "1. (7) Pythonの「リスト (list)」と「タプル (tuple)」の最も大きな違い（特に値の変更に関して）を簡潔に説明しなさい。 (`ネ技II-01python.pdf`, p.34)"

q_30 = """2. (1) (`ネ技II-01python.pdf`, p.30)
<pre><code>n = len("python")</code></pre>"""

q_31 = """2. (2) (`ネ技II-01python.pdf`, p.30)
<pre><code>n = max(5, 1, 10)</code></pre>"""

q_32 = """2. (3) (`ネ技II-01python.pdf`, p.33)
<pre><code>a = (10, 20, 30)
n = a[1]</code></pre>"""

q_33 = """2. (4) (`ネ技II-01python.pdf`, p.32)
<pre><code>b = [10]
b.append(20)
n = b</code></pre>"""

q_34 = """2. (5) (`ネ技II-01python.pdf`, p.32)
<pre><code>b = [1]
b.extend([2, 3])
n = b</code></pre>"""

q_35 = """2. (6) (`ネ技II-01python.pdf`, p.23)
<pre><code>a = 10
if a > 10:
    n = 1
elif a == 10:
    n = 2
else:
    n = 3</code></pre>"""

q_36 = """2. (7) (`ネ技II-06REQUESTの受信.pdf`, p.19)
<pre><code>req_headers = {"Host": "localhost", "Connection": "keep-alive"}
n = "Host" in req_headers</code></pre>"""

q_37 = """2. (8) (`ネ技II-06REQUESTの受信.pdf`, p.19)
<pre><code>s = "Hello!"
n = s.replace("l", "x")</code></pre>"""

q_38 = """2. (9) (`ネ技II-06REQUESTの受信.pdf`, p.14)
<pre><code>line = "Host: localhost"
n = line.split(": ")</code></pre>"""

q_39 = """2. (10) (`ネ技II-01python.pdf`, p.30)
<pre><code>n = type("abc")</code></pre>"""

q_40 = """3. 次の図は HTTP Request のリクエストラインの構造を示したものである。(a)~(c) に入る適切な用語を答えなさい。
(`ネ技II-06REQUESTの受信.pdf`, p.9)

`[ (a) ] [ (b) ] [ (c) ]`
(例: `GET / HTTP/1.1`)

(a):
(b):
(c):"""

q_41 = """4. 次のソースコードは、`webserver.py` の `commun` 関数内で、最小構成のHTTP Responseを送信する部分である。空欄 `<<a a>>` ~ `<<e e>>` に適切なコードを埋めて完成させなさい。
(`ネ技II-05RESPONSEのテスト.pdf`, p.11)
```python
# HTTPの改行コード
CRLF = <<a a>>

# ステータスライン
status_line = f"HTTP/1.1 200 OK"
# メッセージボディ
message_body = "こんにちはー"

try:
    # ステータスラインとCRLFを送信
    sock.sendall(f"{status_line}{<<b b>>}".<<c c>>())
    
    # 空行(CRLF)を送信
    sock.sendall(<<d d>>.encode())
    
    # メッセージボディを送信
    sock.sendall(<<e e>>.encode())

except Exception as e:
    print(f"communで例外発生:{e}")
```"""

q_42 = """5. 次のソースコードは、`webserver.py` で使用する、HTTP Requestを1行ずつ（CRLFまで）抽出する関数である。空欄 `<<a a>>` ~ `<<e e>>` に適切なコードを埋めて完成させなさい。
(`ネ技II-05RESPONSEのテスト.pdf`, p.25)
```python
def extract_row(sock, recv_unit=1, delim=<<a a>>):
    req = ""
    
    # delim が見つかるまでループ
    while req.<<b b>>(delim) < 0:
        
        # 1バイトずつ受信
        data = sock.<<c c>>(recv_unit)
        
        # データがなければループ終了
        if not <<d d>>:
            break
            
        # 受信データを文字列に変換して結合
        req += data.<<e e>>()
        
    return req
```"""

q_43 = """6. 次のソースコードは、Pythonの例外処理（try-except-finally）の例である。空欄 `<<a a>>` ~ `<<d d>>` に適切なコードを埋めて完成させなさい。
(`ネ技II-01python.pdf`, p.36-37)
```python
a = [10, 20]  # 要素は2つ (インデックスは 0, 1)

<<a a>>:
    # 3回ループ (i = 0, 1, 2)
    for i in range(3):
        # i=2 の時に a[2] にアクセスしようとしてエラーになる
        print(a[i])

# IndexError が発生した場合の処理
<<b b>> <<c c>> as err:
    print(f"エラーが発生しました: {err}")

# エラーの有無にかかわらず最後に実行
<<d d>>:
    print("処理を終了します")
```"""







# --- 解答データ (日本語) ---

flashcard_data = {

    # --- シミュレーションAのここから追加 ---
    q_A_1: "HTTP Request (または HTTPリクエスト)",
    q_A_2: "Request Line, Request Header, An Empry row, Message Body",
    q_A_3: "HTTP Response (または HTTPレスポンス)",
    q_A_4: "Status Line, Response Header, An Empry row, Message Body",
    q_A_5: "n = 30",
    q_A_6: "n = 50",
    q_A_7: "n = [20, 30, 40]",
    q_A_8: "n = '/test.html'",
    q_A_9: "n = 'text/html'",
    q_A_10: "n = 'ja'",
    q_A_11: "n = 4",
    q_A_12: "n = 30",
    q_A_13: "n = [3, 'test']",
    q_A_14: "n = [0, 1, 2]",
    q_A_15: "(a) OK\n(b) 404\n(c) 権限がない\n(d) Not Implemented",
    q_A_16: "a: `connect`\nb: `sendall`\nc: `encode`\nd: `close`",
    q_A_17: "a: `bind`\nb: `listen`\nc: `accept`\nd: `recv`\ne: `BUFSIZE`\nf: `decode`\ng: `close`\nh: `close`",
    # --- シミュレーションAのここまで ---


        # --- シミュレーションBのここから追加 ---
    q_B_1: "クライアント",
    q_B_2: "socket, connect, close (この順序)",
    q_B_3: "サーバ",
    q_B_4: "socket, bind, listen, accept (この順序)",
    q_B_5: "n = 243",
    q_B_6: "n = [1, 2, 9, 8, 7]",
    q_B_7: "n = (2, 3)",
    q_B_8: "n = 12",
    q_B_9: "n = <class 'int'>",
    q_B_10: "n = 'applepen'",
    q_B_11: "n = [5, 20]",
    q_B_12: "n = 'GET'",
    q_B_13: "n = 'cde'",
    q_B_14: "n = 2",
    q_B_15: "(a) text/plain\n(b) HTMLファイル\n(c) image/jpeg\n(d) png",
    q_B_16: "a: `SOCK_STREAM`\nb: `PORT`\nc: `recv`\nd: `decode`",
    q_B_17: "a: `settimeout`\nb: `one_row`\nc: `extract_row`\nd: `0`\ne: `split`\nf: `1`\ng: `-1`",
    # --- シミュレーションBのここまで ---
    q_1: "HTTP Request (HTTPリクエスト)",
    q_2: "HTTP Response (HTTPレスポンス)",
    q_3: "ステータスライン (Status Line)",
    q_4: "ステータスライン、空行 (An Empty row)、メッセージボディ (Message Body)",
    q_5: "受信バッファ (Receive Buffer)",
    q_6: "送信バッファ (Send Buffer)",
    q_7: "127.0.0.1",
    q_8: "49152〜65535",
    q_9: "n = 243",
    q_10: "n = 'applepen'",
    q_11: "n = 40",
    q_12: "n = [20, 30]",
    q_13: "n = 5",
    q_14: "n = 'エラー内容:IndexError'",
    q_15: "n = 16",
    q_16: "n = 'ja'",
    q_17: "n = 'localhost:50000'",
    q_18: "n = 'Empty'",
    q_19: "(a) OK\n(b) Moved Permanently",
    q_20: "a: `socket.SOCK_STREAM`\nb: `bind`\nc: `listen`\nd: `accept`\ne: `encode`\nf: `close`\ng: `close`",
    q_21: "a: `connect`\nb: `recv`\nc: `decode`\nd: `close`",
    q_22: "a: `split`\nb: `{}`\nc: `-1`\nd: `\": \"`\ne: `\"Accept-Language\"`\nf: `:2`",

    # (q_1 から q_22 までのデータ)
    # ...
    
    # --- シミュレーション2のここから追加 ---
    q_23: "`socket`",
    q_24: "`signal`",
    q_25: "well-known port number (ウェルノウンポート番号)",
    q_26: "メソッド (Method)、Request-URI、HTTP-Version",
    q_27: "プロトコル名 (HTTP-Version)、ステータスコード (Status Code)、Reason-Phrase",
    q_28: "1. `encode` メソッドがバイト列に変換できない場合。\n2. `sendall` メソッドが送信に失敗した場合。",
    q_29: "リストは値の変更が可能（Mutable）だが、タプルは値の変更が不可能（Immutable）である点。",
    q_30: "n = 6",
    q_31: "n = 10",
    q_32: "n = 20",
    q_33: "n = [10, 20]",
    q_34: "n = [1, 2, 3]",
    q_35: "n = 2",
    q_36: "n = True",
    q_37: "n = 'hexxo'",
    q_38: "n = ['Host', 'localhost']",
    q_39: "n = <class 'str'>",
    q_40: "(a) メソッド (Method)\n(b) Request-URI\n(c) HTTP-Version",
    q_41: "a: `\"\\r\\n\"`\nb: `CRLF`\nc: `encode`\nd: `CRLF`\ne: `message_body`",
    q_42: "a: `\"\\r\\n\"`\nb: `find`\nc: `recv`\nd: `data`\ne: `decode`",
    q_43: "a: `try`\nb: `except`\nc: `IndexError`\nd: `finally`"
    # --- シミュレーション2のここまで ---
}

# --- 英語翻訳 ---

english_translations = {
    # --- シミュレーションAのここから追加 ---
    q_A_1: {
        "question": "1. (1) When browsing a web page, what is the message sent to the web server to 'request data' called? (Network Tech II-04req_and_res.pdf, p. 3)",
        "answer": "HTTP Request"
    },
    q_A_2: {
        "question": "1. (2) What blocks is (1) composed of? Choose 4 from the following options: (Status Line, Request Line, Message Body, Request Header, An Empry row, Response Header). (Network Tech II-05RESPONSE_test.pdf, p. 19)",
        "answer": "Request Line, Request Header, An Empry row, Message Body"
    },
    q_A_3: {
        "question": "1. (3) In response to (1), what is the message the web server sends back to the browser to 'provide data' called? (Network Tech II-04req_and_res.pdf, p. 3)",
        "answer": "HTTP Response"
    },
    q_A_4: {
        "question": "1. (4) What blocks is (3) composed of? Choose 4 from the options in (2). (Network Tech II-05RESPONSE_test.pdf, p. 7)",
        "answer": "Status Line, Response Header, An Empry row, Message Body"
    },
    q_A_5: {
        "question": "2. (1) (Network Tech II-01python.pdf, p. 31)\n```python\na = [10, 20, 30, 40, 50]\nn = a[2]\n```",
        "answer": "n = 30"
    },
    q_A_6: {
        "question": "2. (2) (Network Tech II-01python.pdf, p. 31)\n```python\na = [10, 20, 30, 40, 50]\nn = a[-1]\n```",
        "answer": "n = 50"
    },
    q_A_7: {
        "question": "2. (3) (Network Tech II-01python.pdf, p. 31)\n```python\na = [10, 20, 30, 40, 50]\nn = a[1:4]\n```",
        "answer": "n = [20, 30, 40]"
    },
    q_A_8: {
        "question": "2. (4) (Network Tech II-06REQUEST_reception.pdf, p. 10)\n```python\nreq_line = \"GET /test.html HTTP/1.1\"\nparts = req_line.split(\" \")\nn = parts[1]\n```",
        "answer": "n = '/test.html'"
    },
    q_A_9: {
        "question": "2. (5) (Network Tech II-06REQUEST_reception.pdf, p. 14)\n```python\nheaders = {}\nheaders[\"Content-Type\"] = \"text/html\"\nn = headers[\"Content-Type\"]\n```",
        "answer": "n = 'text/html'"
    },
    q_A_10: {
        "question": "2. (6) (Network Tech II-06REQUEST_reception.pdf, p. 19)\n```python\nlang = \"ja-JP,ja;q=0.9\"\nn = lang[:2]\n```",
        "answer": "n = 'ja'"
    },
    q_A_11: {
        "question": "2. (7) (Network Tech II-01python.pdf, p. 30)\n```python\nn = len(\"test\")\n```",
        "answer": "n = 4"
    },
    q_A_12: {
        "question": "2. (8) (Network Tech II-01python.pdf, p. 30)\n```python\nn = max(12, 20, 30)\n```",
        "answer": "n = 30"
    },
    q_A_13: {
        "question": "2. (9) (Network Tech II-01python.pdf, p. 32)\n```python\nb = []\nb.append(3)\nb.append(\"test\")\nn = b\n```",
        "answer": "n = [3, 'test']"
    },
    q_A_14: {
        "question": "2. (10) (Network Tech II-01python.pdf, p. 35, p. 37)\n```python\na = []\nfor i in range(3):\n    a.append(i)\nn = a\n```",
        "answer": "n = [0, 1, 2]"
    },
    q_A_15: {
        "question": "3. Regarding the status codes returned from the web server, fill in the correct numbers or Reason-Phrases for (a) to (d) in the table. (Network Tech II-07WebServerComplete.pdf, p. 11)\n\n| Status Code | Reason-Phrase | Meaning |\n| :--- | :--- | :--- |\n| 200 | ( a ) | Success |\n| ( b ) | Not Found | Page not found |\n| 403 | Forbidden | ( c ) |\n| 501 | ( d ) | (Server) has not implemented it |",
        "answer": "(a) OK\n(b) 404\n(c) No permission (Forbidden)\n(d) Not Implemented"
    },
    q_A_16: {
        "question": "4. The following source code is for a client connecting to a server and sending a message. Fill in the blanks \<\<a>\> to \<\<d\>\> with the appropriate code. (Network Tech II-03-1client.pdf, pp. 21-22)\n```python\nimport socket\n\nHOST = \"127.0.0.1\"\nPORT = 50000\n\nsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nsock.<< a >>((HOST, PORT)) # Connect to server\n\nmsg = \"hello from client\"\ntry:\n    sock.<< b >>(msg.<< c >>(\"UTF-8\")) # Send message\nexcept:\n    print(\"sendall function failed.\")\n\nsock.<< d >>() # Close socket\n```",
        "answer": "a: `connect`\nb: `sendall`\nc: `encode`\nd: `close`"
    },
    q_A_17: {
        "question": "5. The following source code is for a server waiting for a client connection, then receiving and displaying a message. Fill in the blanks \<\<a>\> to \<\<h\>\> with the appropriate code. (Network Tech II-02server.pdf, p. 28; Network Tech II-03-1client.pdf, p. 23)\n```python\nimport socket\nimport signal\n\nsignal.signal(signal.SIGINT, signal.SIG_DFL)\n\nsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nsock.<< a >>((\"\", 50000))  # Register IP and port\nsock.<< b >>()            # Set to listening state\n\nprint(\"Waiting for a connection...\")\nsock_c, addr = sock.<< c >>() # Accept connection request\n\nBUFSIZE = 1024\ndata = sock_c.<< d >>(<< e >>) # Receive data\nif data:\n    print(data.<< f >>(\"UTF-8\")) # Decode and display\nsock_c.<< g >>() # Close communication socket\nsock.<< h >>() # Close listening socket\n```",
        "answer": "a: `bind`\nb: `listen`\nc: `accept`\nd: `recv`\ne: `BUFSIZE`\nf: `decode`\ng: `close`\nh: `close`"
    },
    # --- シミュレーションAのここまで ---



        # --- シミュレーションBのここから追加 ---
    q_B_1: {
        "question": "1. (1) In network communication, what is the side that uses services or functions called? (Network Tech II-02server.pdf, p. 7)",
        "answer": "Client"
    },
    q_B_2: {
        "question": "1. (2) What are the 3 basic steps in the processing flow for (1)? Write them using the options (socket, bind, listen, connect, accept, close). (Network Tech II-03-1client.pdf, p. 6)",
        "answer": "socket, connect, close (in this order)"
    },
    q_B_3: {
        "question": "1. (3) In contrast to (1), what is the side that provides services or functions called? (Network Tech II-02server.pdf, p. 7)",
        "answer": "Server"
    },
    q_B_4: {
        "question": "1. (4) What are the 4 basic steps in the listening process for (3)? Choose from the options in (2) and write them in the correct order. (Network Tech II-02server.pdf, p. 10)",
        "answer": "socket, bind, listen, accept (in this order)"
    },
    q_B_5: {
        "question": "2. (1) (Network Tech II-01python.pdf, p. 15)\n```python\nn = 3**5\n```",
        "answer": "n = 243"
    },
    q_B_6: {
        "question": "2. (2) (Network Tech II-01python.pdf, p. 32)\n```python\nb = [1, 2]\nb.extend([9, 8, 7])\nn = b\n```",
        "answer": "n = [1, 2, 9, 8, 7]"
    },
    q_B_7: {
        "question": "2. (3) (Network Tech II-01python.pdf, p. 33)\n```python\na = (1, 2, 3, 4)\nn = a[1:3]\n```",
        "answer": "n = (2, 3)"
    },
    q_B_8: {
        "question": "2. (4) (Network Tech II-01python.pdf, p. 30)\n```python\nn = min(12, 20, 30)\n```",
        "answer": "n = 12"
    },
    q_B_9: {
        "question": "2. (5) (Network Tech II-01python.pdf, p. 30)\n```python\nn = type(12)\n```",
        "answer": "n = <class 'int'>"
    },
    q_B_10: {
        "question": "2. (6) (Network Tech II-01python.pdf, p. 18)\n```python\nn = 'apple' + 'pen'\n```",
        "answer": "n = 'applepen'"
    },
    q_B_11: {
        "question": "2. (7) (Network Tech II-01python.pdf, p. 31)\n```python\na = [10, 20]\na[0] = 5\nn = a\n```",
        "answer": "n = [5, 20]"
    },
    q_B_12: {
        "question": "2. (8) (Network Tech II-06REQUEST_reception.pdf, p. 10)\n```python\nreq_line = \"GET /test.html HTTP/1.1\"\nn = req_line.split(\" \")[0]\n```",
        "answer": "n = 'GET'"
    },
    q_B_13: {
        "question": "2. (9) (Network Tech II-01python.pdf, p. 31)\n```python\na = \"abcde\"\nn = a[2:]\n```",
        "answer": "n = 'cde'"
    },
    q_B_14: {
        "question": "2. (10) (Network Tech II-05RESPONSE_test.pdf, p. 23)\n```python\na = \"abcde\"\nn = a.find(\"c\")\n```",
        "answer": "n = 2"
    },
    q_B_15: {
        "question": "3. Regarding the Content-Type (MIME Type) sent by the web server, fill in the correct strings for (a) to (d) in the table. (Network Tech II-07WebServerComplete.pdf, p. 17)\n\n| Content Type | Type | Extension |\n| :--- | :--- | :--- |\n| ( a ) | Text file | txt |\n| text/html | ( b ) | htm, html |\n| ( c ) | JPEG file | jpg, jpeg |\n| image/png | PNG file | ( d ) |",
        "answer": "(a) text/plain\n(b) HTML file\n(c) image/jpeg\n(d) png"
    },
    q_B_16: {
        "question": "4. The following source code is for a client connecting to a server and receiving a message. Fill in the blanks \<\<a>\> to \<\<d\>\> with the appropriate code. (Network Tech II-03-1client.pdf, pp. 9-12)\n```python\nimport socket\n\nHOST = \"127.0.0.1\"\nPORT = 50000\nBUFSIZE = 1024\n\nsock = socket.socket(socket.AF_INET, socket.<< a >>)\nsock.connect((HOST, << b >>)) # Connect to server\n\ndata = sock.<< c >>(BUFSIZE) # Receive data\nif data:\n    print(data.<< d >>(\"UTF-8\")) # Decode and display\n\nsock.close()\n```",
        "answer": "a: `SOCK_STREAM`\nb: `PORT`\nc: `recv`\nd: `decode`"
    },
    q_B_17: {
        "question": "5. The following source code is a part that parses a received HTTP Request line by line. Fill in the blanks \<\<a>\> to \<\<g\>\> with the appropriate code. (Network Tech II-06REQUEST_reception.pdf, pp. 5, 10, 13, 14)\n```python\nimport socket\n\n# (Assume extract_row function is defined)\nCRLF = \"\r\n\"\nsock.<< a >>(1)  # 1 second timeout\n\ntry:\n    one_row = extract_row(sock)\n    http_req = [one_row.replace(CRLF, \"\")]\n\n    while << b >>:  # Until one_row is empty\n        one_row = << c >>(sock) # Extract one line\n        http_req.append(one_row.replace(CRLF, \"\"))\n\nexcept socket.timeout:\n    print(\"Reception timed out after 1 second\")\n\nprint(http_req)\n\nreq_line = http_req[<< d >>] # Get Request Line\nreq_method, req_uri, req_protocol = req_line.<< e >>(\" \") # Split into 3 parts\n\nreq_headers = {}\nfor keyvalue in http_req[<< f >>:<< g >>]: # Loop through Header section\n    key, value = keyvalue.split(\": \")\n    req_headers[key] = value\n```",
        "answer": "a: `settimeout`\nb: `one_row`\nc: `extract_row`\nd: `0`\ne: `split`\nf: `1`\ng: `-1`"
    },
    # --- シミュレーションBのここまで ---
    q_1: {
        "question": "1. (1) What is the data sent from a browser to a web server when browsing a web page called? (Network Tech II-04req_and_res.pdf, p.3)",
        "answer": "HTTP Request"
    },
    q_2: {
        "question": "1. (2) In response to (1), what is the data sent back from the web server to the browser called? (Network Tech II-04req_and_res.pdf, p.3)",
        "answer": "HTTP Response"
    },
    q_3: {
        "question": "1. (3) What is the first line of an HTTP Response (e.g., `HTTP/1.1 200 OK`) called? (Network Tech II-05RESPONSE_test.pdf, p.7)",
        "answer": "Status Line"
    },
    q_4: {
        "question": "1. (4) What are the three minimum components of an HTTP Response that a web server sends back to a browser? (Network Tech II-05RESPONSE_test.pdf, p.7)",
        "answer": "Status Line, An Empty row, Message Body"
    },
    q_5: {
        "question": "1. (5) In Python socket programming, from which OS-managed area does the `recv()` method read data? (Network Tech II-03-2buffer.pdf, p.11)",
        "answer": "Receive Buffer"
    },
    q_6: {
        "question": "1. (6) In Python socket programming, to which OS-managed area does the `sendall()` method write data? (Network Tech II-03-2buffer.pdf, p.12)",
        "answer": "Send Buffer"
    },
    q_7: {
        "question": "1. (7) What is the special IP address (loopback address) that refers to oneself on a network? (Network Tech II-03-1client.pdf, p.9)",
        "answer": "127.0.0.1"
    },
    q_8: {
        "question": "1. (8) Within the port number range 0-65535, what is the range that can be freely used as dynamic/private ports? (Network Tech II-02server.pdf, p.14)",
        "answer": "49152-65535"
    },
    q_9: {
        "question": "2. (1) (Network Tech II-01python.pdf, p.15)\n```python\nn = 3 ** 5\n```",
        "answer": "n = 243"
    },
    q_10: {
        "question": "2. (2) (Network Tech II-01python.pdf, p.18)\n```python\na = 'apple'\nb = 'pen'\nn = a + b\n```",
        "answer": "n = 'applepen'"
    },
    q_11: {
        "question": "2. (3) (Network Tech II-01python.pdf, p.31)\n```python\na = [10, 20, 30, 40]\nn = a[-1]\n```",
        "answer": "n = 40"
    },
    q_12: {
        "question": "2. (4) (Network Tech II-01python.pdf, p.31)\n```python\na = [10, 20, 30, 40]\nn = a[1:3]\n```",
        "answer": "n = [20, 30]"
    },
    q_13: {
        "question": "2. (5) (Network Tech II-01python.pdf, p.35)\n```python\nn = 0\nfor i in range(5):\n    n = n + 1\n```",
        "answer": "n = 5"
    },
    q_14: {
        "question": "2. (6) (Network Tech II-01python.pdf, p.37)\n```python\nerr = \"IndexError\"\nn = f\"エラー内容:{err}\"\n```",
        "answer": "n = 'エラー内容:IndexError' (Content of error:IndexError)"
    },
    q_15: {
        "question": "2. (7) (Network Tech II-05RESPONSE_test.pdf, p.23)\n```python\nreq = \"GET / HTTP/1.1\\r\\nHost: ...\"\ndelim = \"\\r\\n\"\nn = req.find(delim)\n```",
        "answer": "n = 16"
    },
    q_16: {
        "question": "2. (8) (Network Tech II-06REQUEST_reception.pdf, p.19)\n```python\nlang = \"ja-JP,ja;q=0.9\"\nn = lang[:2]\n```",
        "answer": "n = 'ja'"
    },
    q_17: {
        "question": "2. (9) (Network Tech II-06REQUEST_reception.pdf, p.12, 14)\n```python\nreq_headers = {}\nkey = \"Host\"\nvalue = \"localhost:50000\"\nreq_headers[key] = value\nn = req_headers[\"Host\"]\n```",
        "answer": "n = 'localhost:50000'"
    },
    q_18: {
        "question": "2. (10) (Network Tech II-01python.pdf, p.23)\n```python\npassword = \"\"\nif not password:\n    n = \"Empty\"\nelse:\n    n = \"Filled\"\n```",
        "answer": "n = 'Empty'"
    },
    q_19: {
        "question": "3. Regarding the typical status codes returned from a web server, fill in the correct Reason-Phrase for (a) and (b).\n\n| Status Code | Reason-Phrase |\n| :--- | :--- |\n| 200 | (a) |\n| 301 | (b) |\n\n(a): (Network Tech II-05RESPONSE_test.pdf, p.11)\n(b): (Network Tech II-04req_and_res.pdf, p.21)",
        "answer": "(a) OK\n(b) Moved Permanently"
    },
    q_20: {
        "question": "4. The following source code is a TCPServer program that waits for a connection from a client and sends a message after the connection starts. Fill in the blanks <<a a>> ~ <<g g>> with the appropriate code to complete it.\n(Network Tech II-02server.pdf, p.12-21)\n\n```python\nimport socket\nimport signal\n\n# Enable Ctrl+C\nsignal.signal(signal.SIGINT, signal.SIG_DFL)\n\n# 1. Create socket\nsock = socket.socket(socket.AF_INET, <<a___a>>)\n\n# 2. Register own info\nsock.<<b___ b>>((\"\", 50000))\n\n# 3. Wait for someone to connect\nsock.<<c c>>()\n\n# 4. Accept the connection\nsock_c, addr = sock.<<d___ d>>()\n\n# 5. Communicate\nmsg = \"hello!\"\ntry:\n    sock_c.sendall(msg.<<e _____ e>>(\"UTF-8\"))\nexcept:\n    print(\"sendall function failed.\")\n\n# 6. Close sockets\nsock_c.<<f _____ f>>()\nsock.<<g _____ g>>()\n```",
        "answer": "a: `socket.SOCK_STREAM`\nb: `bind`\nc: `listen`\nd: `accept`\ne: `encode`\nf: `close`\ng: `close`"
    },
    q_21: {
        "question": "5. The following source code is a TCPClient program that connects to a server, receives a message, and displays it. Fill in the blanks `<<a a>>` ~ `<<d d>>` with the appropriate code to complete it.\n(Network Tech II-03-1client.pdf, p.9-13)\n\n```python\nimport socket\n\n# Connection info\nHOST = \"127.0.0.1\"\nPORT = 50000\n\n# 1. Create socket\nsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n\n# 2. Connect to server\nsock.<<a a>>((HOST, PORT))\n\n# 3. Communicate (Receive)\nBUFSIZE = 256\ndata = sock.<<b b>>(BUFSIZE)\n\n# Decode and display received data\nif data:\n    print(data.<<c c>>(\"UTF-8\"))\n\n# 4. Close socket\nsock.<<d d>>()\n```",
        "answer": "a: `connect`\nb: `recv`\nc: `decode`\nd: `close`"
    },
    q_22: {
        "question": "6. The following source code is a part of the `commun` function in `webserver.py` that parses a received HTTP Request (stored in the `http_req` list). Fill in the blanks `<<a a>>` ~ `<<f f>>` with the appropriate code to complete it.\n(Network Tech II-06REQUEST_reception.pdf, p.10-19)\n\n```python\n# Parse Request Line\nreq_line = http_req[0]\nreq_method, req_uri, req_protocol = req_line.<<a a>>(\" \")\n\n# Parse Request Header\nreq_headers = <<b b>>  # Initialize dictionary\n\n# Loop from 1st line (Header) to the second to last line (Header)\nfor keyvalue in http_req[1:<<c c>>]:\n    key, value = keyvalue.<<a a>>(<<d d>>)\n    req_headers[key] = value\n\nprint(f\"method is {req_method}\")\nprint(f\"request header is ...\\n{req_headers}\")\n\n# Check for Accept-Language header\nif <<e e>> in req_headers:\n    # Check the first 2 chars of Accept-Language value\n    if req_headers[\"Accept-Language\"][<<f f>>] == \"ja\":\n        message_body = \"こんにちはー\"\n    else:\n        message_body = \"Hello!\"\n```",
        "answer": "a: `split`\nb: `{}`\nc: `-1`\nd: `\": \"`\ne: `\"Accept-Language\"`\nf: `:2`"
    },

    # (q_1 から q_22 までの翻訳)
    # ...

    # --- シミュレーション2のここから追加 ---
    q_23: {
        "question": "1. (1) What is the name of the module that needs to be `import`ed to use socket programming in Python? (Network Tech II-02server.pdf, p.12)",
        "answer": "`socket`"
    },
    q_24: {
        "question": "1. (2) What is the name of the module that needs to be `import`ed to handle `[Ctrl]+[C]` interrupts from the keyboard in Python? (Network Tech II-02server.pdf, p.26)",
        "answer": "`signal`"
    },
    q_25: {
        "question": "1. (3) What is the port number range 0-1023 called? (Network Tech II-02server.pdf, p.14)",
        "answer": "well-known port number"
    },
    q_26: {
        "question": "1. (4) What are the three components that make up the first line (Request Line) of an HTTP Request, in order? (Network Tech II-06REQUEST_reception.pdf, p.9)",
        "answer": "Method, Request-URI, HTTP-Version"
    },
    q_27: {
        "question": "1. (5) What are the three components that make up the first line (Status Line) of an HTTP Response, in order? (Network Tech II-05RESPONSE_test.pdf, p.10)",
        "answer": "Protocol (HTTP-Version), Status Code, Reason-Phrase"
    },
    q_28: {
        "question": "1. (6) Why is the `sendall` method enclosed in a `try...except` block? State two types of exceptions (errors) that are anticipated. (Network Tech II-02server.pdf, p.18)",
        "answer": "1. The `encode` method might fail to convert the string to bytes.\n2. The `sendall` method might fail to send the data."
    },
    q_29: {
        "question": "1. (7) Briefly explain the biggest difference between a Python `list` and a `tuple` (especially regarding value modification). (Network Tech II-01python.pdf, p.34)",
        "answer": "A list is mutable (values can be changed), whereas a tuple is immutable (values cannot be changed)."
    },
    q_30: {
        "question": "2. (1) (Network Tech II-01python.pdf, p.30)\n```python\nn = len(\"python\")\n```",
        "answer": "n = 6"
    },
    q_31: {
        "question": "2. (2) (Network Tech II-01python.pdf, p.30)\n```python\nn = max(5, 1, 10)\n```",
        "answer": "n = 10"
    },
    q_32: {
        "question": "2. (3) (Network Tech II-01python.pdf, p.33)\n```python\na = (10, 20, 30)\nn = a[1]\n```",
        "answer": "n = 20"
    },
    q_33: {
        "question": "2. (4) (Network Tech II-01python.pdf, p.32)\n```python\nb = [10]\nb.append(20)\nn = b\n```",
        "answer": "n = [10, 20]"
    },
    q_34: {
        "question": "2. (5) (Network Tech II-01python.pdf, p.32)\n```python\nb = [1]\nb.extend([2, 3])\nn = b\n```",
        "answer": "n = [1, 2, 3]"
    },
    q_35: {
        "question": "2. (6) (Network Tech II-01python.pdf, p.23)\n```python\na = 10\nif a > 10:\n    n = 1\nelif a == 10:\n    n = 2\nelse:\n    n = 3\n```",
        "answer": "n = 2"
    },
    q_36: {
        "question": "2. (7) (Network Tech II-06REQUEST_reception.pdf, p.19)\n```python\nreq_headers = {\"Host\": \"localhost\", \"Connection\": \"keep-alive\"}\nn = \"Host\" in req_headers\n```",
        "answer": "n = True"
    },
    q_37: {
        "question": "2. (8) (Network Tech II-06REQUEST_reception.pdf, p.19)\n```python\ns = \"Hello!\"\nn = s.replace(\"l\", \"x\")\n```",
        "answer": "n = 'hexxo'"
    },
    q_38: {
        "question": "2. (9) (Network Tech II-06REQUEST_reception.pdf, p.14)\n```python\nline = \"Host: localhost\"\nn = line.split(\": \")\n```",
        "answer": "n = ['Host', 'localhost']"
    },
    q_39: {
        "question": "2. (10) (Network Tech II-01python.pdf, p.30)\n```python\nn = type(\"abc\")\n```",
        "answer": "n = <class 'str'>"
    },
    q_40: {
        "question": "3. The following diagram shows the structure of an HTTP Request's request line. Provide the appropriate terms for (a)-(c).\n(`Network Tech II-06REQUEST_reception.pdf`, p.9)\n\n`[ (a) ] [ (b) ] [ (c) ]`\n(Example: `GET / HTTP/1.1`)\n\n(a):\n(b):\n(c):",
        "answer": "(a) Method\n(b) Request-URI\n(c) HTTP-Version"
    },
    q_41: {
        "question": "4. The following source code is a part of the `commun` function in `webserver.py` that sends a minimal HTTP Response. Fill in the blanks `<<a a>>` ~ `<<e e>>` with the appropriate code to complete it.\n(`Network Tech II-05RESPONSE_test.pdf`, p.11)\n```python\n# HTTP newline code\nCRLF = <<a a>>\n\n# Status line\nstatus_line = f\"HTTP/1.1 200 OK\"\n# Message body\nmessage_body = \"こんにちはー\"\n\ntry:\n    # Send status line and CRLF\n    sock.sendall(f\"{status_line}{<<b b>>}\".<<c c>>())\n    \n    # Send empty line (CRLF)\n    sock.sendall(<<d d>>.encode())\n    \n    # Send message body\n    sock.sendall(<<e e>>.encode())\n\nexcept Exception as e:\n    print(f\"Exception in commun:{e}\")\n```",
        "answer": "a: `\"\\r\\n\"`\nb: `CRLF`\nc: `encode`\nd: `CRLF`\ne: `message_body`"
    },
    q_42: {
        "question": "5. The following source code is a function used in `webserver.py` to extract one line (up to CRLF) of an HTTP Request. Fill in the blanks `<<a a>>` ~ `<<e e>>` with the appropriate code to complete it.\n(`Network Tech II-05RESPONSE_test.pdf`, p.25)\n```python\ndef extract_row(sock, recv_unit=1, delim=<<a a>>):\n    req = \"\"\n    \n    # Loop until delim is found\n    while req.<<b b>>(delim) < 0:\n        \n        # Receive 1 byte at a time\n        data = sock.<<c c>>(recv_unit)\n        \n        # If no data, break loop\n        if not <<d d>>:\n            break\n            \n        # Decode received data and append\n        req += data.<<e e>>()\n        \n    return req\n```",
        "answer": "a: `\"\\r\\n\"`\nb: `find`\nc: `recv`\nd: `data`\ne: `decode`"
    },
    q_43: {
        "question": "6. The following source code is an example of Python's exception handling (try-except-finally). Fill in the blanks `<<a a>>` ~ `<<d d>>` with the appropriate code to complete it.\n(`Network Tech II-01python.pdf`, p.36-37)\n```python\na = [10, 20]  # 2 elements (index 0, 1)\n\n<<a a>>:\n    # Loop 3 times (i = 0, 1, 2)\n    for i in range(3):\n        # Error occurs at i=2 when trying to access a[2]\n        print(a[i])\n\n# Handle the IndexError\n<<b b>> <<c c>> as err:\n    print(f\"An error occurred: {err}\")\n\n# Always execute at the end\n<<d d>>:\n    print(\"Processing finished\")\n```",
        "answer": "a: `try`\nb: `except`\nc: `IndexError`\nd: `finally`"
    }
   
    # --- シミュレーション2のここまで ---
}

# --- タイ語翻訳 ---

thai_translations = {

        # --- シミュレーションAのここから追加 ---
    q_A_1: {
        "question": "1. (1) เมื่อเรียกดูหน้าเว็บ ข้อความที่ส่งไปยังเว็บเซิร์ฟเวอร์เพื่อ 'ขอข้อมูล' เรียกว่าอะไร? (Network Tech II-04req_and_res.pdf, p. 3)",
        "answer": "HTTP Request (HTTP รีเควส)"
    },
    q_A_2: {
        "question": "1. (2) (1) ประกอบด้วยบล็อกอะไรบ้าง? จงเลือก 4 รายการจากตัวเลือกต่อไปนี้: (Status Line, Request Line, Message Body, Request Header, An Empry row, Response Header) (Network Tech II-05RESPONSE_test.pdf, p. 19)",
        "answer": "Request Line, Request Header, An Empry row, Message Body"
    },
    q_A_3: {
        "question": "1. (3) เพื่อตอบสนองต่อ (1) ข้อความที่เว็บเซิร์ฟเวอร์ส่งกลับไปยังเบราว์เซอร์เพื่อ 'ให้ข้อมูล' เรียกว่าอะไร? (Network Tech II-04req_and_res.pdf, p. 3)",
        "answer": "HTTP Response (HTTP เรสพอนส์)"
    },
    q_A_4: {
        "question": "1. (4) (3) ประกอบด้วยบล็อกอะไรบ้าง? จงเลือก 4 รายการจากตัวเลือกใน (2) (Network Tech II-05RESPONSE_test.pdf, p. 7)",
        "answer": "Status Line, Response Header, An Empry row, Message Body"
    },
    q_A_5: {
        "question": "2. (1) (Network Tech II-01python.pdf, p. 31)\n```python\na = [10, 20, 30, 40, 50]\nn = a[2]\n```",
        "answer": "n = 30"
    },
    q_A_6: {
        "question": "2. (2) (Network Tech II-01python.pdf, p. 31)\n```python\na = [10, 20, 30, 40, 50]\nn = a[-1]\n```",
        "answer": "n = 50"
    },
    q_A_7: {
        "question": "2. (3) (Network Tech II-01python.pdf, p. 31)\n```python\na = [10, 20, 30, 40, 50]\nn = a[1:4]\n```",
        "answer": "n = [20, 30, 40]"
    },
    q_A_8: {
        "question": "2. (4) (Network Tech II-06REQUEST_reception.pdf, p. 10)\n```python\nreq_line = \"GET /test.html HTTP/1.1\"\nparts = req_line.split(\" \")\nn = parts[1]\n```",
        "answer": "n = '/test.html'"
    },
    q_A_9: {
        "question": "2. (5) (Network Tech II-06REQUEST_reception.pdf, p. 14)\n```python\nheaders = {}\nheaders[\"Content-Type\"] = \"text/html\"\nn = headers[\"Content-Type\"]\n```",
        "answer": "n = 'text/html'"
    },
    q_A_10: {
        "question": "2. (6) (Network Tech II-06REQUEST_reception.pdf, p. 19)\n```python\nlang = \"ja-JP,ja;q=0.9\"\nn = lang[:2]\n```",
        "answer": "n = 'ja'"
    },
    q_A_11: {
        "question": "2. (7) (Network Tech II-01python.pdf, p. 30)\n```python\nn = len(\"test\")\n```",
        "answer": "n = 4"
    },
    q_A_12: {
        "question": "2. (8) (Network Tech II-01python.pdf, p. 30)\n```python\nn = max(12, 20, 30)\n```",
        "answer": "n = 30"
    },
    q_A_13: {
        "question": "2. (9) (Network Tech II-01python.pdf, p. 32)\n```python\nb = []\nb.append(3)\nb.append(\"test\")\nn = b\n```",
        "answer": "n = [3, 'test']"
    },
    q_A_14: {
        "question": "2. (10) (Network Tech II-01python.pdf, p. 35, p. 37)\n```python\na = []\nfor i in range(3):\n    a.append(i)\nn = a\n```",
        "answer": "n = [0, 1, 2]"
    },
    q_A_15: {
        "question": "3. เกี่ยวกับรหัสสถานะที่เว็บเซิร์ฟเวอร์ส่งกลับมา จงเติมตัวเลขหรือ Reason-Phrase ที่ถูกต้องลงใน (a) ถึง (d) ในตาราง (Network Tech II-07WebServerComplete.pdf, p. 11)\n\n| รหัสสถานะ | Reason-Phrase | ความหมาย |\n| :--- | :--- | :--- |\n| 200 | ( a ) | สำเร็จ |\n| ( b ) | Not Found | ไม่พบหน้า |\n| 403 | Forbidden | ( c ) |\n| 501 | ( d ) | (เซิร์ฟเวอร์) ยังไม่รองรับ |",
        "answer": "(a) OK\n(b) 404\n(c) ไม่มีสิทธิ์\n(d) Not Implemented"
    },
    q_A_16: {
        "question": "4. ซอร์สโค้ดต่อไปนี้เป็นโปรแกรมไคลเอนต์ที่เชื่อมต่อกับเซิร์ฟเวอร์และส่งข้อความ จงเติมโค้ดที่เหมาะสมลงในช่องว่าง \<\<a>\> ถึง \<\<d\>\> (Network Tech II-03-1client.pdf, pp. 21-22)\n```python\nimport socket\n\nHOST = \"127.0.0.1\"\nPORT = 50000\n\nsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nsock.<< a >>((HOST, PORT)) # เชื่อมต่อเซิร์ฟเวอร์\n\nmsg = \"hello from client\"\ntry:\n    sock.<< b >>(msg.<< c >>(\"UTF-8\")) # ส่งข้อความ\nexcept:\n    print(\"sendall function failed.\")\n\nsock.<< d >>() # ปิดซ็อกเก็ต\n```",
        "answer": "a: `connect`\nb: `sendall`\nc: `encode`\nd: `close`"
    },
    q_A_17: {
        "question": "5. ซอร์สโค้ดต่อไปนี้เป็นโปรแกรมเซิร์ฟเวอร์ที่รอการเชื่อมต่อจากไคลเอนต์ จากนั้นรับและแสดงข้อความ จงเติมโค้ดที่เหมาะสมลงในช่องว่าง \<\<a>\> ถึง \<\<h\>\> (Network Tech II-02server.pdf, p. 28; Network Tech II-03-1client.pdf, p. 23)\n```python\nimport socket\nimport signal\n\nsignal.signal(signal.SIGINT, signal.SIG_DFL)\n\nsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nsock.<< a >>((\"\", 50000))  # ลงทะเบียน IP และพอร์ต\nsock.<< b >>()            # ตั้งค่าสถานะรอการเชื่อมต่อ\n\nprint(\"Waiting for a connection...\")\nsock_c, addr = sock.<< c >>() # ยอมรับการเชื่อมต่อ\n\nBUFSIZE = 1024\ndata = sock_c.<< d >>(<< e >>) # รับข้อมูล\nif data:\n    print(data.<< f >>(\"UTF-8\")) # ถอดรหัสและแสดงผล\nsock_c.<< g >>() # ปิดซ็อกเก็ตสื่อสาร\nsock.<< h >>() # ปิดซ็อกเก็ตสำหรับรอรับ\n```",
        "answer": "a: `bind`\nb: `listen`\nc: `accept`\nd: `recv`\ne: `BUFSIZE`\nf: `decode`\ng: `close`\nh: `close`"
    },
    # --- シミュレーションAのここまで ---


        # --- シミュレーションBのここから追加 ---
    q_B_1: {
        "question": "1. (1) ในการสื่อสารเครือข่าย ฝั่งที่ใช้บริการหรือฟังก์ชันเรียกว่าอะไร? (Network Tech II-02server.pdf, p. 7)",
        "answer": "ไคลเอนต์ (Client)"
    },
    q_B_2: {
        "question": "1. (2) 3 ขั้นตอนพื้นฐานในกระบวนการทำงานของ (1) คืออะไร? จงเขียนโดยใช้ตัวเลือก (socket, bind, listen, connect, accept, close) (Network Tech II-03-1client.pdf, p. 6)",
        "answer": "socket, connect, close (ตามลำดับนี้)"
    },
    q_B_3: {
        "question": "1. (3) ตรงข้ามกับ (1) ฝั่งที่ให้บริการหรือฟังก์ชันเรียกว่าอะไร? (Network Tech II-02server.pdf, p. 7)",
        "answer": "เซิร์ฟเวอร์ (Server)"
    },
    q_B_4: {
        "question": "1. (4) 4 ขั้นตอนพื้นฐานในกระบวนการรอรับการเชื่อมต่อของ (3) คืออะไร? จงเลือกจากตัวเลือกใน (2) และเขียนตามลำดับที่ถูกต้อง (Network Tech II-02server.pdf, p. 10)",
        "answer": "socket, bind, listen, accept (ตามลำดับนี้)"
    },
    q_B_5: {
        "question": "2. (1) (Network Tech II-01python.pdf, p. 15)\n```python\nn = 3**5\n```",
        "answer": "n = 243"
    },
    q_B_6: {
        "question": "2. (2) (Network Tech II-01python.pdf, p. 32)\n```python\nb = [1, 2]\nb.extend([9, 8, 7])\nn = b\n```",
        "answer": "n = [1, 2, 9, 8, 7]"
    },
    q_B_7: {
        "question": "2. (3) (Network Tech II-01python.pdf, p. 33)\n```python\na = (1, 2, 3, 4)\nn = a[1:3]\n```",
        "answer": "n = (2, 3)"
    },
    q_B_8: {
        "question": "2. (4) (Network Tech II-01python.pdf, p. 30)\n```python\nn = min(12, 20, 30)\n```",
        "answer": "n = 12"
    },
    q_B_9: {
        "question": "2. (5) (Network Tech II-01python.pdf, p. 30)\n```python\nn = type(12)\n```",
        "answer": "n = <class 'int'>"
    },
    q_B_10: {
        "question": "2. (6) (Network Tech II-01python.pdf, p. 18)\n```python\nn = 'apple' + 'pen'\n```",
        "answer": "n = 'applepen'"
    },
    q_B_11: {
        "question": "2. (7) (Network Tech II-01python.pdf, p. 31)\n```python\na = [10, 20]\na[0] = 5\nn = a\n```",
        "answer": "n = [5, 20]"
    },
    q_B_12: {
        "question": "2. (8) (Network Tech II-06REQUEST_reception.pdf, p. 10)\n```python\nreq_line = \"GET /test.html HTTP/1.1\"\nn = req_line.split(\" \")[0]\n```",
        "answer": "n = 'GET'"
    },
    q_B_13: {
        "question": "2. (9) (Network Tech II-01python.pdf, p. 31)\n```python\na = \"abcde\"\nn = a[2:]\n```",
        "answer": "n = 'cde'"
    },
    q_B_14: {
        "question": "2. (10) (Network Tech II-05RESPONSE_test.pdf, p. 23)\n```python\na = \"abcde\"\nn = a.find(\"c\")\n```",
        "answer": "n = 2"
    },
    q_B_15: {
        "question": "3. เกี่ยวกับ Content-Type (MIME Type) ที่เว็บเซิร์ฟเวอร์ส่ง จงเติมสตริงที่ถูกต้องลงใน (a) ถึง (d) ในตาราง (Network Tech II-07WebServerComplete.pdf, p. 17)\n\n| Content Type | ประเภท | นามสกุล |\n| :--- | :--- | :--- |\n| ( a ) | ไฟล์ข้อความ | txt |\n| text/html | ( b ) | htm, html |\n| ( c ) | ไฟล์ JPEG | jpg, jpeg |\n| image/png | ไฟล์ PNG | ( d ) |",
        "answer": "(a) text/plain\n(b) ไฟล์ HTML\n(c) image/jpeg\n(d) png"
    },
    q_B_16: {
        "question": "4. ซอร์สโค้ดต่อไปนี้เป็นโปรแกรมไคลเอนต์ที่เชื่อมต่อกับเซิร์ฟเวอร์และรับข้อความ จงเติมโค้ดที่เหมาะสมลงในช่องว่าง \<\<a>\> ถึง \<\<d\>\> (Network Tech II-03-1client.pdf, pp. 9-12)\n```python\nimport socket\n\nHOST = \"127.0.0.1\"\nPORT = 50000\nBUFSIZE = 1024\n\nsock = socket.socket(socket.AF_INET, socket.<< a >>)\nsock.connect((HOST, << b >>)) # เชื่อมต่อเซิร์ฟเวอร์\n\ndata = sock.<< c >>(BUFSIZE) # รับข้อมูล\nif data:\n    print(data.<< d >>(\"UTF-8\")) # ถอดรหัสและแสดงผล\n\nsock.close()\n```",
        "answer": "a: `SOCK_STREAM`\nb: `PORT`\nc: `recv`\nd: `decode`"
    },
    q_B_17: {
        "question": "5. ซอร์สโค้ดต่อไปนี้เป็นส่วนที่วิเคราะห์ HTTP Request ที่ได้รับทีละบรรทัด จงเติมโค้ดที่เหมาะสมลงในช่องว่าง \<\<a>\> ถึง \<\<g\>\> (Network Tech II-06REQUEST_reception.pdf, pp. 5, 10, 13, 14)\n```python\nimport socket\n\n# (สมมติว่าฟังก์ชัน extract_row ถูกกำหนดไว้แล้ว)\nCRLF = \"\r\n\"\nsock.<< a >>(1)  # ไทม์เอาต์ 1 วินาที\n\ntry:\n    one_row = extract_row(sock)\n    http_req = [one_row.replace(CRLF, \"\")]\n\n    while << b >>:  # จนกว่า one_row จะว่างเปล่า\n        one_row = << c >>(sock) # ดึงข้อมูล 1 บรรทัด\n        http_req.append(one_row.replace(CRLF, \"\"))\n\nexcept socket.timeout:\n    print(\"การรับข้อมูลหมดเวลาหลังจาก 1 วินาที\")\n\nprint(http_req)\n\nreq_line = http_req[<< d >>] # ดึง Request Line\nreq_method, req_uri, req_protocol = req_line.<< e >>(\" \") # แบ่งเป็น 3 ส่วน\n\nreq_headers = {}\nfor keyvalue in http_req[<< f >>:<< g >>]: # วนลูปส่วน Header\n    key, value = keyvalue.split(\": \")\n    req_headers[key] = value\n```",
        "answer": "a: `settimeout`\nb: `one_row`\nc: `extract_row`\nd: `0`\ne: `split`\nf: `1`\ng: `-1`"
    },
    # --- シミュレーションBのここまで ---
    q_1: {
        "question": "1. (1) ข้อมูลที่เบราว์เซอร์ส่งไปยังเว็บเซิร์ฟเวอร์เมื่อเรียกดูหน้าเว็บเรียกว่าอะไร? (Network Tech II-04req_and_res.pdf, p.3)",
        "answer": "HTTP Request (HTTP รีเควส)"
    },
    q_2: {
        "question": "1. (2) เพื่อตอบสนองต่อ (1) ข้อมูลที่เว็บเซิร์ฟเวอร์ส่งกลับไปยังเบราว์เซอร์เรียกว่าอะไร? (Network Tech II-04req_and_res.pdf, p.3)",
        "answer": "HTTP Response (HTTP เรสพอนส์)"
    },
    q_3: {
        "question": "1. (3) บรรทัดแรกของ HTTP Response (เช่น `HTTP/1.1 200 OK`) เรียกว่าอะไร? (Network Tech II-05RESPONSE_test.pdf, p.7)",
        "answer": "Status Line (บรรทัดสถานะ)"
    },
    q_4: {
        "question": "1. (4) องค์ประกอบขั้นต่ำ 3 ส่วนของ HTTP Response ที่เว็บเซิร์ฟเวอร์ใช้ตอบกลับไปยังเบราว์เซอร์คืออะไรบ้าง? (Network Tech II-05RESPONSE_test.pdf, p.7)",
        "answer": "Status Line (บรรทัดสถานะ), An Empty row (บรรทัดว่าง), Message Body (เนื้อหาข้อความ)"
    },
    q_5: {
        "question": "1. (5) ในการเขียนโปรแกรมซ็อกเก็ต Python เมธอด `recv()` อ่านข้อมูลจากพื้นที่ใดที่ OS จัดการ? (Network Tech II-03-2buffer.pdf, p.11)",
        "answer": "Receive Buffer (บัฟเฟอร์รับข้อมูล)"
    },
    q_6: {
        "question": "1. (6) ในการเขียนโปรแกรมซ็อกเก็ต Python เมธอด `sendall()` เขียนข้อมูลไปยังพื้นที่ใดที่ OS จัดการ? (Network Tech II-03-2buffer.pdf, p.12)",
        "answer": "Send Buffer (บัฟเฟอร์ส่งข้อมูล)"
    },
    q_7: {
        "question": "1. (7) ที่อยู่ IP พิเศษ (loopback address) ที่ใช้ระบุถึงตัวเองบนเครือข่ายคืออะไร? (Network Tech II-03-1client.pdf, p.9)",
        "answer": "127.0.0.1"
    },
    q_8: {
        "question": "1. (8) ในบรรดาหมายเลขพอร์ต 0-65535 ช่วงใดที่สามารถใช้เป็นพอร์ตแบบไดนามิก/ส่วนตัวได้อย่างอิสระ? (Network Tech II-02server.pdf, p.14)",
        "answer": "49152-65535"
    },
    q_9: {
        "question": "2. (1) (Network Tech II-01python.pdf, p.15)\n```python\nn = 3 ** 5\n```",
        "answer": "n = 243"
    },
    q_10: {
        "question": "2. (2) (Network Tech II-01python.pdf, p.18)\n```python\na = 'apple'\nb = 'pen'\nn = a + b\n```",
        "answer": "n = 'applepen'"
    },
    q_11: {
        "question": "2. (3) (Network Tech II-01python.pdf, p.31)\n```python\na = [10, 20, 30, 40]\nn = a[-1]\n```",
        "answer": "n = 40"
    },
    q_12: {
        "question": "2. (4) (Network Tech II-01python.pdf, p.31)\n```python\na = [10, 20, 30, 40]\nn = a[1:3]\n```",
        "answer": "n = [20, 30]"
    },
    q_13: {
        "question": "2. (5) (Network Tech II-01python.pdf, p.35)\n```python\nn = 0\nfor i in range(5):\n    n = n + 1\n```",
        "answer": "n = 5"
    },
    q_14: {
        "question": "2. (6) (Network Tech II-01python.pdf, p.37)\n```python\nerr = \"IndexError\"\nn = f\"エラー内容:{err}\"\n```",
        "answer": "n = 'エラー内容:IndexError' (เนื้อหาข้อผิดพลาด:IndexError)"
    },
    q_15: {
        "question": "2. (7) (Network Tech II-05RESPONSE_test.pdf, p.23)\n```python\nreq = \"GET / HTTP/1.1\\r\\nHost: ...\"\ndelim = \"\\r\\n\"\nn = req.find(delim)\n```",
        "answer": "n = 16"
    },
    q_16: {
        "question": "2. (8) (Network Tech II-06REQUEST_reception.pdf, p.19)\n```python\nlang = \"ja-JP,ja;q=0.9\"\nn = lang[:2]\n```",
        "answer": "n = 'ja'"
    },
    q_17: {
        "question": "2. (9) (Network Tech II-06REQUEST_reception.pdf, p.12, 14)\n```python\nreq_headers = {}\nkey = \"Host\"\nvalue = \"localhost:50000\"\nreq_headers[key] = value\nn = req_headers[\"Host\"]\n```",
        "answer": "n = 'localhost:50000'"
    },
    q_18: {
        "question": "2. (10) (Network Tech II-01python.pdf, p.23)\n```python\npassword = \"\"\nif not password:\n    n = \"Empty\"\nelse:\n    n = \"Filled\"\n```",
        "answer": "n = 'Empty'"
    },
    q_19: {
        "question": "3. เกี่ยวกับรหัสสถานะทั่วไปที่เว็บเซิร์ฟเวอร์ส่งกลับมา จงเติม Reason-Phrase (วลีบอกเหตุผล) ที่ถูกต้องลงใน (a) และ (b)\n\n| รหัสสถานะ | Reason-Phrase |\n| :--- | :--- |\n| 200 | (a) |\n| 301 | (b) |\n\n(a): (Network Tech II-05RESPONSE_test.pdf, p.11)\n(b): (Network Tech II-04req_and_res.pdf, p.21)",
        "answer": "(a) OK\n(b) Moved Permanently"
    },
    q_20: {
        "question": "4. ซอร์สโค้ดต่อไปนี้เป็นโปรแกรม TCPServer ที่รอการเชื่อมต่อจากไคลเอนต์และส่งข้อความหลังจากเชื่อมต่อแล้ว จงเติมโค้ดที่เหมาะสมลงในช่องว่าง <<a a>> ~ <<g g>> เพื่อทำให้สมบูรณ์\n(Network Tech II-02server.pdf, p.12-21)\n\n```python\nimport socket\nimport signal\n\n# เปิดใช้งาน Ctrl+C\nsignal.signal(signal.SIGINT, signal.SIG_DFL)\n\n# 1. สร้างซ็อกเก็ต\nsock = socket.socket(socket.AF_INET, <<a___a>>)\n\n# 2. ลงทะเบียนข้อมูลของตัวเอง\nsock.<<b___ b>>((\"\", 50000))\n\n# 3. รอการเชื่อมต่อ\nsock.<<c c>>()\n\n# 4. ยอมรับการเชื่อมต่อ\nsock_c, addr = sock.<<d___ d>>()\n\n# 5. สื่อสาร\nmsg = \"hello!\"\ntry:\n    sock_c.sendall(msg.<<e _____ e>>(\"UTF-8\"))\nexcept:\n    print(\"sendall function failed.\")\n\n# 6. ปิดซ็อกเก็ต\nsock_c.<<f _____ f>>()\nsock.<<g _____ g>>()\n```",
        "answer": "a: `socket.SOCK_STREAM`\nb: `bind`\nc: `listen`\nd: `accept`\ne: `encode`\nf: `close`\ng: `close`"
    },
    q_21: {
        "question": "5. ซอร์สโค้ดต่อไปนี้เป็นโปรแกรม TCPClient ที่เชื่อมต่อกับเซิร์ฟเวอร์ รับข้อความ และแสดงผล จงเติมโค้ดที่เหมาะสมลงในช่องว่าง `<<a a>>` ~ `<<d d>>` เพื่อทำให้สมบูรณ์\n(Network Tech II-03-1client.pdf, p.9-13)\n\n```python\nimport socket\n\n# ข้อมูลปลายทาง\nHOST = \"127.0.0.1\"\nPORT = 50000\n\n# 1. สร้างซ็อกเก็ต\nsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n\n# 2. เชื่อมต่อเซิร์ฟเวอร์\nsock.<<a a>>((HOST, PORT))\n\n# 3. สื่อสาร (รับข้อมูล)\nBUFSIZE = 256\ndata = sock.<<b b>>(BUFSIZE)\n\n# ถอดรหัสและแสดงข้อมูลที่ได้รับ\nif data:\n    print(data.<<c c>>(\"UTF-8\"))\n\n# 4. ปิดซ็อกเก็ต\nsock.<<d d>>()\n```",
        "answer": "a: `connect`\nb: `recv`\nc: `decode`\nd: `close`"
    },
    q_22: {
        "question": "6. ซอร์สโค้ดต่อไปนี้เป็นส่วนหนึ่งในฟังก์ชัน `commun` ของ `webserver.py` ที่ใช้แยกวิเคราะห์ HTTP Request ที่ได้รับ (เก็บในลิสต์ `http_req`) จงเติมโค้ดที่เหมาะสมลงในช่องว่าง `<<a a>>` ~ `<<f f>>` เพื่อทำให้สมบูรณ์\n(Network Tech II-06REQUEST_reception.pdf, p.10-19)\n\n```python\n# แยกวิเคราะห์ Request Line\nreq_line = http_req[0]\nreq_method, req_uri, req_protocol = req_line.<<a a>>(\" \")\n\n# แยกวิเคราะห์ Request Header\nreq_headers = <<b b>>  # เริ่มต้น dictionary\n\n# วนลูปตั้งแต่บรรทัดที่ 1 (Header) จนถึงบรรทัดรองสุดท้าย (Header)\nfor keyvalue in http_req[1:<<c c>>]:\n    key, value = keyvalue.<<a a>>(<<d d>>)\n    req_headers[key] = value\n\nprint(f\"method is {req_method}\")\nprint(f\"request header is ...\\n{req_headers}\")\n\n# ตรวจสอบว่ามี Accept-Language header หรือไม่\nif <<e e>> in req_headers:\n    # ตรวจสอบ 2 ตัวอักษรแรกของค่า Accept-Language\n    if req_headers[\"Accept-Language\"][<<f f>>] == \"ja\":\n        message_body = \"こんにちはー\"\n    else:\n        message_body = \"Hello!\"\n```",
        "answer": "a: `split`\nb: `{}`\nc: `-1`\nd: `\": \"`\ne: `\"Accept-Language\"`\nf: `:2`"
    },
    # (q_1 から q_22 までの翻訳)
    # ...

    # --- シミュレーション2のここから追加 ---
    q_23: {
        "question": "1. (1) ในการเขียนโปรแกรมซ็อกเก็ต Python ต้อง `import` โมดูลชื่ออะไร? (Network Tech II-02server.pdf, p.12)",
        "answer": "`socket`"
    },
    q_24: {
        "question": "1. (2) ในการจัดการการขัดจังหวะ `[Ctrl]+[C]` จากคีย์บอร์ดใน Python ต้อง `import` โมดูลชื่ออะไร? (Network Tech II-02server.pdf, p.26)",
        "answer": "`signal`"
    },
    q_25: {
        "question": "1. (3) ช่วงหมายเลขพอร์ต 0-1023 เรียกว่าอะไร? (Network Tech II-02server.pdf, p.14)",
        "answer": "well-known port number (พอร์ตที่รู้จักกันดี)"
    },
    q_26: {
        "question": "1. (4) องค์ประกอบ 3 ส่วนที่ประกอบกันเป็นบรรทัดแรก (Request Line) ของ HTTP Request ตามลำดับคืออะไร? (Network Tech II-06REQUEST_reception.pdf, p.9)",
        "answer": "Method (เมธอด), Request-URI, HTTP-Version (เวอร์ชัน HTTP)"
    },
    q_27: {
        "question": "1. (5) องค์ประกอบ 3 ส่วนที่ประกอบกันเป็นบรรทัดแรก (Status Line) ของ HTTP Response ตามลำดับคืออะไร? (Network Tech II-05RESPONSE_test.pdf, p.10)",
        "answer": "Protocol (HTTP-Version), Status Code (รหัสสถานะ), Reason-Phrase (วลีบอกเหตุผล)"
    },
    q_28: {
        "question": "1. (6) เพราะเหตุใดจึงต้องใส่เมธอด `sendall` ไว้ในบล็อก `try...except`? จงบอกเหตุผล 2 ข้อเกี่ยวกับข้อยกเว้น (ข้อผิดพลาด) ที่คาดว่าจะเกิดขึ้น (Network Tech II-02server.pdf, p.18)",
        "answer": "1. เมธอด `encode` อาจล้มเหลวในการแปลงสตริงเป็นไบต์\n2. เมธอด `sendall` อาจล้มเหลวในการส่งข้อมูล"
    },
    q_29: {
        "question": "1. (7) จงอธิบายความแตกต่างที่ใหญ่ที่สุดระหว่าง `list` (ลิสต์) และ `tuple` (ทูเพิล) ใน Python (โดยเฉพาะเกี่ยวกับการเปลี่ยนแปลงค่า) (Network Tech II-01python.pdf, p.34)",
        "answer": "ลิสต์ (list) สามารถเปลี่ยนแปลงค่าได้ (Mutable) แต่ทูเพิล (tuple) ไม่สามารถเปลี่ยนแปลงค่าได้ (Immutable)"
    },
    q_30: {
        "question": "2. (1) (Network Tech II-01python.pdf, p.30)\n```python\nn = len(\"python\")\n```",
        "answer": "n = 6"
    },
    q_31: {
        "question": "2. (2) (Network Tech II-01python.pdf, p.30)\n```python\nn = max(5, 1, 10)\n```",
        "answer": "n = 10"
    },
    q_32: {
        "question": "2. (3) (Network Tech II-01python.pdf, p.33)\n```python\na = (10, 20, 30)\nn = a[1]\n```",
        "answer": "n = 20"
    },
    q_33: {
        "question": "2. (4) (Network Tech II-01python.pdf, p.32)\n```python\nb = [10]\nb.append(20)\nn = b\n```",
        "answer": "n = [10, 20]"
    },
    q_34: {
        "question": "2. (5) (Network Tech II-01python.pdf, p.32)\n```python\nb = [1]\nb.extend([2, 3])\nn = b\n```",
        "answer": "n = [1, 2, 3]"
    },
    q_35: {
        "question": "2. (6) (Network Tech II-01python.pdf, p.23)\n```python\na = 10\nif a > 10:\n    n = 1\nelif a == 10:\n    n = 2\nelse:\n    n = 3\n```",
        "answer": "n = 2"
    },
    q_36: {
        "question": "2. (7) (Network Tech II-06REQUEST_reception.pdf, p.19)\n```python\nreq_headers = {\"Host\": \"localhost\", \"Connection\": \"keep-alive\"}\nn = \"Host\" in req_headers\n```",
        "answer": "n = True"
    },
    q_37: {
        "question": "2. (8) (Network Tech II-06REQUEST_reception.pdf, p.19)\n```python\ns = \"Hello!\"\nn = s.replace(\"l\", \"x\")\n```",
        "answer": "n = 'hexxo'"
    },
    q_38: {
        "question": "2. (9) (Network Tech II-06REQUEST_reception.pdf, p.14)\n```python\nline = \"Host: localhost\"\nn = line.split(\": \")\n```",
        "answer": "n = ['Host', 'localhost']"
    },
    q_39: {
        "question": "2. (10) (Network Tech II-01python.pdf, p.30)\n```python\nn = type(\"abc\")\n```",
        "answer": "n = <class 'str'>"
    },
    q_40: {
        "question": "3. แผนภาพต่อไปนี้แสดงโครงสร้างของ request line ใน HTTP Request จงเติมคำที่เหมาะสมลงใน (a)-(c)\n(`Network Tech II-06REQUEST_reception.pdf`, p.9)\n\n`[ (a) ] [ (b) ] [ (c) ]`\n(ตัวอย่าง: `GET / HTTP/1.1`)\n\n(a):\n(b):\n(c):",
        "answer": "(a) Method (เมธอด)\n(b) Request-URI\n(c) HTTP-Version"
    },
    q_41: {
        "question": "4. ซอร์สโค้ดต่อไปนี้เป็นส่วนหนึ่งในฟังก์ชัน `commun` ของ `webserver.py` ที่ใช้ส่ง HTTP Response แบบขั้นต่ำสุด จงเติมโค้ดที่เหมาะสมลงในช่องว่าง `<<a a>>` ~ `<<e e>>` เพื่อทำให้สมบูรณ์\n(`Network Tech II-05RESPONSE_test.pdf`, p.11)\n```python\n# รหัสขึ้นบรรทัดใหม่ของ HTTP\nCRLF = <<a a>>\n\n# Status line\nstatus_line = f\"HTTP/1.1 200 OK\"\n# Message body\nmessage_body = \"こんにちはー\"\n\ntry:\n    # ส่ง status line และ CRLF\n    sock.sendall(f\"{status_line}{<<b b>>}\".<<c c>>())\n    \n    # ส่งบรรทัดว่าง (CRLF)\n    sock.sendall(<<d d>>.encode())\n    \n    # ส่ง message body\n    sock.sendall(<<e e>>.encode())\n\nexcept Exception as e:\n    print(f\"เกิดข้อยกเว้นใน commun:{e}\")\n```",
        "answer": "a: `\"\\r\\n\"`\nb: `CRLF`\nc: `encode`\nd: `CRLF`\ne: `message_body`"
    },
    q_42: {
        "question": "5. ซอร์สโค้ดต่อไปนี้เป็นฟังก์ชันที่ใช้ใน `webserver.py` เพื่อดึงข้อมูล HTTP Request ทีละบรรทัด (จนถึง CRLF) จงเติมโค้ดที่เหมาะสมลงในช่องว่าง `<<a a>>` ~ `<<e e>>` เพื่อทำให้สมบูรณ์\n(`Network Tech II-05RESPONSE_test.pdf`, p.25)\n```python\ndef extract_row(sock, recv_unit=1, delim=<<a a>>):\n    req = \"\"\n    \n    # วนลูปจนกว่าจะพบ delim\n    while req.<<b b>>(delim) < 0:\n        \n        # รับข้อมูลทีละ 1 ไบต์\n        data = sock.<<c c>>(recv_unit)\n        \n        # ถ้าไม่มีข้อมูล ให้ออกจากลูป\n        if not <<d d>>:\n            break\n            \n        # ถอดรหัสข้อมูลที่ได้รับและนำมาต่อกัน\n        req += data.<<e e>>()\n        \n    return req\n```",
        "answer": "a: `\"\\r\\n\"`\nb: `find`\nc: `recv`\nd: `data`\ne: `decode`"
    },
    q_43: {
        "question": "6. ซอร์สโค้ดต่อไปนี้เป็นตัวอย่างการจัดการข้อยกเว้น (try-except-finally) ใน Python จงเติมโค้ดที่เหมาะสมลงในช่องว่าง `<<a a>>` ~ `<<d d>>` เพื่อทำให้สมบูรณ์\n(`Network Tech II-01python.pdf`, p.36-37)\n```python\na = [10, 20]  # มี 2 องค์ประกอบ (index 0, 1)\n\n<<a a>>:\n    # วนลูป 3 ครั้ง (i = 0, 1, 2)\n    for i in range(3):\n        # เกิดข้อผิดพลาดที่ i=2 เมื่อพยายามเข้าถึง a[2]\n        print(a[i])\n\n# จัดการเมื่อเกิด IndexError\n<<b b>> <<c c>> as err:\n    print(f\"เกิดข้อผิดพลาด: {err}\")\n\n# ทำงานส่วนนี้เสมอไม่ว่าจะเกิดข้อผิดพลาดหรือไม่\n<<d d>>:\n    print(\"การประมวลผลสิ้นสุดลง\")\n```",
        "answer": "a: `try`\nb: `except`\nc: `IndexError`\nd: `finally`"
    }
   
    # --- シミュレーション2のここまで ---
}