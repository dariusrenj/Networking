"""
Name: Zackery Vering
Project: Lab 2C
Date: 21 Sept 2018
"""
from socket import *
#set up socket
s = socket(AF_INET, SOCK_STREAM)
s.bind(("192.168.31.128", 1313))
#start listening
s.listen(5)
c,a = s.accept()
pineapple = True
#loop until the kill command of 'close' is given
count = 0
while(pineapple == True):
    data = c.recv(1024)
    print("{}").format(data)
    c.send("Ok")
    count +=1
    if (count ==3):
        pineapple = False
c.close()


