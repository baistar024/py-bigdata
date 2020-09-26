import pygame, sys

# init pygame
window = (640, 480)
screen = pygame.display.set_mode(window,0,32)
pygame.display.set_caption("ball")
background = pygame.image.load("./images/ship.png")
x, y = 0, 0
movex, movey = 0, 0
# handle event
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movex = -1
            elif event.key == pygame.K_RIGHT:
                movex = 1
            elif event.key == pygame.K_UP:
                movey = -1
            elif event.key == pygame.K_DOWN:
                movey = 1
        elif event.type == pygame.KEYUP:
            movex,movey = 0, 0
    x += movex
    y += movey
    # handle display
    screen.fill((33,33,33))
    screen.blit(background,(x,y))
    # display refresh
    pygame.display.update()