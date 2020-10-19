# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:52:19 2018

Eksempel på at tegne et rektangel og cirkel i pygame

@author: HTH
"""

# Importerer pygame
import pygame

# Initialiserer alle funktioner i pygame
pygame.init()

# Indstiller vinduestørrelse og vinduetekst
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Eksempel på tegning i pygame")

gameLoop = True

# Spil-loopet, som kører for evigt, indtil vi klikker på X i højre hjørne
while gameLoop:
    
    # Tjek for events (hændelser)
    events = pygame.event.get()
    for event in events:
        # Hvis vi trykker på det røde kryds i højre hjørne, afsluttes spillet
        if event.type == pygame.QUIT:
            gameLoop = False

    color = (0,255,0)
    pygame.draw.rect(screen, color, pygame.Rect(20, 20, 60, 60))
    
    color = (128,0,128)
    pygame.draw.circle(screen, color, (100,100), 20)
    
    color = (0,128,255)
    pygame.draw.line(screen, color, (120,150), (400,300), 10)
            
    # Opdaterer indholdet i vinduet
    pygame.display.flip()
    
# Afslutter Pygame
pygame.quit()