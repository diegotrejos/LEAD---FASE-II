#!/usr/bin/env python
from collections import deque
import time

print('Que tantos segundos esperar')
num=input()
#reviso que ingreso sea un numero
try:
	
	val=int(num)
	tiempo = val
except:
	print("Eso no es un numero, se pondran 5 segundos")
	tiempo = 5

#esto esta en cliente
oracion = ''
cola = deque()
while oracion != '1': 
	oracion = str(input('Digite su oracion\n'))
	#
	#cuenta palabras
	print ('contando palabras en oracion:', oracion)
	resultado = len(oracion.split())
	#guarda en cola
	cola.append(resultado)
	#print(cola)
	#espera 5 segundos
	time.sleep(tiempo);
	
#envio datos a cliente
cola.popleft()
print(cola)
