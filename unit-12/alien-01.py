import pygame
import sys

def playGame():
    # step 1
    pygame.init()
    # step 2
    screen =pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    bgcolor = (230, 230, 230)
    # step 3
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.fill(bgcolor)
        pygame.display.flip()

playGame()


