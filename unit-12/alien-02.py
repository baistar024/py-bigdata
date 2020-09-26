import sys
import pygame
from setting import Setting
from ship import Ship


def run_game():
    pygame.init()
    alien_setting = Setting()
    screen = pygame.display.set_mode(alien_setting.screenSize)
    pygame.display.set_caption("外星人入侵")
    ship = Ship(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(alien_setting.bgcolor)
        ship.blitme()
        pygame.display.flip()

run_game()