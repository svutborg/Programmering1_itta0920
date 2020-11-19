# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 2020

Start med at oprette en bruger på ThingSpeak. Lav derefter en privat kanal.

Nedenstående skal laves med Requests modulet:
Skriv ét datapunkt (dvs. ét tal) til denne kanal med GET. Vælg selv tallet.
Læs fra den private kanal som du har oprettet. Virker det hvis du ikke bruger API-nøglen?
Hvilken status kode (dvs. requests.status_code) får du?
Hvad hvis du bruger en forkert API-nøgle i ovenstående? Hvilken status kode får du?
Hvad betyder denne status kode?


Print derefter ovenstående data.

@author: SVU
"""

import requests
import json

write_url = "https://api.thingspeak.com/update?api_key=3JN1E3TZKBT0EAF0&"
value =  input("Indtast værdi: ")
resp = requests.get(write_url + "field1=" + value)
if resp.reason == "OK":
	print("Værdi tilføjet!")

read_url = "https://api.thingspeak.com/channels/1235377/feeds.json?api_key=LRX4G885KQAMJA7C&results=1"
resp = requests.get(read_url)
if resp.reason == "OK":
	respDict = resp.json()
	with open("resp.json", "w") as fileObject:
		json.dump(respDict, fileObject, indent=2)
	print(respDict)
else:
	print("Status code: " + str(resp.status_code) + " - Failed to read!")


