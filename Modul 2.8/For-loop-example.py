# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 2020

Vi skal lave et program som gør følgende:
	Opretter en liste med tre programmeringssprog
	Printer hvert af programmeringssprogene i listen på hver sin linje

@author: SVU
"""

# initialise list
languages_list = ["C", "Python", "Java", "Go"]

# print all langnguages
for lang in languages_list:
	print(lang) # Add end=", " to print as comaseparated list

languages_list.remove("Java") # remove element by value
languages_list.pop(1) # remove element by index
#print all members of the language list based in index
num_elements = len(languages_list)
index_list = list(range(num_elements))
for index in index_list:
	print(index, ": ", languages_list[index])