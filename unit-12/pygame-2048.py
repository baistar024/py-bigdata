import pygame
from random import randint, randrange, choice
from collections import defaultdict

lettercode = [ord(x)  for x in 'WSADQRwsadqr']
for code in lettercode:
    print(code)
action = ["up", "down", "left", "right", "quit", "reset"]
actiondict = dict(zip(lettercode, action*2))
for k in actiondict.keys():
    print(k, actiondict[k])
fields = [[0 for i in range(4)] for j in range(4)]
print(fields)
new_element = 4 if randrange(100) > 89 else 2
(i, j) = choice([(i, j) for i in range(4) for j in range(4) if fields[i][j] == 0])
fields[i][j] = new_element
for field in fields:
    print("-" * 50)
    for cell in field:
        print(cell, end = "    ")
    print()
    newrow = [i for i in field if i != 0]
    newrow += [0 for i in range(len(field)-len(newrow))]

    for cell in newrow:
        print(cell, end= "    ")
    print()



class Game2048():
    def __init__(self, rows =4, column = 4, winvalue = 2048 ):
        self.rows, self.columns = rows, column
        self.winvalue = winvalue
        self.userscore = 0
        self.hightscore = 0
        self.reset()
    def reset(self):
        if self.userscore > self.hightscore:
            self.hightscore = self.userscore
            self.userscore = 0
        self.field = [[0 for i in range(self.rows)] for j in range(self.columns)]
        self.genatom()
        self.genatom()

    def genatom(self):
        pass



def initgame():
    winsize = 640, 640
    pygame.init()
    screen = pygame.display.set_mode(winsize)
    pygame.display.set_caption("game:2048")
    screen.fill((233,233,233))
    pygame.display.update()
    return screen
# game = initgame()
# while True:
#     event = pygame.event.wait()
#     if event.type == pygame.QUIT:
#         pygame.quit()
#         exit()
#
#     pygame.display.update()



