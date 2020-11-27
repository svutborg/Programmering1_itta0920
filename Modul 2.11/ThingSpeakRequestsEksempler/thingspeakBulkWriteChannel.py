# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:34:45 2018

Write data in bulk to ThingSpeak channel with POST

@author: HTH
"""

import requests as r
import datetime
import pytz

url = 'https://api.thingspeak.com/channels/635978/bulk_update.json'

currentTimeDate = datetime.datetime.now(tz = pytz.timezone('CET')).isoformat()

data = {
	"write_api_key": "ROH8OOORHB7A9UXP",
	"updates": [{
			"created_at": currentTimeDate,
			"field1": "6.0",
			"field2": "5.0"
		}
	]
}

resp = r.post(url, json=data)