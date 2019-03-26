#!/usr/bin/env python
import socket
import queue
import time
import threading
import pair

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

TCP_IP = '192.168.205.131'
TCP_PORT = 5050
BUFFER_SIZE = 1024

#socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.connect((TCP_IP, TCP_PORT))


cola = queue.Queue()
listaResultados = []

sem1 = threading.Semaphore(0) #semaforo 1
sem2 = threading.Semaphore(0) #semafoto 2



def imprimirResultados():
	for pair in listaResultados:
		print(str(pair.oracion) + ": " + str(pair.cantidadPalabras))



def lector():
	num=input('Introduzca la espera en segundos: \n')
	#reviso que ingreso sea un numero
	try:
		val=int(num)
		tiempo = val
	except:
		print("Eso no es un numero, se pondran 5 segundos")
		tiempo = 5
	
	mensaje = " "
	
	while mensaje != "1":
		mensaje = input('Digite su oracion\n')
		#print(mensaje)
		myPair = pair.Pair(mensaje)
		listaResultados.append(myPair)
		cola.put(myPair)
		sem1.release()
	# Aqui sigue cuando lo que se encuentra es un 1
	print("Soy el thread 0 y estoy esperando por el queue")
	sem2.acquire()
	imprimirResultados()

def enviar():
	global contador
	seguir = True
	while seguir:
		sem1.acquire()
		while cola.empty() == False:
			mensj = cola.get().oracion
			if mensj == "1":
				seguir = False
				sem2.release()
				print("Release del semaforo 2")
			#socket.send(mensj.encode())
			#data = socket.recv(BUFFER_SIZE)
			#list[contador].cantidadPalabras = data.decode()
			contador += 1
			sem1.release()			

			
contador = 0

thread1 = MyThread(0)
thread2 = MyThread(1)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
#socket.close()
