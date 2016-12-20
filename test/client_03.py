# coding:utf8

import socket
import struct
from thread import start_new


def sendData(sendstr, commandId):
    '''定义协议头'''
    HEAD_0 = chr(0)
    HEAD_1 = chr(0)
    HEAD_2 = chr(0)
    HEAD_3 = chr(0)
    ProtoVersion = chr(0)
    ServerVersion = 0
    sendstr = sendstr
    data = struct.pack(
        '!sssss3I',
        HEAD_0,
        HEAD_1,
        HEAD_2,
        HEAD_3,
        ProtoVersion,
        ServerVersion,
        len(sendstr) + 4,
        commandId
    )
    senddata = data + sendstr
    return senddata

def resolveRecvdata(data):
    '''解析数据，根据定义的协议头解析服务器返回的数据'''
    head = struct.unpack(
        '!sssss3I',
        data[:17]
    )
    lenght = head[6]
    message = data[17:17+lenght]
    return message

def sendMessage(connection):
    '''发送信息'''
    while 1:
        data = raw_input()
        length = len(data)
        if length > 80:
            length = 80
        line = length * '-'
        data += '\r\n' + line
        connection.sendall(sendData(data, 10001)) # 向服务器发送信息
        print line

def receiveMessage(connection):
    '''接收消息'''
    while 1:
        message = connection.recv(1024) # 接收服务器返回的消息
        message = resolveRecvdata(message) # 解析消息
        print message

class ChatServer:

    def __init__(self, port):
        self.port = port
        self.srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.connect(('127.0.0.1', port))

    def run(self):
        start_new(sendMessage, (self.srvsock,))
        start_new(receiveMessage, (self.srvsock,))

if __name__ == '__main__':
    myServer = ChatServer(1000).run()
    while 1:
        pass


