import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as hensu:
    hensu.sendto(b'Hello UDP world',('127.0.0.1',50007))