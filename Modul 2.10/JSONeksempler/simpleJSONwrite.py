# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 14:44:16 2018

Eksempel med at skrive JSON fil

@author: HTH
"""

import json

# Laver en Python dictionary med to dictionaries indeni
presidenter = {"Donald Trump": {"Parti": "Republikaner", "Valgperiode": "2016-"}, 
               "Barack Obama": {"Parti": "Demokrat", "Valgperiode": "2008-2016"}}

filNavn = "presidenter.json"

# Skriver dette data til en JSON fil med dump

# Vi laver json filen nemmere at læse med indent-kommandoen
with open(filNavn, "w") as filObjekt:
    json.dump(presidenter, filObjekt, indent=4)
    
filNavnNoIndent = "presidenterNoIndent.json"
# Uden indentering indeholde JSON filen bare en linje
with open(filNavnNoIndent, "w") as filObjekt:
    json.dump(presidenter, filObjekt)
    
# Skriver dette data til en string variabel med dumps
presStr = json.dumps(presidenter)

# Skriver til en string variabel med indentering
presIndentStr = json.dumps(presidenter, indent=4)