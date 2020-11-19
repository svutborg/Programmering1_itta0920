# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:04:33 2018

Update channel field with HTTP PUT command

Here we use the *USER API KEY*, which can be found in the Account Profile page:
https://thingspeak.com/account/profile

Replace XXXXXXXXXXXXXXXX with the USER API KEY.

@author: HTH
"""

import requests as r

url = 'https://api.thingspeak.com/channels/635978.json'

# Adds a third field to the channel, and names it "Antal requests"
# If the field exists, it will be overwritten
data = {
	"api_key": "XXXXXXXXXXXXXXXX",
	"field3": "Antal requests"
}

resp = r.put(url, json=data)

print("Status: ", resp.status_code)