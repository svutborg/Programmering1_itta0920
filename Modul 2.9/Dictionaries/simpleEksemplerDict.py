# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 14:17:51 2018

Eksempler med Dictionaries

@author: HTH
"""

# Definerer en tom dictonary
# syntaks 1
slikTypeDict1 = {}
# syntaks 2
slikTypeDict2 = dict()

# Definer med to key-value par:
slikTypeDict = {"Type": "Bounty", "Pris": 10}


# Indeksering af dict
slikType = slikTypeDict["Type"]
slikPris = slikTypeDict["Pris"]

# Printer resultatet:
print("En " + slikType + " koster " + str(slikPris) + " kr.")

# Tilføjer nyt key-value par:
slikTypeDict["AntalSolgt"] = 100

# Ændring af prisen på en Bounty:
slikTypeDict["Pris"] = 12

# Ændring af to key-value par samtidigt:
slikTypeDict.update({"AntalSolgt": 11, "Pris": 15})

# Returnerer alle keys:
keys = slikTypeDict.keys()

# Returnerer alle values:
values = slikTypeDict.values()

# Returnerer alle key-value par:
keyValuePar = slikTypeDict.items()