
import csv

persons = [{"Navn": "Peter", "Alder": 20},
           {"Navn": "Torben", "Alder": 21},
           {"Navn": "Andersine", "Alder": 32}]

with open("dict_file.csv", "w", newline="\n") as fileObject:
	cw = csv.DictWriter(fileObject, list(persons[0].keys()))
	cw.writeheader()
	for person in persons:
		cw.writerow(person)

with open("dict_file.csv", "r", newline="\n") as fileObject:
	cr = csv.DictReader(fileObject)
	for row in cr:
		print(row)