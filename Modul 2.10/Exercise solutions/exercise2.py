"""
2: Udvid programmet fra forrige opgave, så man kan søge i JSON filen efter en president baseret på dennes fulde navn.
Programmet skal (såfremt det man søger efter bliver fundet) printe presidentens navn, embedsperiode og parti.
"""

import json
from exercise1 import main as ex1 # importerer main funktionen fra exercise 1; Genbrug er god brug ;)

valid_parties = ["Republikaner", "Demokrat", "UCN"]
menu_options ={"1": "Add president", "2": "Search for president"}

def print_menu():
	print("Welcome to the presidential archive!")
	print("Your options are as follows")
	for number, option in menu_options.items():
		print(number, ": ", option)

	def get_selection():
		selection = input(">")
		if selection in menu_options.keys():
			return selection
		else:
			print("You must select one of the following: ", str(list(menu_options.keys())))
			return get_selection() # kald sig selv rekursivt, hvis man ikke valgte noget gyldigt

	return get_selection()

def add_president():
	ex1() # referere tilbage til opgave 1

def print_dict(p, indent=0):
	for k, v in p.items():
		padding = '\t'*indent
		print(f"{padding}{k}:", end="")
		if type(v) == dict:
			print("")
			print_dict(v, indent = indent+1)
		else:
			print(f" {v}")



def get_president():
	with open("../JSONeksempler/presidenter.json", "r") as fileObject:
		presidents = json.load(fileObject)
		president = input("Enter the full name of a presedent:")
		if president in presidents.keys():
			presidential_information = presidents[president]
			print_dict({president: presidential_information})
		else:
			print("505: President not found")

selection = print_menu()
if selection == "1":
	add_president()
elif selection == "2":
	get_president()