"""
16: Brug GET til at læse det seneste datapunkt fra Vandstand i din Privatkanal.
Får du det samme som du skrev i opg. 13?
"""
import requests

channel_id = "1235497"
api_key = "HNPPLC0EQ5MEGPSF"
num_results = 1

url=f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&results={num_results}"

response = requests.get(url)

if response.status_code == 200:
	response_dict = response.json()
	entry = response_dict["feeds"][0]
	if entry["field1"] == '34':
		print("All good :D")
	else:
		print("You done goofed!")
