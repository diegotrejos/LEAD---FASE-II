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

def comunicacionSocket():
	global mySocket
	
	TCP_IP = input('Ingrese el IP del servidor\n')
	while(not(validate_ip(TCP_IP))):
		TCP_IP = input('Ingrese un IP valido para el servidor\n')
	
	TCP_PORT = input('Ingrese el puerto por el cual se comunicaran\n')
	while(not(validate_conn_port(int(TCP_PORT)))):
		TCP_PORT = input('Ingrese un puerto valido por el cual comunicarse\n')
	
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mySocket.connect((TCP_IP, int(TCP_PORT)))
				

def imprimirResultados():
	cantidad = 1
	print("Imprimiendo...")
	for pair in listaResultados:
		print(str(cantidad) + ": " + str(pair.oracion) + ": " + str(pair.cantidadPalabras))
		cantidad += 1

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
			mySocket.send(mensj.encode())
			data = mySocket.recv(BUFFER_SIZE)
			listaResultados[contador].cantidadPalabras = data.decode()
			contador += 1
			sem1.release()	

comunicacionSocket() # Arma socket pidiendo IP y puerto

thread0 = MyThread(0)
thread1 = MyThread(1)
thread0.start()
thread1.start()
thread0.join()
thread1.join()

mySocket.close()


#10.1.137.25 
