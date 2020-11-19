"""
13: Brug GET til at skrive dette tal i din Privatkanal: Vandstand: 34.
"""
import requests

api_key = "P5JLLSPPOY5JHZ9O"
fields = {"field1": 34}

url = f"https://api.thingspeak.com/update?api_key={api_key}"

for field, value in fields.items():
	url += f"&{field}={value}"
response = requests.get(url)

print(response.reason)