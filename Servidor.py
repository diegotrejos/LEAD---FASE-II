#!/usr/bin/env python
import socket
import queue

TCP_IP = '10.1.137.235'
TCP_PORT = 5050  # Pedirlo por consola o argumento
BUFFER_SIZE = 1024  

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
		else if self.threadID == 1:
			# Envie
			print("Soy el Thread 1")
			enviar()
		else: #Thread 2
			print("Soy el Thread 2")
			leerConsola() # Valorador IP Andres


def leerConsola():
	# leer input de consola que pide imprimir lo del IP



def enviar():
	# Sacar la oracion del queue, usar lock del queue
	#resultado = len(oracion.split())
	#conn.send(resultado)
	




def recibir():
	while True:
		print("Listening\n")
		data = conn.recv(BUFFER_SIZE)
		data2 = data.decode()
		cola.put(data2)
		if not data2: break
		print("received data:", data2)
		  

conn.close()
