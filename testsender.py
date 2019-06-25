#!/usr/bin/env python
import socket
from a_aPaq import a_aPaq
UDP_IP = "10.1.137.29"
UDP_PORT=8888




test = a_aPaq(0,1,"hola",('10.1.137.166',8888))#mete de un solo en cola de entrada
MESSAGE = test.serialize()
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE,(UDP_IP,UDP_PORT)) 
