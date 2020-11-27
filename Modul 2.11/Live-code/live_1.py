# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 2020

Lav et Python script som læser den nyeste måling fra Channel 9 i Thingspeak, og gemmer denne måling i en JSON fil
Print indholdet af denne JSON fil i konsollen, så det er læsevenligt
Udvid programmet, så at en bruger kan vælge et dato-interval.
Data fra dette dato-interval skal (såfremt intervallet er gyldigt!) gemmes i en JSON fil.
Print derefter ovenstående data.

@author: SVU
"""
import requests
import json

url = "https://api.thingspeak.com/channels/9/feeds.json?results=50"

resp = requests.get(url)

respDict = resp.json()

with open("Channel9_feeds.json","w") as fileObject:
	json.dump(respDict, fileObject, indent=4)

#with open("Channel9_feeds.json","r") as fileObject:
#	print(fileObject.read())

feed_list = respDict["feeds"]
temp = 0
for entry in feed_list:
	temp += float(entry["field2"])
temp = temp/len(feed_list)
print(temp)

"""
for k, v in respDict.items():
	print(k + ": ")
	if type(v) == dict:
		for k2, v2 in v.items():
			print("\t" + k2 + ": " + str(v2))
	else:
		for element in v:
			for k2, v2 in element.items():
				print("\t" + k2 + ": " + str(v2))
"""
