#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

s.connect((host,port))

msg = s.recv(1024) #recieve no more than 1024 bytes

#s.close()

print(msg.decode('ascii'))