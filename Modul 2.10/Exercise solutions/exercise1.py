"""
1: Med udgangspunkt i Live-codingen og den sidste version af JSON filen, skal du i denne opgave lave et program hvor
brugeren kan indtaste navn, parti og embedsperioden for en president.
Tag højde for ugyldige indtastninger (hvilke kan du komme i tanker om?).
"""

import json

def main():
	valid_parties = ["Republikaner", "Demokrat", "UCN"]

	with open("../JSONeksempler/presidenter.json", "r", encoding="utf-8") as fileObject:
		presidents = json.load(fileObject) # indlæser filen i en dictionary

		name = input("Enter the name of a new president: ")

		while True: # Gentag spørgsmplet indtil brugeren indtaster et gyldig parti
			party = input("What is the party of " + name + "? ")
			if party in valid_parties:
				break
			else:
				print("Following parties are valid: " + str(valid_parties))


		while True: # Gentag spørgsmplet indtil brugeren indtaster et tal
			try:
				start_of_term = int(input("When did " + name + "'s term start? "))
			except ValueError:
				print("Start term must be a number")
			else:
				break

		while True: # Gentag spørgsmplet indtil brugeren indtaster et tal, eller ingen ting
			try:
				end_of_term = input("When did " + name + "'s term end (optional, can be left blank)? ")
				if end_of_term == "":
					end_of_term = None
				else:
					end_of_term = int(end_of_term)
			except ValueError:
				print("End term must be a number")
			else:
				break

	# Tilføjer præsidenten til vores dictionary med presidenter
	presidents[name] = {
				"Parti": party,
				"Valgperiode": {
					"startår": start_of_term,
					"slutår": end_of_term
				}
			}

	# Gemmer præsidenterne til presidenter.json
	with open("../JSONeksempler/presidenter.json", "w", encoding="utf-8") as fileObject:
		json.dump(presidents, fileObject, indent="\t")

if __name__ == "__main__":
	main()