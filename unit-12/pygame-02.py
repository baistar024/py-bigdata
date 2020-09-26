# -*- coding: UTF-8 -*-
import pygame,sys,time
from random import randint
# 初始化

pygame.init()
window = (600, 600)
bgcolor =(233,233,233)
font = pygame.font.SysFont("微软雅黑", 20)
font_height = font.get_linesize()
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Pygame-ball")
eventtext = []

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()

    eventtext.append(str(event))
    eventtext = eventtext[int(-window[1] / font_height):]
    screen.fill(bgcolor)
    y = window[1] - font_height

    for text in eventtext:
        screen.blit(font.render(text, True, (randint(0, 255), randint(0, 255), randint(0, 255))), (0, y))
        y -= font_height
    pygame.display.update()


