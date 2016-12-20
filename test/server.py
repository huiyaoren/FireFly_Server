#coding:utf8
import os
import sys
from firefly.netconnect.protoc import LiberateFactory
from firefly.utils import services
from twisted.internet import reactor
from twisted.python import log

if os.name != 'nt': # 不是 NT 系统的话使用 epoll
    from twisted.internet import epollreactor
    epollreactor.install()

def command_1(_conn, data):
    print('233~')
    print(data)

if __name__ == '__main__':
    # 日志输出
    log.startLogging(sys.stdout)

    # 服务 服务端数据的逻辑处理
    # service = services.Service("testService")
    service = services.CommandService("testService")

    # 添加命令码处理
    service.mapTarget(command_1)

    # 工厂类 用于处理数据封装 协议头封装 分包 粘包的处理
    factory = LiberateFactory()

    # 关于 twisted
    reactor = reactor

    # 添加服务通道
    factory.addServiceChannel(service)

    # 开始监听端口
    reactor.listenTCP(1000, factory)
    reactor.run()
