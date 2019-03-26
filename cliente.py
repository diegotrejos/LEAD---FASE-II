#!/usr/bin/env python
import socket
import queue
import time
import threading
import pair
import asyncio

TCP_IP = '192.168.0.6'
TCP_PORT = 5000
BUFFER_SIZE = 1024


mensaje = ""

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((TCP_IP, TCP_PORT))


cola = queue.Queue()
semaforo1 = asyncio.Semaphore(0)
lista_resultados = []
counter = 0

def lector():
	num=input('Introduzca la espera en segundos: \n')
	#reviso que ingreso sea un numero
	try:
		val=int(num)
		tiempo = val
	except:
		print("Eso no es un numero, se pondran 5 segundos")
		tiempo = 5
	
	while mensaje != "1":
		mensaje = input('Digite su oracion\n')
		#print(mensaje)
		myPair = pair.Pair(mensaje)
		listaResultados.append(myPair)
		cola.put(myPair)
		semaforo1.release()
		
	


def enviar():
	seguir = True
	while seguir:
		semaforo1.acquire()
		mensj = cola.get().oracion
		if mensj == "1":
			seguir = False
		socket.send(mensj.encode())
		data = socket.recv(BUFFER_SIZE)
		list[counter].cantidadPalabras = data.decode()
		counter = counter + 1
		
class MyThread (threading.Thread):
	def __init__(self, threadID): #override del constructor
		threading.Thread.__init__(self)
		self.threadID = threadID

	def run(self):
		if self.threadID == 0:
			# Lea
			print("Soy el Thread 0")
			lector()
		else:
			# Envie
			print("Soy el Thread 1")
			enviar()
			
			
thread1 = MyThread(0)
thread2 = MyThread(1)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
socket.close()
