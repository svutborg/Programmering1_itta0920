# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:45:23 2018

Looping over dictionaries

@author: HTH
"""

# Vi laver først en dictionary
guldVMFodbold = {'Brasilien': 5,
		   'Italien': 4,
		   'Tyskland': 4,
		   'Uruguay': 2,
		   'Argentina': 2,
		   'Frankrig': 2,
		   'England': 1,
		   'Spanien': 1}

# Printer hvor mange gange hvert enkelt land har vundet
for land in list(guldVMFodbold.keys()):
    print(land + " har vundet " + str(guldVMFodbold[land]) + " gange.")