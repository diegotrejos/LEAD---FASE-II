#!/usr/bin/env python

import socket


TCP_IP = '10.1.137.235'
TCP_PORT = 5050
BUFFER_SIZE = 1024  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print(conn)
print('Connection address:', addr)
while 1:
	print("Listening\n")
	data = conn.recv(BUFFER_SIZE)
	data2 = data.decode()
	if not data2: break
	print("received data:", data2)
	conn.send(data)  # echo
conn.close()
