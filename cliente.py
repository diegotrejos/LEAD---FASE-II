#!/usr/bin/env python

import socket
from collections import deque
import time

TCP_IP = '10.1.138.31'
TCP_PORT = 5020
BUFFER_SIZE = 1024
#MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

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

num=input('Introduzca la espera en segundos: \n')
#reviso que ingreso sea un numero
try:
	val=int(num)
	tiempo = val
except:
	print("Eso no es un numero, se pondran 5 segundos")
	tiempo = 5
message = ''
while message != '1':
	message = input('Digite su oracion\n')
	#mes = list(message)
	s.send(message.encode())
	time.sleep(tiempo);
data = s.recv(BUFFER_SIZE)
s.close()
print (data.decode())
