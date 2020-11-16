# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:30:30 2018

Læsning og skrivning af CSV filer på den almindelige måde

@author: HTH
"""

csvFilnavn = "studerende.csv"

# Læsning af CSV fil
with open(csvFilnavn) as filObjekt:
    linjeCounter = 0
    dataListe = []
    for linje in filObjekt:
        print(linje)
        if linjeCounter == 0:
            header = linje
            linjeCounter += 1
        else:
            dataListe.append(linje)

# Skrivning af CSV fil
        
csvFilnavnSkriv = "studerende2.csv"

with open(csvFilnavnSkriv, 'w') as filObjekt:
    filObjekt.write("Hans Schmidt, Arkitekt, 21, godmorgen")