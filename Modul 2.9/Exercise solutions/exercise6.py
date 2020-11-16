"""
6: Udvid programmet fra opgave 5, så det kan gemme dictionary’en i en tekstfil.
Den skal gemme hvert key, value på sin egen linje. Vælg selv navnet på denne tekstfil.
"""

from exercise2 import Chokolade_cheesecake_med_marengslaeg as kage

# Denne er mere kompleks, end hvad der behøves
def print_dict(d, level=0, fileObject=None):
	for key in sorted(d):
		if type(d[key]) == dict:
			print(f"{key}:")
			if fileObject != None:
				fileObject.write(f"{key}:\n")
			print_dict(d[key], level=level+1, fileObject=fileObject)
		else:
			indent = '\t'*level
			print(f"{indent}{key}: {d[key]}")
			if fileObject != None:
				fileObject.write(f"{indent}{key}: {d[key]}\n")

# Mere simple print funktion der ikke passer helt så godt på min datastruktur
def print_dict_simple(d, fileObject=None):
	for key in sorted(d):
		print(f"{key}: {d[key]}")
		if fileObject != None:
			fileObject.write(f"{key}: {d[key]}\n")

with open("kage.txt", "w", encoding="utf-8") as fileObject:
	print_dict(kage, fileObject=fileObject)
	#print_dict_simple(kage, fileObject=fileObject)