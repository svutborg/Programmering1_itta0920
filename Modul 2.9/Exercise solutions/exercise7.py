"""
7: I denne opgave skal du tage udgangspunkt i filen studerende.csv, samt i Python koden fra Live-coding’en.
Programmet skal tage et input fra brugeren i form af et navn på en studerene (f.eks. Jens Hansen),
og printe personens alder samt uddannelse. Hvis den studerende ikke findes i CSV filen,
skal programmet give en besked om dette.
"""

import csv

with open("../CSV/studerende.csv", "r", newline="\n") as fileObject:
	cr = csv.DictReader(fileObject, delimiter=",")

	print("Tast q for at afslutte")
	search_name = input("Indtast navn: ")
	while search_name not in ('q', 'Q'):
		found = False
		for entry in cr:
			if entry["navn"].__contains__(search_name):
				print(', '.join(list(entry.values())))
				found = True
		if not found:
			print(search_name + " blev ikke fundet")
		search_name = input("Indtast navn: ")