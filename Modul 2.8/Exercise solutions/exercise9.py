"""
9: Prøv at lave en loggingsfil med Pygame.
Dvs. hver gang du trykker på en af knapperne W, A, S eller D, bliver dette gemt
i en logfil. F.eks. hvis du trykker på knappen ”W”, skal programmet skrive W i filen,
efterfulgt af mellemrum. Hvis du holder en knap nede, skal programmet kun skrive
hvilken knap det er én gang i filen. Når du afslutter programmet prøv at tjekke
hvad blev skrevet i filen. Du kan selv vælge hvad logfilen skal hedde.
"""

import pygame

# initialise pygame engine and window
pygame.init()
gameLoop = True
pygame.display.set_mode((200, 200))

# open "logfile.txt" for writing, note that the file is automatically closed by using the with statement
with open("logfile.txt", "w") as f:
	while gameLoop: 
		events = pygame.event.get()

		for event in events:

			# stops the gameloop if the window is closed
			if event.type == pygame.QUIT:
				gameLoop = False
			# if the event is a keypress, log the given key
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					f.write("W ")
				if event.key == pygame.K_a:
					f.write("A ")
				if event.key == pygame.K_s:
					f.write("S ")
				if event.key == pygame.K_d:
					f.write("D ")

		pygame.display.flip()