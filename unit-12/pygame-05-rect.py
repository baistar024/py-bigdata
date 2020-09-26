import pygame, sys
# test 当前位置是否可以移动图片
def ismove(pos,rect):
    x, y = pos
    rx,ry,rw,rh =rect
    if (rx<=x<=rx+rw) and (ry<=y<=ry+rh):
        return True
    else:
        return False

pygame.init()
window = 600, 600
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Picture drage")

image = pygame.image.load("./images/ship.png")
imgx, imgy = 100, 100
screen.blit(image,(imgx,imgy))
pygame.display.flip()
pygame.display.update()

moving =False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            w,h = image.get_size()
            moving = ismove(event.pos, (imgx,imgy,w,h))
            if event.type == pygame.MOUSEBUTTONUP:
                moving = False
        if event.type == pygame.MOUSEMOTION:
            if moving:
                screen.fill((255,255,255))
                x,y = event.pos
                imgw,imgh = image.get_size()
                imgx = x - int(imgw/2)
                imgy = y - int(imgh/2)
                screen.blit(image,(imgx,imgy))
                pygame.display.update()



