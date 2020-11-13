"""
8: Skriv et program som læser linjerne fra filen municipalities.txt
(find den i Canvas, under dagens modul) og derefter finder ud af hvad det længste kommunenavn er.
Hint: Start med at læse alle navnene i en liste, og loop derefter gennem listen, hvor du i hvert gennemløb holder styr
på hvad det længste navn er. Husk at inkludere passende exceptions.
"""

longest_name = 0 # variable to keep track of the longest name
try:
	with open('municipalities.txt', 'r') as f: # opens the file in read mode
		municipalities = f.readlines() # reads all lines in the file into a list
		for municipality in municipalities: # iterate through list
			if len(municipality) > longest_name: # if a municipality is larger, assign it as the new longest length
				longest_name = len(municipality)
except OSError: # the open() can raise an OSError if the file could not be opened.
	print("File cloud not be opened!")
finally: # As an extra bonus, the length record is printed
	print(f"The longest municipality name is {longest_name} characters long")