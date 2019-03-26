#!/usr/bin/env python
import threading
import socket
import queue

def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def validate_conn_port(s):
	if s < 0 or s > 65535:
		return False
	else:
		return True
	
	
def leerConsola():
	# leer input de consola que pide imprimir lo del IP
	b2 = False
	while b2 == False:
		decision = input('Quiere digitar un IP o un puerto [ip/pu]? \n')
		if decision == 'ip':
			b2 = True
		elif decision == 'pu':
		  	b2 = True
		else:
		  	print("Input invalido")

	b = False
	if decision == 'ip':
		while b == False:
			y = input('Digite el IP: \n')
			b = validate_ip(y)
	else:
		while b == False:
			y = int(input('Digite el puerto: \n'))
			if 0 <= y <= 65535:
				b = True

def enviar():
	# Sacar la oracion del queue, usar lock del queue
	item = cola.get(true)
	resultado = len(item.split())
	#resultado = len(oracion.split())
	conn.send(resultado)
	#conn.send(resultado)


def recibir():
	while True:
		print("Listening\n")
		data = conn.recv(BUFFER_SIZE)
		data2 = data.decode()
		cola.put(data2)
		if not data2: break
		print("received data:", data2)
		  
TCP_IP = '192.168.0.6'
TCP_PORT = int(input("ingrese el puerto de conexion\n"))
BUFFER_SIZE = 1024  
while(not validate_conn_port(TCP_PORT)):
	TCP_PORT = int(input("ingrese el puerto de conexion\n"))	
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((TCP_IP, TCP_PORT))
socket.listen(1)
conn, addr = socket.accept()
print(conn)
print('Connection address:', addr)


cola = queue.Queue()


class MyThread (threading.Thread):
	def __init__(self, threadID): #override del constructor
		threading.Thread.__init__(self)
		self.threadID = threadID

	def run(self):
		if self.threadID == 0:
			# Lea
			print("Soy el Thread 0")
			recibir()
		elif self.threadID == 1:
			# Envie
			print("Soy el Thread 1")
			enviar()
		else: #Thread 2
			print("Soy el Thread 2")
			leerConsola() # Valorador IP Andres


conn.close()
