"""
1(a): I denne opgave skal du arbejde med filen population_json.json, som kan hentes i Canvas.
Start med at indlæse denne fil, og gem dens indhold i en liste med dictionaries.

1(b): Print populationen for den Europæiske Union (landekode: EUU) for hvert 5. år mellem 1960 og 2015 (begge år inklusive).

1(c): Prøv at finde ud af hvor mange forskellige grupper af lande (dvs. hvor mange country codes) der er i alt.
(Hint: lav evt. en liste med country codes)

1(d): Lav et program hvor brugeren kan vælge mellem disse grupper, vælge årstal og ud fra disse valg få printet befolkningstallet.
"""
import json


def exercise_a():
	global pop_list
	with open("population_json.json", "r") as fileObject:
		pop_list = json.load(fileObject)

def exercise_b():
	for element in pop_list:
		if element["Country Code"] == "EUU":
			if (element["Year"] % 5 == 0) and (1960 <= element["Year"] <= 2015):
				print(f"Population for the year {element['Year']} is {element['Value']}")

def exercise_c():
	global country_codes
	country_codes = []

	for entry in pop_list:
		if entry["Country Code"] not in country_codes:
			country_codes.append(entry["Country Code"])
	print(len(country_codes))

def exercise_d():
	global country_codes
	while True:
		cc = input("Vælg en country code (tast q for at afslutte): ").upper()
		if (cc.lower() == "q") or (cc in country_codes):
			country_data = []
			for element in pop_list:
				if element["Country Code"] == cc:
					country_data.append(element)

			year = int(input("Vælg et årstal: "))
			for entry in country_data:
				if entry["Year"] == year:
					print(f"Befolkningen i {entry['Country Name']} var {entry['Value']} i år {entry['Year']}")

			break
		else:
			print("following country codes are valid:")
			print(country_codes)


exercise_a()
exercise_b()
exercise_c()
exercise_d()

#print(pop_list)