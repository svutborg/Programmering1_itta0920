# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 2020

Vi skal lave et program som gør følgende:
Lav et Python script som læser den nyeste måling fra Channel 9 i Thingspeak, og gemmer denne måling i en JSON fil
Print indholdet af denne JSON fil i konsollen, så det er læsevenligt
Udvid programmet, så at en bruger kan vælge et dato-interval.
Data fra dette dato-interval skal (såfremt intervallet er gyldigt!) gemmes i en JSON fil.

Print derefter ovenstående data.

@author: SVU
"""
import requests
import json

#feeds.json?start=2018-11-11%2010:10:00&end=2018-11-12%2011:11:00

url = "https://api.thingspeak.com/channels/556273/feeds.json?api_key=NU852861M481OKS1&"

start = "2020-01-01"# input("Enter start date: ")
end = "2020-11-20"#input("Enter end date: ")

resp = requests.get(f"{url}start={start}&end={end}")
#print(resp.status_code)
respDict = resp.json()
with open("MyPi.json", "w") as fileObject:
	json.dump(respDict, fileObject, indent="\t")
feeds = respDict["feeds"]
for entry in feeds:
	for k, v in entry.items():
		if k == "field2":
			print(f"{k.title().replace('_', ' '):15}: {v}")
		#print(k.title().replace('_', ' '), ": " , v)

