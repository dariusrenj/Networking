"""
Name: Zackery Vering
Project: Lab 1A-D
Date: 19 Sept 2018
"""
#import sockets
from socket import *
#set up sockets
s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.31.128", 1313))
banana = True
#loop and allow user to send to the server until the server says 'Goodbye'
#server will say 'Goodbye' when the client sends 'close'. Case sensitive
while (banana == True):
    sending = s.send(raw_input("What would you like to send?\n"))
    if (sending == 5):
        data = s.recv(1024)
        print("{}").format(data)
        if (data == "Goodbye"):
            banana = False
s.close()