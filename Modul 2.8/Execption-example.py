# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 2020

Vi skal lave et program som gør følgende:
	Brugeren skal enten indtaste et programmeringssprog, som bliver tilføjet til en liste, eller fjerne et (eller flere programmeringssprog). Programmet skal køre indtil brugeren trykker på q.
	Når programmet kører, skal brugeren vælge om han vil indtaste et programmeringssprog, eller om han vi se de programmeringssprog som er indtastet
	Han kan desuden vælge at slette et valgfrit programmeringssprog fra listen. Dette kan han gøre indtil der ikke er flere programmeringssprog i listen
	Hvis han vælger at slette et programmeringssprog, som ikke er i listen, skal programmet informere ham om dette og køre videre.

@author: SVU
"""

languages_list = []
num_languages = 0

def print_menu():
	'''
	Prints the usermenu, and calls apropriate functions as needed
	'''
	print("L: print listen med indtastede programmeringssprog")
	print("T: tilføj programmeringssprog til listen")
	print("S: selt sprog fra listen")
	choise = input("Vælg funktion: ")
	if choise.upper() == "L":
		print_list(languages_list)
	elif choise.upper() == "T":
		add_to_list(languages_list)
	elif choise.upper() == "S":
		remove_from_list(languages_list)
	else:
		print_menu()

def print_list(L):
	'''
	Prints a given list L. If the list is empty, it will print "Ingen indtastede sprog"
	Args:
		L: List to be printed
	'''
	try:
		print("Du indtastede følgende sprog:")
		for index in range(len(L)-1):
			print(L[index], end=", ")
		print(L[-1])
	except IndexError:
		print("Ingen indtastede sprog")


def add_to_list(L):
	'''
	Adds a user-input to a given list L.
	Args:
		L: List to be added to
	'''
	global num_languages
	user_language = input("Enter a language to add: ")
	if user_language != "":
		L.append(user_language)
		num_languages -= 1

def remove_from_list(L):
	'''
	Removes a user given entry from a given list L.
	Args:
		L: List to have element removed from.
	'''
	try:
		global num_languages
		user_language = input("Enter a language to remove: ")
		L.remove(user_language)
		num_languages += 1
	except ValueError:
		print("Valgte sprog fantes ikke på listen")
	finally:
		print_menu()


num_languages = int(input("Indtast antal programmeringssprog: "))
while num_languages > 0:
	print_menu()

print_list(languages_list)