"""
Name: Zackery Vering
Project: Lab 3a
Date: 24 Sept 2018
"""
#import socket
from socket import *
import struct

#set up socket
s = socket(AF_INET, SOCK_STREAM)
s.bind(("192.168.31.132", 1313))
#start listening
s.listen(5)
c,a = s.accept()
#loop until the kill command of 'close' is given
data = c.recv(1024)
print("Little Endian: {}".format(struct.unpack('<HIhi',data)))
print("Big Endian: {}".format(struct.unpack('>HIhi',data)))
#close the connection
c.close()