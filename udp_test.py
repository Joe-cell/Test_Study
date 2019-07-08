# -*- coding: utf-8 -*-
"""
@author: Joe_xu
@time: 2019/7/6 21:34
"""
import socket


def main():
    # 创建UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind(("", 7890))
    # 可以使用套接字收发数据
    udp_socket.sendto(b"hahaha", ("127.0.0.1", 8080))
    # 关闭套接字
    udp_socket.close()
    pass


if __name__ == "__main__":
    main()
