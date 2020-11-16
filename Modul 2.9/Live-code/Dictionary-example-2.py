# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 2020

Vi skal lave et program som gør følgende:
	Lav en dictionary over årstal for vinderne af VM i fodbold
	(se listen på https://en.wikipedia.org/wiki/FIFA_World_Cup).
	Her er keys de enkelte lande, og den tilhørende value er en liste med de(t) år som det pågældende land har vundet.
	Kald denne dictionary guldVMFodbold.
	Loop over denne dictionary og print antal mesterskaber og årstal for disse mesterskaber for hvert land.
	F.eks.: Brasilien har vundet 5 gange: [1958, 1962, 1970, 1994, 2002]

@author: SVU
"""

def print_dict(d):
    for country, years in d.items():
        print(country + "har vundet " + str(len(years)) + " gange: " + str(years))
        #print(f"{country} har vundet {len(years)} gange: {years}")
    #for country in d.keys(): # alternativ metode
        #print(f"{country} har vundet {len(d[country])} gange: {d[country]}")


world_cup_wins = {"Brazil":     [1958, 1962, 1970, 1994, 2002],
                  "Germany":    [1954, 1974, 1990, 2014],
                  "Italy":      [1934, 1938, 1982, 2006],
                  "Argentina":  [1978, 1986],
                  "France":     [1998, 2018],
                  "Uruguay":    [1930, 1950],
                  "England":    [1966],
                  "Spain":      [2010]}

print_dict(world_cup_wins)