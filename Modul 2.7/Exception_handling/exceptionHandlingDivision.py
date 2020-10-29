# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 21:24:19 2018

Eksempel med exception handling, hvor der laves en simpel beregning.

@author: HTH
"""

try:
    a = int(input("Indtast det første tal:"))
    b = int(input("Indtast det næste tal:"))
    resultat = a / b
    
except ZeroDivisionError:
    print("Fejl: Man kan ikke dele med nul.")
except ValueError:
    print("Fejl: Kan kun lave beregninger med tal.")
else:
    print("Resultat: " + str(resultat) + ".")
finally:
    print("Program færdigt.")