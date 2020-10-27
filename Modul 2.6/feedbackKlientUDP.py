# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:15:36 2018

Eksempel med klient. Dette kører en klient proces, etablerer 
forbindelser til en server proces og sender noget data.
Klienten får feedback fra serveren.
Derefter lukkes forbindelsen.

@author: HTH
"""

import socket, time

print("Kører klienten\n")

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Laver en socket

host = "10.31.128.105" # Dette er IP-adressen for Raspberry Pi
port = 3000

# Definerer data:
dataListe = ["Mars", "Jupiter", "Italien", "TCP", "Stol"]

# Sender data
for data in dataListe:
    print("Sender data:", str(data))
    
    # Indkoder data til UTF-8
    indkodet_data = data.encode("UTF-8")
    skt.sendto(indkodet_data, (host, port))

    # Modtager feedback
    mdata, server = skt.recvfrom(64)
    dekodet_data = mdata.decode("UTF-8")
    if mdata:
        print("Server feedback: ", str(dekodet_data))
    else:
        print("Slut på feedback")
   
    time.sleep(1)

skt.close() # Lukker forbindelsen

print("Socketen blev lukket")