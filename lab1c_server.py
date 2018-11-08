"""
Name: Zackery Vering
Project: Lab 1c
Date: 21 Sept 2018
"""
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("192.168.31.128",13000))

while True:
    data, addr = s.recvfrom(1024)
    print data
    print addr
    resp = "It worked."
    s.sendto(resp,addr)
