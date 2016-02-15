"""
Handshake Data

Chrome：

GET / HTTP/1.1
Upgrade: websocket
Connection: Upgrade
Host: 127.0.0.1:1337
Sec-WebSocket-Origin: http://127.0.0.1:8000
Sec-WebSocket-Key: erWJbDVAlYnHvHNulgrW8Q==
Sec-WebSocket-Version: 8
Cookie: csrftoken=xxxxxx; sessionid=xxxxx

Firefox：

GET / HTTP/1.1
Host: 127.0.0.1:1337
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:8.0) Gecko/20100101 Firefox/8.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip, deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Connection: keep-alive, Upgrade
Sec-WebSocket-Version: 8
Sec-WebSocket-Origin: http://127.0.0.1:8000
Sec-WebSocket-Key: 1t3F81iAxNIZE2TxqWv+8A==
Cookie: xxx
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket

Safari：

GET / HTTP/1.1
Upgrade: WebSocket
Connection: Upgrade
Host: 127.0.0.1:1337
Origin: http://127.0.0.1:8000
Cookie: sessionid=xxxx; calView=day; dayCurrentDate=1314288000000
Sec-WebSocket-Key1: cV`p1* 42#7  ^9}_ 647  08{
Sec-WebSocket-Key2: O8 415 8x37R A8   4
;"######
"""

