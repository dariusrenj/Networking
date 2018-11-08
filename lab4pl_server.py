"""
Name: Zackery Vering
Project: Lab 4PL
Date: 26 Sept 2018
"""
#import socket
from socket import *
import struct
import binascii

#set up socket
s = socket(AF_INET, SOCK_STREAM)
s.bind(("192.168.31.132", 1313))
#start listening
s.listen(5)
c,a = s.accept()
#loop until the kill command of 'close' is given
data = struct.unpack('<HIihi',c.recv(1024))
print data
userList = []
userList.append(data[0])
userList.append(data[1])
userList.append(str(unichr(data[2])))
userList.append(hex(data[3]))
userList.append(bin(data[4]))
print userList
c.send(struct.pack('=HIihi', data[0],data[1],data[2],data[3],data[4]))
#close the connection
c.close()