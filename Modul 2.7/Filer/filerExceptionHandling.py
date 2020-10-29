# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:10:20 2018

Eksempel med åbning og lukning af filer samt exception handling

@author: HTH
"""

# Læsning fra fil
try:
    with open("words.txt","r") as filObjekt:
        listeAfOrd = filObjekt.readlines()
except FileNotFoundError:
    print("Fejl: Filen blev ikke fundet.")

# Læsning fra fil som ikke findes
try:
    with open("words2.txt","r") as filObjekt:
        listeAfOrd = filObjekt.readlines()
except FileNotFoundError:
    print("Fejl: Filen blev ikke fundet.")

# Skrivning til fil
try:
    with open("test.txt", "a") as filObjekt:
        filObjekt.writelines("Dette bliver tilføjet til filen\n")
except FileNotFoundError:
    print("Fejl: Filen blev ikke fundet.")
    
# Læsning fra til, alterantiv metode    
try:
	filObjekt = open("words.txt", 'r')
	listeAfOrd2 = filObjekt.readlines()
except FileNotFoundError:
	print("Fejl: Filen blev ikke fundet.")
finally:
	filObjekt.close()