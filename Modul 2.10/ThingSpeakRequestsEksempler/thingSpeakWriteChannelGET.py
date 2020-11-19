# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:30:38 2018

Write data to channel with requests using HTTP GET command

We need to use the correct API key.

@author: HTH
"""

import requests as r

# Writes 23 in field 1 in the channel
url = 'https://api.thingspeak.com/update?api_key=ROH8OOORHB7A9UXP&field1=23'

resp = r.get(url)

print("Status: ", resp.status_code)

# Writes 33 in field 1 and 44 in field 2 in the channel
url = 'https://api.thingspeak.com/update?api_key=ROH8OOORHB7A9UXP&field1=33&field2=44'

resp = r.get(url)

print("Status: ", resp.status_code)

# Writes data in non-existent field in the channel
url = 'https://api.thingspeak.com/update?api_key=ROH8OOORHB7A9UXP&field3=14'

resp = r.get(url)

print("Status: ", resp.status_code)