# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 2020

Vi skal lave et program som gør følgende:
	Opretter en liste med tre programmeringssprog
	Tilføjer et programmeringssprog i slutningen listen
	Tilføjer input fra brugeren i starten af listen
	Printer listen

@author: SVU
"""

# initialise list
languages_list = ["C", "Python", "Java"]

# adding element to the end of the list
languages_list.append("Go")

# asking user for input and adding the userinput to the start of the list
user_language = input("Enter a programming language: ")
languages_list.insert(0, user_language)

# print the list
print(languages_list)