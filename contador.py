#!/usr/bin/env python
import queue
import time
import pair

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
cola = queue.Queue()
while oracion != '1': 
	oracion = str(input('Digite su oracion\n'))
	#Crea un objeto pair
	myPair = pair.Pair(oracion)
	
	#cuenta palabras
	print ("Contando palabras en oracion: ", oracion)
	resultado = len(oracion.split())
	myPair.cantidadPalabras = resultado
	
	#guarda en cola
	cola.put(myPair)
	#print(cola)
	cola.get().printPair()
	#espera 5 segundos
	
	time.sleep(tiempo);	
#envio datos a cliente


