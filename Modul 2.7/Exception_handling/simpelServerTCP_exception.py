# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:10:37 2018

En server som accepterer indkomne forbindelser og viser hvilke data 
klienten sender.
Når klienten ikke sender mere data, lukkes forbindelsen.
Der er ingen feedback fra server til klient i denne version.

@author: HTH
"""

import socket

print("Kører serveren\n")

host = "127.0.0.1" # Dette er IP-adressen for Raspberry Pi
port = 3000 # Husk at portnumre på 1024 og lavere er priviligerede

skt = socket.socket() # Man kan give argumenter til denne (f.eks. om det skal være TCP eller UDP)

try:
    skt.bind((host, port)) # Tilskriver IP-adressen og porten til vores socket
    print("Socket lavet.")
except OSError:
    print("Kunne ikke lave socket med IP " + str(host) + " og port " + str(port) + ".")

antalForbindelser = int(input("Vælg antal forbindelser:"))

try:
    skt.listen() # Lytter efter forbindelser
except OSError:
    print("Socketen kunne ikke lytte efter indkomne forbindelser.")
    
while antalForbindelser > 0:
    forbindelse, addresse = skt.accept()
    print("Værten med " + str(addresse[0]) + " har etableret forbindelse.")
    
    # Moodtager data
    while True:
        data = forbindelse.recv(64)
        
        dekodet_data = data.decode("UTF-8")
        
        if data:
            print("Data modtaget: ", str(dekodet_data))
        else:
            print("Ikke mere data.")
            break
    
    forbindelse.close()
    
    antalForbindelser = antalForbindelser - 1
    
skt.close()