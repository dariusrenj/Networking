"""
Name: Zackery Vering
Project: Lab 2B
Date: 21 Sept 2018
"""
from socket import *
import json
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("192.168.31.128",13000))

while True:
    data, addr = s.recvfrom(1024)
    print ("{}").format(json.loads(data))
    print addr
    resp = "It worked."
    s.sendto(resp,addr)
