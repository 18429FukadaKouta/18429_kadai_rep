import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#ソケットの作成

    s.connect(('10.40.2.35',50007))#サーバーの指定
    s.sendall(b'hallo')#メッセージの送信

    data = s.recv(1024)#データの受信

    print(repr(data))
    
    