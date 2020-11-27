# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:08:52 2019

Brug JSON pakken til at åbne presidenter.json filen. Tilføj presidenten George W. Bush samt parti og embedsperiode til JSON filen.

Konverter JSON filen presidenter.json, så at embedsperioden i stedet for en tekststreng er to heltal (integers) for henholdsvis start og slutår for embedsperioden. 

Hvis der ikke er noget slutår, skal denne variabel have værdien 0 (nul). Denne konvertering skal ske i Python.

@author: HTH
"""

import json

filNavn = "presidenter.json"

# Data som skal tilføjes
presidentNavn = "George W. Bush"
parti = "Republikaner"
valgperiode = "2000-2008"

# Åbner JSON filen presidenter.json 
# og gemmer indholdet
with open(filNavn, "r") as filObjekt:
    jsonObjekt = json.load(filObjekt)
    
# Tilføjer George W. Bush til dictionary'en
jsonObjekt["George W. Bush"] = {"Valgperiode": valgperiode, "Parti": parti}

# Åbner JSON filen til skrivning
with open(filNavn, "w") as filObjekt:
    json.dump(jsonObjekt, filObjekt)








