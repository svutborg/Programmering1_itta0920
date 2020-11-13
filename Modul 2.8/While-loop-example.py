# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 2020

Vi skal lave et program som gør følgende:
	Brugeren skal indtaste så mange programmeringssprog han/hun vil, og de skal hvert især tilføjes til en liste.
	Når brugeren trykker på q, skal programmet afsluttes
	Før programmet afsluttes, skal alle programmeringssprogene som brugeren har tilføjet, printes i konsollen

@author: SVU
"""
#initialising list
languages_list = []

#initialising command variable
command = ""
# keep getting commmands from the user, until q is entered
while command != "q":
	command = input("Enter a programming language: ")
	languages_list.append(command)

# removing "q" from the list before printing
languages_list.remove("q") # alternatively pop(-1)
print(languages_list)