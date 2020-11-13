"""
10: Skriv en klient/server applikation, hvor klienten skal åbne en tekstfil
(f.eks. words.txt) og sende ordene til serveren via en TCP socket.
Serveren skal så gemme ordene i en liste, ét ord i hver indgang i listen.
F.eks. hvis tekstfilen indeholder ordene: Stakit Stativ Kasket,
skal listen være [”Stakit”, ”Stativ”, ”Kasket”].
Når klienten ikke sender flere ord (fordi alle ordene i filen er blevet sendt),
skal serveren gemme ordene i listen i en anden tekst fil
(vælg selv navnet på denne fil). Med eksemplet bliver det så Stakit Stativ Kasket.
Start med at implementere Klienten og serveren på samme computer,
dvs. brug Localhost (IP 127.0.0.1).
"""

'''
	Dette er server programmet 
'''

import socket

receive_list = []

host = "" # not binding to any specific address
port = 1337 # port; remember that ports 1024 and below are privileged

connection_sock = socket.socket() # create a TCP socket
connection_sock.bind((host, port)) # bind this socket to, in this case all addresses -> host = ""

connection_sock.listen() # wait for incomming connections

while True:
	data_sock, client_addr = connection_sock.accept() # accept connection and create socket for data com.
	#data_sock.settimeout(1) # consider the transaction terminated, if nothing is received in a second
	print(f"Accepted connection from {client_addr}")

	try:
		while True:
			data = data_sock.recv(64).decode() # receive upto 64 bytes and write this to the buffer list
			if data: # if nothing is recieved, this will come back empty
				receive_list.append(data)
			else:
				break
	except socket.timeout:
		print(f"Connection to {client_addr} closed; Connection timed out.")
	finally:
		with open("received_words.txt", "w") as f: # opens the file "received_words.txt" in write mode
			f.writelines(receive_list) # write received words to the file
