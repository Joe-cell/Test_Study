# -*- coding: utf-8 -*-
"""
@author: Joe_xu
@time: 2019/7/7 17:18
"""
import socket


def main():
    # 创建TCP套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    tcp_socket.connect(("192.168.3.4", 8080))
    # 可以使用套接字收发数据
    tcp_socket.send(b"123")
    # 关闭套接字
    tcp_socket.close()
    pass


if __name__ == "__main__":
    main()
