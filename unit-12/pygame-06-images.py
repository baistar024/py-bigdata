import pygame, sys

pygame.init()

window = 600, 600
screen = pygame.display.set_mode(window)
screen.fill((255,255,255))
# load images
image = pygame.image.load("./images/bgimg2.jpg")
imgsize = image.get_size()
print(imgsize)
# transform image
scaleimg = pygame.transform.scale(image,(120,90))
rotateimg = pygame.transform.rotate(image,-90)
rotzoomimg = pygame.transform.rotozoom(image,90,0.5)

#render  image to screen
screen.blit(image,(0,0))
screen.blit(scaleimg,(30,30))
screen.blit(rotateimg,(60,60))
screen.blit(rotzoomimg,(30,120))

#show screen

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
