#coding: utf-8
from socket import AF_INET, SOCK_STREAM, socket

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 1000
    ADDR = (HOST, PORT)

    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    while True:
        pass