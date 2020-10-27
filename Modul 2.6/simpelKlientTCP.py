# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:15:36 2018

Eksempel med echo klient. Dette kører en klient proces, etablerer 
forbindelser til en server proces og sender noget data.
Derefter lukkes forbindelsen.
Der er ingen feedback fra server til klient i denne version.

@author: HTH
"""

import socket, time

print("Kører klienten\n")

skt = socket.socket() # Laver en socket

host = "192.168.68.132" # Dette er IP-adressen for Raspberry Pi
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
   
    time.sleep(1)

skt.close() # Lukker forbindelsen

print("Socketen blev lukket")