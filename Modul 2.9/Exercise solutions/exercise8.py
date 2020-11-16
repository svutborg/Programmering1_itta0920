"""
8: I denne opgave skal du bruge dictWriter fra CSV modulet.
Du skal i denne opgave gemme information om nogle lande i en CSV fil. Vælg selv nogle lande,
f.eks.: {’land’: ’Danmark’, ’Hovedstad’: ’København’, ’Indbyggere’: ’5500000’, ’Verdensdel’: ’Europa’}.
I CSV filen skal der være et land på hver linje. Den første linje skal være med emnefelterne
"""
import csv

lande = [   {"Land": "Danmark", "Hovedstad": "København", "Indbyggere": 5500000, "Verdensdel": "Europa"},
			{"Land": "Kina", "Hovedstad": "Beijing", "Indbyggere": 1376000000, "Verdensdel": "Asien"}
]

with open("Lande.csv", "w", newline="\n", encoding="utf-8") as fileObject:
	csv_dict_writer = csv.DictWriter(fileObject, fieldnames=lande[0].keys())

	csv_dict_writer.writeheader()

	for land in lande:
		csv_dict_writer.writerow(land)