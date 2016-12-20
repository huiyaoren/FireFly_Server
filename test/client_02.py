#coding:utf8

from socket import AF_INET, SOCK_STREAM, socket
import struct

def send_data(send_str, command_id):
    HEAD_0 = chr(0) # 协议头0
    HEAD_1 = chr(0) # 协议头1
    HEAD_2 = chr(0) # 协议头2
    HEAD_3 = chr(0) # 协议头3
    ProtoVersion = chr(0) # 协议头版本号
    ServerVersion = 0 # 服务器版本号
    send_str = send_str

    # 打包头部信息
    data = struct.pack(
        '!sssss3I',
        HEAD_0,
        HEAD_1,
        HEAD_2,
        HEAD_3,
        ProtoVersion,
        ServerVersion,
        len(send_str) + 4,
        command_id
    )

    send_data = data + send_str
    return send_data

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 1000
    ADDR = (HOST, PORT)

    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)
    client.sendall(send_data('hello server', 1))
    while True:
        pass