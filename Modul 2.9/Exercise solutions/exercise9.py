"""
9: I denne opgave skal du bruge dictReader fra CSV modulet.
Prøv at indlæse filen du lavede i opgave 8, og gem hvert lands oplysninger i en dictionary.
Hver af disse dictionaries skal gemmes i en liste.
"""
import csv

lande = []

with open("Lande.csv", "r", newline="\n", encoding="utf-8") as fileObject:
	csv_dict_reader = csv.DictReader(fileObject)

	for land in csv_dict_reader:
		lande.append(dict(land))
