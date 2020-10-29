# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:16:47 2019

Eksempel med læsning og skrivning af 
binære filer.

@author: HTH
"""

filnavnLæs = "image.png"
filnavnSkriv = "newimage.png"
filnavn2Skriv = "newimage2.png"

# Læser en byte fra filen
try:
    filObjekt = open(filnavnLæs, 'rb')
    enByteFraFilen = filObjekt.read(1) # Læser 1 byte fra filen
    print(enByteFraFilen) # Printer denne byte
except FileNotFoundError:
    print("Fejl: Filen blev ikke fundet.")
finally:
    filObjekt.close()
    
# Læser hele filen
try:
    filObjekt = open(filnavnLæs, 'rb')
    heleFilen = filObjekt.read() # Læser hele filen
    print("Filen er: " + str(len(heleFilen)) + " bytes.")
except FileNotFoundError:
    print("Fejl: Filen blev ikke fundet.")
finally:
    filObjekt.close()

# Skriver til en anden fil
try:
    filObjekt = open(filnavnSkriv, "wb")
    filObjekt.write(heleFilen)
finally:
    filObjekt.close()
    
# Skriver til en anden fil, én byte ad gangen
try:
    filObjekt = open(filnavn2Skriv, "wb")
    for data in heleFilen:
        filObjekt.write(data.to_bytes(1,'little'))
finally:
    filObjekt.close()