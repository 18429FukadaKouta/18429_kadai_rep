import socket

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as a:
    a.bind(("0.0.0.0",50007))
    while True:
        b, ad = a.recvfrom(1024)
        print("data: {}, addr: {}".format(b, ad))