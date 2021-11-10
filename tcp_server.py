import socket #ネットワークインターフェース

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s: #ソケットの作成
    #AF_INET(host,port) hostはIPv4アドレス,portは整数
    s.bind(('127.0.0.1',50007))

    s.listen(1)#アクセス待ち

    while True:

        conn, addr =s.accept()#アクセスされたらアドレスを入力する
        with conn:
            while True:

                data = conn.recv(1024)#データの受信
                if not data:
                    break
                print('data : {}, addr: {}'.format(data,addr))

                conn.sendall(b'Received:' + data)#メッセージの送信