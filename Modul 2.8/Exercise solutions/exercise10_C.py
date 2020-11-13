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
	Dette er klient programmet 
'''

import socket

host = "127.0.0.1" # not binding to any specific address
port = 1337 # port; remember that ports 1024 and below are privileged

sock = socket.socket() # create a TCP socket
sock.connect((host, port)) # connect to server
print(f"Connection to {host} established")
with open("words.txt") as f:
	send_list = f.readlines()
	print("Sending text")
	for line in send_list:
		sock.send(line.encode())

	print("Done sending, closing connection")
	sock.close()