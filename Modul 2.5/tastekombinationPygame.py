# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:43:40 2018

Eksempel med tastekombinationen Ctrl+R i Pygame.

@author: HTH
"""
# Importerer pygame
import pygame

# Initialiserer alle funktioner i pygame
pygame.init()

# Indstiller vinduestørrelse og vinduetekst
screen = pygame.display.set_mode((300,200))
pygame.display.set_caption("Eksempel med tastekombinaion i Pygame")

gameLoop = True

# Spil-loopet, som kører for evigt, indtil vi klikker på X i højre hjørne
while gameLoop:
    
    # Tjek for events (hændelser)
    events = pygame.event.get()
    for event in events:
        # Hvis vi trykker på det røde kryds i højre hjørne, afsluttes spillet
        if event.type == pygame.QUIT:
            gameLoop = False
            
        # Tjekker om Ctrl er holdt nede
        pressed = pygame.key.get_pressed()
        ctrl_holdt_nede = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        # Læg mærke til at ctrl_holdt_nede er booleansk
        if ctrl_holdt_nede:
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                print("Du trykkede på Ctrl+R")
            
        else:
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                
                print("Du trykkede kun på R")

    # Opdaterer indholdet i vinduet
    pygame.display.flip()
    
# Afslutter Pygame
pygame.quit()