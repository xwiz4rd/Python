#!/usr/bin/python
import socket
ip = raw_input("Digite o ip: ")
porta = input("Digite a porta: ")

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if soc.connect_ex((ip, porta)):
	print "Porta fechada"
else:
	print("Porta aberta")
