import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#ソケットの作成

    s.connect(('127.0.0.1',50007))#サーバーの指定
    s.sendall(b'hallo world')#メッセージの送信

    data = s.recv(1024)#データの受信

    print(repr(data))
    
    