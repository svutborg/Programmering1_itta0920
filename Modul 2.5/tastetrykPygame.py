# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:51:51 2018

Eksempel med indtastning af navn og eventlisten

@author: HTH
"""

import pygame, time

pygame.init()

screen = pygame.display.set_mode((300,200))
pygame.display.set_caption("Tastetryk")

gameLoop = True

while gameLoop:
    
    # Tjek for events
    if pygame.event.peek(pygame.KEYDOWN):
        print("KEYDOWN")
    if pygame.event.peek(pygame.KEYUP):
        print("KEYUP")
    events = pygame.event.get()
    print("Events: ")
    print(events)
    
    for event in events:
        #print("----------START AF FOR LOOP-------------------")
        print("Antal events: ", len(events))
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Du trykkede space")
        if event.type == pygame.KEYDOWN:
            print("Du trykkede en knap ned")
        if event.type == pygame.KEYUP:
            print("Knappen hoppede op igen")
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            print("Du holdt op med at trykke på ESC")
            
    #print("+++++++++++UDE AF FOR LOOP+++++++++++++++++")          
    
    # Tjekker hvilke knapper er trykket
    #pressed = pygame.key.get_pressed()
    
    #print(pygame.K_ESCAPE)
    
    time.sleep(1)
            
    pygame.display.flip()
    
# Afslutter Pygame
pygame.quit()