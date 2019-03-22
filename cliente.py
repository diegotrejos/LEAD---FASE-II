#!/usr/bin/env python

import socket


TCP_IP = '10.1.138.31'
TCP_PORT = 5020
BUFFER_SIZE = 1024
#MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
message = input("Escriba una linea\n")
#mes = list(message)
s.send(message.encode())
data = s.recv(BUFFER_SIZE)
s.close()
print (data.decode())
