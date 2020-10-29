# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:47:12 2018

Eksempel med indlæsning af fil.

@author: HTH
"""

filnavn1 = "words.txt"

# Åbner filer og printer dens indhold
with open(filnavn1) as filObjekt:
    indhold = filObjekt.read()
    print(indhold)

# Obs.: filObjekt er lukket, så næste linje kan ikke køres    
#filObjekt.read()

# Nedenstående gemmer indholdet af filen i en liste, separeret af linjeskift
with open(filnavn1, 'r') as filObjekt:
    linjer = filObjekt.readlines()
    
# Laver en ny fil og skriver noget i den
filnavn2 = "nyfil.txt"
with open(filnavn2, "w") as filObjekt:
    filObjekt.write("Hej")
    
# Dette vil overskrive filen nyfil.txt
with open(filnavn2, "w") as filObjekt:
    filObjekt.write("Hallo")
    
# Tilføjer til en fil
with open(filnavn2, "a") as filObjekt:
    filObjekt.write("Hej")
    
filnavn3 = "appendfil.txt"
with open(filnavn3, "a") as filObjekt:
    filObjekt.write("Hejsa")
    
# Argumentet med x virker kun hvis filen ikke findes i forvejen
filnavn4 = "lavNyFil.txt"
with open(filnavn4, "x") as filObjekt:
    filObjekt.write("Aha")