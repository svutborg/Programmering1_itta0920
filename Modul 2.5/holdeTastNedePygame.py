# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:14:32 2018

Et eksempel på hvordan man kan registrere at en person holder space nede.

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
            
    # Får en tuppel over de knapper som er trykket ned
    pressed = pygame.key.get_pressed()
    
    # Tjekker om space er trykket ned, og printer Space på en ny linje 
    # sålænge den er det
    if pressed[pygame.K_SPACE]:
        print("Space", end=" ")
            
    # Opdaterer indholdet i vinduet
    pygame.display.flip()

# Afslutter Pygame
pygame.quit()