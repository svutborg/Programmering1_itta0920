# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 2020

Vi skal lave et program som gør følgende:
Brug JSON pakken til at åbne presidenter.json filen.
Tilføj presidenten George W. Bush samt parti og embedsperiode til JSON filen.
Konverter JSON filen presidenter.json, så at embedsperioden i stedet for en tekststreng er to heltal (integers)
for henholdsvis start og slutår for embedsperioden.
Hvis der ikke er noget slutår, skal denne variabel have værdien 0 (nul). Denne konvertering skal ske i Python.

@author: SVU
"""

import json

with open("../JSONeksempler/presidenter.json", "r", encoding="utf-8") as fileObject:
	presidents = json.load(fileObject) # indlæser filen i en dictionary
	print(presidents)
	presidents["George W. Bush"] = {'Parti': 'Republikaner', 'Valgperiode': {'startår': 2000, 'slutår': 2008}} # tilføjer en president
	print(presidents)

	# Kode der omdanner valgperioden til start og slut år, hvis det står som en streng
	for name, info in presidents.items():
		print(name, "-", info['Valgperiode'])
		if type(info['Valgperiode']) == str:
			years = info['Valgperiode'].split('-') # inddeler strengen i en liste eks. "1234-5678" --> ["1234","5678"]
			try:
				info['Valgperiode'] = {'startår': int(years[0]), 'slutår': int(years[1])}
			except ValueError: # Fanger, hvis der ikke er noget slutår
				info['Valgperiode'] = {'startår': int(years[0]), 'slutår': None}

# Gemmer filen
with open("../JSONeksempler/presidenter.json", "w", encoding='utf-8') as fileObject:
	json.dump(presidents, fileObject, indent="\t")