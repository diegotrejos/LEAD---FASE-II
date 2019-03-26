#!/usr/bin/env python
import socket
import queue
import time
import threading
import pair


cola = queue.Queue()
listaResultados = []

sem1 = threading.Semaphore(0) #semaforo 1
sem2 = threading.Semaphore(0) #semafoto 2

BUFFER_SIZE = 1024

mySocket = ''

class MyThread (threading.Thread):
	def __init__(self, threadID): #override del constructor
		threading.Thread.__init__(self)
		self.threadID = threadID

	def run(self):
		if self.threadID == 0:
			# Lea
			lector()
		else:
			# Envie
			enviar()

def comunicacionSocket():
	global mySocket
	TCP_IP = input('Ingrese el IP del servidor\n')
	TCP_PORT = input('Ingrese el puerto por el cual se comunicaran\n')
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mySocket.connect((TCP_IP, int(TCP_PORT)))
				

def imprimirResultados():
	for pair in listaResultados:
		print(str(pair.oracion) + ": " + str(pair.cantidadPalabras))

def lector():
	mensaje = " "
	while mensaje != "1":
		mensaje = input('Digite su oracion\n')
		#print(mensaje)
		myPair = pair.Pair(mensaje)
		listaResultados.append(myPair)
		cola.put(myPair)
		sem1.release()
	# Aqui sigue cuando lo que se encuentra es un 1
	sem2.acquire()
	imprimirResultados()

def enviar():
	contador = 0
	seguir = True
	while seguir:
		sem1.acquire()
		while cola.empty() == False:
			mensj = cola.get().oracion
			if mensj == "1":
				seguir = False
				sem2.release()
			#mySocket.send(mensj.encode())
			#data = mySocket.recv(BUFFER_SIZE)
			#list[contador].cantidadPalabras = data.decode()
			contador += 1
			sem1.release()	
			
			

comunicacionSocket() # Arma socket pidiendo IP y puerto

thread0 = MyThread(0)
thread1 = MyThread(1)
thread0.start()
thread1.start()
thread0.join()
thread1.join()

#socket.close()
