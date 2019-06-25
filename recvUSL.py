import socket
from uslPaq import uslPaq
   
class senderUSL:    
	def main():   
		UDP_IP = "127.0.0.1"
		UDP_PORT = 5005
		
		uslPrueba = uslPaq(0,0,'no')

		sock = socket.socket(socket.AF_INET, # Internet
							socket.SOCK_DGRAM) # UDP
		sock.bind((UDP_IP, UDP_PORT))

		while True:
		   data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		   uslPrueba.unserialize(data)
		   print ("received message:", uslPrueba.payload[0:])
		   print ("SN: ", uslPrueba.sn)
		   print ("Tipo: ", uslPrueba.tipo)

	if __name__== "__main__":
	  main()
