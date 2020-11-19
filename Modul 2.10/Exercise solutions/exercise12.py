"""
12: Brug GET til at skrive disse to tal i din Publickanal: Temperatur: 23, Luftfugtighed: 44.
"""
import requests

api_key = "JTFWDGC8JOGPY70P"
fields = {"field1": 23, "field2": 44}

url = f"https://api.thingspeak.com/update?api_key={api_key}"

for field, value in fields.items():
	url += f"&{field}={value}"
response = requests.get(url)

print(response.reason)