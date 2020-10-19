# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:38:24 2018

Eksempel med musen i Pygame.

@author: HTH
"""

# Importerer pygame
import pygame

# Initialiserer alle funktioner i pygame
pygame.init()

# Indstiller vinduestørrelse og vinduetekst
screen = pygame.display.set_mode((300,200))
pygame.display.set_caption("Eksempel med musen i Pygame")

gameLoop = True

# Spil-loopet, som kører for evigt, indtil vi klikker på X i højre hjørne
while gameLoop:
    
    # Tjek for events (hændelser)
    events = pygame.event.get()
    for event in events:
        # Hvis vi trykker på det røde kryds i højre hjørne, afsluttes spillet
        if event.type == pygame.QUIT:
            gameLoop = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Museknap trykket ned, position: " + str(pygame.mouse.get_pos()))
            
        if event.type == pygame.MOUSEMOTION:
            print("Musemarkørposition: " + str(pygame.mouse.get_pos()))
            
    # Opdaterer indholdet i vinduet
    pygame.display.flip()
    
# Afslutter Pygame
pygame.quit()