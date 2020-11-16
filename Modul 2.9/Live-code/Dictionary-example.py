# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 2020

Vi skal lave et program som gør følgende:
	Lav en dictionary med fornavn, efternavn, alder og by for en person (vælg selv hvilken).
	Print derefter de enkelte elementer i denne dictionary.
	Tilføj et key-value par til denne dictionary, f.eks. uddannelsessted
	Slet et key-value par efter eget valg

@author: SVU
"""

def print_dict(d):
	for element in d:
		print(f"{element.title():15}: {d[element]}")
		#print(element.title() + ": " + str(d[element]))

def fill_dict(d):
	for k in d.keys():
		d[k] = input(f"Indtast {k}: ")


person = {"fornavn": "", "efternavn": "", "alder": None}
fill_dict(person)
print_dict(person)
print("")

person["Arbejde"] = "UCN"
print_dict(person)
print()

#del person["alder"]
alder = person.pop("alder")
print_dict(person)

print(alder)
