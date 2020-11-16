"""
4: Ændr loopet som du lavede i opgave 3, så du looper over keys, values.
"""

from exercise2 import Chokolade_cheesecake_med_marengslaeg as kage

# Denne er mere kompleks, end hvad der behøves
def print_dict(d, level=0):
	for key, value in d.items():
		if type(value) == dict:
			print(f"{key}:")
			print_dict(value, level+1)
		else:
			indent = '\t'*level
			print(f"{indent}{key}: {value}")

# Mere simple print funktion der ikke passer helt så godt på min datastruktur
def print_dict_simple(d):
	for key, value in d.items():
		print(f"{key}: {value}")


print_dict(kage)
#print_dict_simple(kage)