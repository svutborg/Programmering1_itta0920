# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 20:26:29 2018

@author: HTH
"""

import csv

# Skriver noget data til CSV fil med DictWriter
with open('studerende.csv', mode='w') as filObjekt:
    feltNavne = ['navn', 'studieretning', 'alder']
    csvObjekt = csv.DictWriter(filObjekt, fieldnames=feltNavne, lineterminator="\n")

    csvObjekt.writeheader()
    csvObjekt.writerow({'navn': 'Jens Hansen', 'studieretning': 'Design', 'alder': '22'})
    csvObjekt.writerow({'navn': 'Peter Madsen', 'studieretning': 'IT', 'alder': '24'})
    
# Læser noget data fra CSV fil med DictReader
with open("studerende.csv", 'r') as filObjekt:
    
    csvObjekt = csv.DictReader(filObjekt)
    
    studerendeListe = []
    
    for row in csvObjekt:
        studerendeListe.append(row)
    feltNavne = csvObjekt.fieldnames