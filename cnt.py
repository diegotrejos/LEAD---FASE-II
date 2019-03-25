#!/usr/bin/env python
from collections import deque
import time
import threading

print('Que tantos segundos esperar')
num=input()
#reviso que ingreso sea un numero
try:	
	val=int(num)
	tiempo = val
except:
	print("Eso no es un numero, se pondran 5 segundos")
	tiempo = 5





#creo una cola
cola = deque()

#hilo
def worker():
	#esto esta en cliente, seria el que recibe los datos 
	while oracion != 1:
		print('Digite su oracion')
		oracion = str(input())
	#
	#cuenta palabras
		print ('contando palabras en oracion:', oracion)
		resultado = len(oracion.split())
	#guarda en cola
		cola.append(resultado)
		print(cola)

while message != '1':
	if cola:
	#si no esta vacia
	#espera 5 segundos
		time.sleep(tiempo);
		message=cola.popleft()
	#envio datos a cliente
	else:
	#esta vacia


t=threading.Thread(target=worker)
threads.append(t)
t.start()
print(cola)


