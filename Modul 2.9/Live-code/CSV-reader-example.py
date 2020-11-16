# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 2020

Vi skal lave et program som gør følgende:
	Brug CSV reader til at læse CSV filen studerende.csv. Print på hver linje navn, uddannelse og alder.
	F.eks.: Navn: Jens Hansen, Studieretning: Design, Alder: 22 år.
	Skriv et program som beder en studerende om input i form af navn, studieretning og alder.
	Tilføj denne information til filen studerende.csv. Brug CSV writer til dette.

@author: SVU
"""
import csv

with open("../CSV/studerende.csv", "r+", newline="\n") as fileObject:
	cr = csv.reader(fileObject, delimiter=";")
	line = 0
	for studerende in cr:
		if line == 0:
			header = studerende
			line += 1
		else:
			for index in range(len(header)):
				if index < len(header)-1:
					print(f"{header[index]}: {studerende[index]}", end=", ")
				else:
					print(f"{header[index]}: {studerende[index]}", end="\n")

	cw = csv.writer(fileObject, delimiter=';')
	row = []
	for entry in header:
		row.append(input("Indtast " + entry))
	cw.writerow(row)