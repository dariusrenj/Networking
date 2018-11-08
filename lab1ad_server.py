"""
Name: Zackery Vering
Project: Lab 1C
Date: 19 Sept 2018
"""
#import socket
from socket import *
#set up socket
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("", 1313))

#loop
while(True):
    data, addr = s.recvfrom((1024), ("localhost", 1313))
    print("{} {}").format(data, addr)
    s.sendto("OK", addr)
#send 'Goodbye' and close the connection
s.sendto("Goodbye", addr)
s.close()