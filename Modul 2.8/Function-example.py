# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 2020

Vi skal lave et program som gør følgende:
	Når programmet startes, skal brugeren vælge hvor mange programmeringssprog skal tilføjes til en liste
	Når programmet kører, skal brugeren vælge om han vil indtaste et programmeringssprog, eller om han vi se de programmeringssprog som er indtastet
	Hvis han vælger at indtaste et programmeringssprog, skal vores program kalde en funktion, som gør dette
	Hvis han vælger at se hvilke programmeringssprog der er i listen, skal vores program kalde en funktion som printer listens indhold

@author: SVU
"""
languages_list = []
num_languages = 0

def print_menu():
	print("L: print listen med indtastede programmeringssprog")
	print("T: tilføj programmeringssprog til listen")
	choise = input("Tast L eller T: ")
	if choise.upper() == "L":
		print_list(languages_list)
	elif choise.upper() == "T":
		add_to_list(languages_list)
		pass
	else:
		print_menu()

def print_list(L):
	if len(L) > 0:
		print("Du indtastede følgende sprog:")
		for index in range(len(L)-1):
			print(L[index], end=", ")
		print(L[-1])
	else:
		print("Ingen indtastede sprog")


def add_to_list(L):
	global num_languages
	user_language = input("Enter a language: ")
	L.append(user_language)
	num_languages -= 1


num_languages = int(input("Indtast antal programmeringssprog: "))
while num_languages > 0:
	print_menu()

print_list(languages_list)