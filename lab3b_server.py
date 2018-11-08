"""
Name: Zackery Vering
Project: Lab 2B
Date: 21 Sept 2018
"""
from socket import *
#set up socket
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("192.168.31.132",1300))
#receive data
data, addr = s.recvfrom(1024)
#split data
userInput = data.split()
userInput = sorted(userInput, key=len)
#set up response
resp = ""
for i in range(len(userInput)):
    if i == 0:
        resp = resp + userInput[i]
    else:
        resp = resp + " " + userInput[i]
#print address received from, define new address, print new address and response
print addr
address = addr[1]
address = address + 1
print address
print resp
#close socket
s.close()
#set up new socket to send from
ns = socket(AF_INET, SOCK_DGRAM)
ns.bind(("192.168.31.132",address))
#send response
ns.sendto(resp,("192.168.31.131", address))
ns.close()