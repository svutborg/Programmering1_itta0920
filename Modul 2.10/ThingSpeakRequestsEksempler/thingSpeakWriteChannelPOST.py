# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:45:44 2018

Write data in bulk to channel using HTTP POST command

@author: HTH
"""

import requests as r

###############################################################################
# Writes data in bulk using absolute timestamps
url = 'https://api.thingspeak.com/channels/635978/bulk_update.json'

data = {
	"write_api_key": "ROH8OOORHB7A9UXP",
	"updates": [{
            "created_at": "2018-11-25 10:26:00 +0100",
			"field1": "6.0",
			"field2": "5.0"
		},
        {
            "created_at": "2018-11-25 10:27:00 +0100",
			"field1": "8.0",
			"field2": "3.0"
		}
	]
}

resp = r.post(url, json=data)

print("Status: ", resp.status_code)

###############################################################################
# Writes data in bulk using relative timestamps
url = 'https://api.thingspeak.com/channels/635978/bulk_update.json'

data = {
	"write_api_key": "ROH8OOORHB7A9UXP",
	"updates": [{
            "delta_t": 4,
			"field1": "10.0",
			"field2": "20.0"
		},
        {
            "delta_t": 2,
			"field1": "15.0",
			"field2": "25.0"
		}
	]
}

resp = r.post(url, json=data)

print("Status: ", resp.status_code)

###############################################################################
# Writes data in bulk using relative timestamps
url = 'https://api.thingspeak.com/channels/635978/bulk_update.json'

data = {
	"write_api_key": "ROH8OOORHB7A9UXP",
	"updates": [{
            "delta_t": 5,
			"field1": "10.0",
			"field2": "20.0"
		},
        {
            "delta_t": 5,
			"field1": "15.0",
			"field2": "25.0"
		},
        {
            "delta_t": 5,
			"field1": "11.0",
			"field2": "22.0"
		},
        {
            "delta_t": 5,
			"field1": "21.0",
			"field2": "18.0"
		}
	]
}

resp = r.post(url, json=data)

print("Status: ", resp.status_code)

###############################################################################
# Writes data in bulk using relative timestamps to non-existent field
url = 'https://api.thingspeak.com/channels/635978/bulk_update.json'

data = {
	"write_api_key": "ROH8OOORHB7A9UXP",
	"updates": [{
            "delta_t": 4,
			"field1": "10.0",
			"field2": "20.0",
            "field3": "14.0"
		},
        {
            "delta_t": 2,
			"field1": "15.0",
			"field2": "25.0",
            "field3": "17.0"
		}
	]
}

resp = r.post(url, json=data)

print("Status: ", resp.status_code)