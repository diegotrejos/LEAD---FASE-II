#!/usr/bin/env python
import socket
import queue
import time
import threading

TCP_IP = '10.1.138.31'
TCP_PORT = 5020
BUFFER_SIZE = 1024
#MESSAGE = "Hello, World!"

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))

######################################################################################
#esto esta en cliente

#cola = deque()

#while oracion != '1': 
#	oracion = str(input())
	#
	#cuenta palabras ESTO VA PARA EL SERVIDOR
	#print ('contando palabras en oracion:', oracion)
	#resultado = len(oracion.split())
	#guarda en cola
	#cola.append(resultado)
	#print(cola)
	#espera 5 segundos
	
	
#envio datos a cliente
#cola.popleft()
#print(cola)
#####################################################################################



class MyThread (threading.Thread):
	def __init__(self, threadID): #override del constructor
		threading.Thread.__init__(self)
		self.threadID = threadID

	def run(self):
		if self.threadID == 0:
			# Lea
			print("Soy el Thread 0")
		else:
			# Envie
			print("Soy el Thread 1")
			
thread1 = MyThread(0)
thread2 = MyThread(1)
thread1.start()
thread2.start()
thread1.join()
thread2.join()


def lector():
	num=input('Introduzca la espera en segundos: \n')
	#reviso que ingreso sea un numero
	try:
		val=int(num)
		tiempo = val
	except:
		print("Eso no es un numero, se pondran 5 segundos")
		tiempo = 5
	message = ''
	cola = queue.Queue()
	#cola_2 = Queue()
	while message != '1':
		message = input('Digite su oracion\n')
		print(message)
		#mes = list(message)
		cola.put(message)
		#s.send(message.encode())
		#data = s.recv(BUFFER_SIZE)
		#cola_2.put(data.decode())	
		time.sleep(tiempo)
		# print(cola)
	#s.close()
	
lector()
