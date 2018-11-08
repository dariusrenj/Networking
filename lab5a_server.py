"""
Name: Zackery Vering
Project: Lab 5a
Date: 28 Sept 2018
"""
#import socket
from socket import *
import random

#set up socket
s = socket(AF_INET, SOCK_STREAM)
s.bind(("192.168.31.132", 1313))
#start listening
s.listen(5)
c,a = s.accept()
number = random.randint(0, 100)
isWrong = True
#loop until the kill command of 'close' is given
while (isWrong == True):
    data = int(c.recv(1024))
    print number
    print data
    if (data == number):
        c.send("You guessed right!")
        c.close()
        isWrong = False
    else:
        if (data < number):
            c.send("Guess higher")
        else:
            c.send("Guess lower.")
#close the connection
s.close()