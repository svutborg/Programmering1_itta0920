# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:22:58 2018

Read data from channel with requests using HTTP GET command

@author: HTH
"""

import requests as r

# Reads the 3 most recent results from channel 9 in JSON format
urlJSON = 'https://api.thingspeak.com/channels/9/feeds.json?results=3'

response = r.get(urlJSON)

print("Status: ", response.status_code)

# Saves results in dictionary
rDict = response.json()

# Reads the 3 most recent results from channel 9 in CSV format
urlCSV = 'https://api.thingspeak.com/channels/9/feeds.csv?results=3'

response = r.get(urlCSV)

rCSV = response.content.decode('UTF-8') # Decodes it to a string

print("Status: ", response.status_code)

# Reads from incorrect URL:
urlNOT = 'https://api.thingspeak.com/channels/0/feeds.csv?results=3'

response = r.get(urlNOT)

print("Status: ", response.status_code)