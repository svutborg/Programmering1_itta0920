"""
15: Brug GET til at læse det seneste datapunkt fra hhv. Temperatur og Luftfugtighed i din Publickanal.
Får du det samme som du skrev i opg. 12?
"""
import requests

channel_id = "1235498"
num_results = 1

url=f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?results={num_results}"

response = requests.get(url)

if response.status_code == 200:
	response_dict = response.json()
	entry = response_dict["feeds"][0]
	if (entry["field1"] == '23') and (entry["field2"] == '44'):
		print("All good :D")
	else:
		print("You done goofed!")
