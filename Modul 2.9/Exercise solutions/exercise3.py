"""
3: Loop over denne dictionary, og print hver ingrediens samt dens mængde på hver sin linje.
"""

from exercise2 import Chokolade_cheesecake_med_marengslaeg as kage

# Denne er mere kompleks, end hvad der behøves
def print_dict(d, level=0):
	for key in d.keys():
		if type(d[key]) == dict:
			print(f"{key}:")
			print_dict(d[key], level+1)
		else:
			indent = '\t'*level
			print(f"{indent}{key}: {d[key]}")

# Mere simple print funktion der ikke passer helt så godt på min datastruktur
def print_dict_simple(d):
	for key in d.keys():
		print(f"{key}: {d[key]}")


print_dict(kage)
#print_dict_simple(kage)