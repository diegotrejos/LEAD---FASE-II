#!/usr/bin/env python
import threading
import socket
import queue
import time


cola = queue.Queue()

BUFFER_SIZE = 1024 

tiempo = 5

conn = ''
addr = ''
mySocket = ''
TCP_IP = ''
TCP_PORT = ''

semCola = threading.Semaphore(0) #semaforo cola

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
			y = int(input('Digite el puerto: \n')) #10.1.137.25 
			if 0 <= y <= 65535:
				b = True

def enviar():
	seguir = True
	while seguir:
		semCola.acquire()
		while cola.empty() == False:
			oracion = cola.get()
			if oracion == "1":
				seguir = False
			resultado = len(oracion.split())
			conn.send(str(resultado).encode())
			time.sleep(tiempo)


def recibir():
	seguirRecibiendo = True
	while seguirRecibiendo:
		print("Escuchando")
		data = conn.recv(BUFFER_SIZE)
		data2 = data.decode()
		if data2 == "1":
			seguirRecibiendo = False
		print("Lo que me llego: " + data2)
		cola.put(data2)
		semCola.release()
		#if not data2: break
		#print("received data: ", data2)
		  

def pedirRetardo():
	global tiempo
	num = input('Introduzca la espera en segundos: \n')
	#reviso que ingreso sea un numero
	try:
		val = int(num)
		tiempo = val
	except:
		print("Eso no es un numero, se pondran 5 segundos")
			
			
def comunicacionSocket():
	global conn
	global addr
	global mySocket
	global TCP_IP
	global TCP_PORT
	TCP_IP = input('Ingrese el IP del servidor\n')
	TCP_PORT = input('Ingrese el puerto por el cual se comunicaran\n')
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mySocket.bind((TCP_IP, int(TCP_PORT)))
	mySocket.listen(1) 
	conn, addr = mySocket.accept()
	print(conn)
	print('Connection address:', addr)

	
	
pedirRetardo()
comunicacionSocket()

thread0 = MyThread(0)
thread1 = MyThread(1)
#thread2 = MyThread(2)
thread0.start()
thread1.start()
#thread2.start()
thread0.join()
thread1.join()
#thread2.join()

conn.close()

#192.168.205.131
