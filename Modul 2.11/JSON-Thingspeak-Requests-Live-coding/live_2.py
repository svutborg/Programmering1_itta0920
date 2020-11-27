# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:17:45 2019

Lav et Python script som læser den nyeste måling fra Channel 9 i Thingspeak, og gemmer denne måling i en JSON fil

Print indholdet af denne JSON fil i konsollen, så det er læsevenligt

Udvid programmet, så at en bruger kan vælge et dato-interval. Data fra dette dato-interval skal (såfremt intervallet er gyldigt!) gemmes i en JSON fil.

Print derefter ovenstående data.

@author: HTH
"""
# Laver et Python script som læser den nyeste måling fra Channel 9 i Thingspeak, og gemmer denne måling i en JSON fil

import requests
import json

url = "https://api.thingspeak.com/channels/9/feeds.json?results=1"

# Hvis der kræves en API key:
urlMedAPI = "https://api.thingspeak.com/channels/9/feeds.json?api_key=XXXXXXXXXXXX&results=1"

# Sender forespørgsel til Thingspeak
response = requests.get(url)

# Printer statuskoden
print("Status: ", response.status_code)

# Konverterer serverens svar til en dictionary
channel9Dict = response.json()

# Trækker feeds ud af ovenstående dictionary, 
# og bagefter det første element
målingChannel9Dict = channel9Dict["feeds"][0]

with open("minFil.json", "w") as filObjekt:
    json.dump(målingChannel9Dict, filObjekt, indent=4)

# Print indholdet af denne JSON fil i konsollen, så det er læsevenligt
for key, value in målingChannel9Dict.items():
    print(key, ": ", value)





