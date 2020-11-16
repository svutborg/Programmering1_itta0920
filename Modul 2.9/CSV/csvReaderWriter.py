# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:42:11 2018

Læsning og skrivning af CSV filer med reader og writer

@author: HTH
"""

import csv

csvFilnavn = "studerende.csv"

dataListe = []

# Læsning af CSV fil
with open(csvFilnavn, 'r') as filObjekt:
    csvObjekt = csv.reader(filObjekt, delimiter=',')
    linjeCounter = 0
    for linje in csvObjekt:
        if linjeCounter == 0:
            emnerCSV = linje
            linjeCounter += 1
        else:
            dataListe.append(linje)
            linjeCounter += 1
                        
# Skrivning af CSV fil            
csvSkrivFilnavn = "studerendeSkriv.csv"
            
with open(csvSkrivFilnavn, 'w', newline='\n') as filObjekt:
    csvObjekt = csv.writer(filObjekt, delimiter=',')
    # Skriver emnefeltet (dvs. headeren)
    csvObjekt.writerow(['navn' ,'studieretning', 'alder'])
    csvObjekt.writerow(['Yvonne Dahl' ,'Historie', '23'])