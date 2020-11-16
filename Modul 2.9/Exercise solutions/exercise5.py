"""
5: Ændr loopet som du lavede i opgave 4, så ingredienserne bliver printet i alfabetisk rækkefølge.
"""

from exercise2 import Chokolade_cheesecake_med_marengslaeg as kage

# Denne er mere kompleks, end hvad der behøves
def print_dict(d, level=0):
	for key in sorted(d):
		if type(d[key]) == dict:
			print(f"{key}:")
			print_dict(d[key], level+1)
		else:
			indent = '\t'*level
			print(f"{indent}{key}: {d[key]}")

# Mere simple print funktion der ikke passer helt så godt på min datastruktur
def print_dict_simple(d):
	for key in sorted(d):
		print(f"{key}: {d[key]}")


print_dict(kage)
#print_dict_simple(kage)