# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:16:34 2018

Eksempel med at læse JSON fil

@author: HTH
"""

import json

filNavn = "presidenter.json"

# Åbner filen  og gemmer dens indhold i en dictionary
with open(filNavn, "r") as filObjekt:
    presidenterDict = json.load(filObjekt)