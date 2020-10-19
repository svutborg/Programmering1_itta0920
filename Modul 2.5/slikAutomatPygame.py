# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:00:52 2018

Denne fil skal bruges til at løse opgaven om slikautomaten.
Opgave 1

@author: HTH
"""

# Importerer pygame
import pygame

# Initialiserer alle funktioner i pygame
pygame.init()

# Indstiller vinduestørrelse og vinduetekst
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Hello World Pygame")

gameLoop = True

# Spil-loopet, som kører for evigt, indtil vi klikker på X i højre hjørne
while gameLoop:
    
    # Tjek for events (hændelser)
    events = pygame.event.get()
    for event in events:
        # Hvis vi trykker på det røde kryds i højre hjørne, afsluttes spillet
        if event.type == pygame.QUIT:
            gameLoop = False
            
    # Opdaterer indholdet i vinduet
    pygame.display.flip()
    
# Afslutter Pygame
pygame.quit()