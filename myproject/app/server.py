#coding:utf8

from firefly.server.globalobject import netserviceHandle
from firefly.server.globalobject import GlobalObject
from datetime import *

def doConnectionMade(conn):
    '''连接建立时调用的方法'''
    str1 = 'welcome\r\n'
    GlobalObject().netfactory.pushObject(10001, str1, [conn.transport.sessionno])

    str2 = '{0} is login\r\n'.format(conn.transport.sessionno)
    lis = GlobalObject().netfactory.connmanager._connections.keys() # 获取所有在线用户
    lis.remove(conn.transport.sessionno) # 移除登录者本身
    GlobalObject().netfactory.pushObject(1000, str2, lis) # 向用户群发送当前登录者登录信息

def doConnectionLost(conn):
    '''连接断开时调用的方法'''
    str2 = '{0} is logout\r\n'.format(conn.transport.sessionno)
    lis = GlobalObject().netfactory.connmanager._connections.keys() # 获取所有在线用户
    lis.remove(conn.transport.sessionno) # 移除下线者本身
    GlobalObject().netfactory.pushObject(10001, str2, lis) # 向用户群发送当前下线者下线信息

GlobalObject().netfactory.doConnectionMade = doConnectionMade # 绑定登录方法到框架
GlobalObject().netfactory.doConnectionLost = doConnectionLost # 绑定下线方法到框架

@netserviceHandle
def speak_10001(_conn, data):
    '''用户发言的方法'''
    date = datetime.now()
    str1 = date.strftime("%Y-%m-%d %H:%M:%S") + '(' + str(_conn.transport.sessionno) + '):\r\n' + data
    lis = GlobalObject().netfactory.connmanager._connections.keys() # 获取所有在线用户
    lis.remove(_conn.transport.sessionno) # 移除发言者本身
    GlobalObject().netfactory.pushObject(10001, str1, lis) # 向用户群发送当前发言者的发言信息