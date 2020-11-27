# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 2020

Start med at oprette en bruger på ThingSpeak. Lav derefter en privat kanal.
Nedenstående skal laves med Requests modulet:
Skriv ét datapunkt (dvs. ét tal) til denne kanal med GET. Vælg selv tallet.
Læs fra den private kanal som du har oprettet. Virker det hvis du ikke bruger API-nøglen?
Hvilken status kode (dvs. requests.status_code) får du?
Hvad hvis du bruger en forkert API-nøgle i ovenstående? Hvilken status kode får du? Hvad betyder denne status kode?

@author: SVU
"""

import requests
measurement = int(input("Indtast måling"))
url = f"https://api.thingspeak.com/update?api_key=JTFWDGC8JOGPY70P&field1={measurement}"

resp = requests.get(url)

print(str(resp.status_code) + ": " + resp.reason)