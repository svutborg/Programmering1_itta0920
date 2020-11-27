# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:02:06 2019

@author: HTH
"""

import requests
import json

url = 'https://api.thingspeak.com/channels/9/feeds.json'
r = requests.get(url)
print("Status: ", r.status_code)
rDict = r.json()

with open('channel9.json', 'w') as filObjekt:
    json.dump(rDict, filObjekt, indent=4)






