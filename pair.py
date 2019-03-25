class Pair:
	def __init__(self, oracion, cantidadPalabras = 0):	
		self.oracion = oracion
		self.cantidadPalabras = cantidadPalabras
		
	def printPair(self):
		print(self.oracion + ": " + str(self.cantidadPalabras))