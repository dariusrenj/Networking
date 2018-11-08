"""
Name: Zackery Vering
Project: Lab 4A
Date: 26 Sept 2018
"""
#import sockets
from socket import *
import select
#set up sockets
server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('192.168.31.132', 1313))
#start listening
server.listen(5)
clientList = [server]
#loop 
while (True):
    incli, outcli, errcli = select.select(clientList,[],[])
    for clients in clientList:
        if clients == server:
            clients,addr = server.accept()    
            clientList.append(clients)
            print clientList
        else:
            data = clients.recv(1024)
            for clients in incli:
                if clients == server:
                    continue
                else:
                    clients.send(clients+'\n'+data)
clients.close()
server.close()