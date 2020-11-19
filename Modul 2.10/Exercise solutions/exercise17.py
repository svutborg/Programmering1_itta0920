"""
17: Prøv at bruge GET for at læse de seneste 3 datapunkter fra kanal 9 med linket:
https://api.thingspeak.com/channels/9/feeds.json?results=3
Hvilken statuskode får du? Hvad betyder denne statuskode?
"""
import requests

resp = requests.get("https://api.thingspeak.com/channels/9/feeds.json?results=3")
print("Hvilken statuskode får du?", end = ": ")
print(resp.status_code)
print("Hvad betyder denne statuskode?", end = ": ")
print(resp.reason)