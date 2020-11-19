# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:35:26 2018

Delete a channel with HTTP DELETE.

Here we use the *USER API KEY*, which can be found in the Account Profile page:
https://thingspeak.com/account/profile

Replace XXXXXXXXXXXXXXXX with the USER API KEY.

@author: HTH
"""

import requests as r

url = 'https://api.thingspeak.com/channels/636066.json'

# Adds a third field to the channel, and names it "Antal requests"
# If the field exists, it will be overwritten
data = {
	"api_key": "XXXXXXXXXXXXXXXX"
}

resp = r.delete(url, json=data)

print("Status: ", resp.status_code)