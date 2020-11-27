# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:31:27 2018

Create a new channel with HTTP POST.

Here we use the *USER API KEY*, which can be found in the Account Profile page:
https://thingspeak.com/account/profile

Replace XXXXXXXXXXXXXXXX with the USER API KEY.

@author: HTH
"""

import requests as r

url = 'https://api.thingspeak.com/channels.json'

# Adds a third field to the channel, and names it "Antal requests"
# If the field exists, it will be overwritten
data = {
	"api_key": "XXXXXXXXXXXXXXXX",
	"name": "My new channel"
}

resp = r.post(url, json=data)

print("Status: ", resp.status_code)