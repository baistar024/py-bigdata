# _*_coding:utf-8_*_
import pygame, sys

#init pygame
pygame.init()
window = 800, 600
screen = pygame.display.set_mode(window,0,32)
#文字示例
myfont = pygame.font.SysFont("微软雅黑", 40)
text_surface = myfont.render(u"This is a demo",True,(255,200,200))
x, y = -text_surface.get_width(), 300
bgimg = pygame.image.load("./images/bgimg2.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(bgimg,(0,0))
    x -= 0.2
    if x < -text_surface.get_width():
        x = 800-text_surface.get_width()
    screen.blit(text_surface,(x,y))
    pygame.display.update()

