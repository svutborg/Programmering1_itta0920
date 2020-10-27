# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:15:36 2018

Eksempel med echo klient. Dette kører en klient proces, etablerer 
forbindelser til en echo server proces og sender noget data.
Derefter lukkes forbindelsen.

@author: HTH
"""

import socket, time

print("Kører klienten\n")

skt = socket.socket() # Laver en socket

host = "127.0.0.1"
port = 3000

skt.connect((host, port))

# Definerer data:
dataListe = ["Mars", "Jupiter", "Italien", "TCP", "Stol"]

# Sender data
for data in dataListe:
    print("Sender data:", str(data))
    
    # Indkoder data til UTF-8
    indkodet_data = data.encode("UTF-8")
    skt.sendall(indkodet_data)

    # Modtager feedback
    mdata = skt.recv(64)
    dekodet_data = mdata.decode("UTF-8")
    if data:
        print("Server feedback: ", str(dekodet_data))
    else:
        print("Slut på feedback")
   
    time.sleep(1)

skt.close() # Lukker forbindelsen

print("Socketen blev lukket")