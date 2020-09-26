import random

import pygame,sys

class Plane():
    def __init__(self, play_image_filename, play_pos):
        self.image = pygame.image.load(play_image_filename)
        self.plane_rect = self.image.get_rect()
        self.play_image = self.image.subsurface(self.plane_rect)
        self.plane_rect.midtop = play_pos
        self.speed = 2
        # 子弹是由玩家飞机发射的，所以创建列表，存储子弹对象，使该列表变为该类的属性
        self.bullets = []
        self.is_hitted = False

        # 生成函数，完成发射子弹动作，同时将每个子弹对象存在列表中

    def shoot(self, bullet_filename):
        bulletobj = Bullet(bullet_filename, self.plane_rect.midtop)
        self.bullets.append(bulletobj)

        # 向上移动，当飞机移动到边框位置时，无法移动

    def moveup(self):
        if self.plane_rect.top <= 0:
            self.plane_rect.top = 0
        else:
            self.plane_rect.top -= self.speed

        # 向下移动，当飞机移动到边框位置时，无法移动

    def movedown(self):
        if self.plane_rect.top >= 950 - self.plane_rect.height:
            self.plane_rect.top = 950 - self.plane_rect.height
        else:
            self.plane_rect.top += self.speed

        # 向右移动，当飞机移动到边框位置时，无法移动

    def moveleft(self):
        if self.plane_rect.left <= -40:
            self.plane_rect.left = -40
        else:
            self.plane_rect.left -= self.speed

        # 向左移动，当飞机移动到边框位置时，无法移动

    def moveright(self):
        if self.plane_rect.left >= 700 - self.plane_rect.width:
            self.plane_rect.left = 700 - self.plane_rect.width
        else:
            self.plane_rect.left += self.speed

class Enemy():
    def __init__(self, myimage, mypos):
        self.enemyimage = pygame.image.load(myimage)
        self.enemyrect = self.enemyimage.get_rect()
        self.enemysurface = self.enemyimage.subsurface(self.enemyrect)
        self.enemyrect.midbottom = mypos
        self.speed = 1
    def move(self):
        self.enemyrect.bottom += self.speed

class Bullet():
    def __init__(self,myimages,mypos):
        self.bulletimg = pygame.image.load(myimages)
        self.bulletrect = self.bulletimg.get_rect()
        self.bulletsurface = self.bulletimg.subsurface(self.bulletrect)
        self.bulletrect.midbottom = mypos
        self.speed = 2

    def move(self):
        self.bulletrect.top -= self.speed

clock = pygame.time.Clock()
def main():
    #init game
    pygame.font.init()
    pygame.init()
    clock.tick(50)
    window = (660,950)
    top, bottom, left, right = 0, 950, 0, 660
    color={"white":(255,255,255),"black":(0,0,0),"red":(255,0,0),"green":(0,255,0),"blue":(0,0,255)}
    bulletimage = "./images/bull3.png"
    planeimage = "./images/ship2.png"
    enemyimage = "./images/enemy.png"

    screen = pygame.display.set_mode(window,0,32)
    pygame.display.set_caption("飞机大战")
    background = pygame.image.load("./images/alien.jpg")
    bgsurface = pygame.transform.scale(background, window)

    bulletcount = 0
    enemycount = 0
    enemys = []
    planepos = (330, 600)
    player = Plane(planeimage, planepos)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_UP] or keypress[pygame.K_w]:
            player.moveup()
        if keypress[pygame.K_DOWN] or keypress[pygame.K_s]:
            player.movedown()
        if keypress[pygame.K_LEFT] or keypress[pygame.K_a]:
            player.moveleft()
        if keypress[pygame.K_RIGHT] or keypress[pygame.K_d]:
            player.moveright()

        screen.blit(bgsurface,(0,0))
        if not player.is_hitted:
            if bulletcount % 30 == 0:
                player.shoot(bulletimage)
            bulletcount += 1
            if bulletcount >= 30:
                bulletcount = 0
            # 让子弹动起来
            for i in player.bullets:
                i.move()
                screen.blit(i.bulletimg, i.bulletrect)
                # 当子弹飞出屏幕，删除子弹对象
                if i.bulletrect.bottom <= 0:
                    player.bullets.remove(i)
            # 按频率生成敌机
            if enemycount % 100 == 0:
                enemypos = [random.randint(30, 630), 0]
                enemyplane = Enemy(enemyimage, enemypos)
                # 将敌机对象添加到列表中
                enemys.append(enemyplane)
            enemycount += 1
            if enemycount >= 100:
                enemycount = 0
            # 让敌机动起来
            for i in enemys:
                i.move()
                screen.blit(i.enemyimage, i.enemyrect)
                # 当敌机飞出屏幕，删除敌机对象
                if i.enemyrect.bottom >= 950:
                    enemys.remove(i)
                # 遍历子弹对象，判断子弹是否击中敌机
                for j in player.bullets:
                    # 如果击中，分数增加，同时移除该子弹和敌机对象
                    if pygame.Rect.colliderect(j.bulletrect, i.enemyrect):
                        enemys.remove(i)
                        player.bullets.remove(j)
                # 遍历敌机对象，判断玩家是否和敌机相撞
                if pygame.Rect.colliderect(player.plane_rect, i.enemyrect):
                    # 修改is_hitted的值，跳出该层循环
                    player.is_hitted = True
                    break

            screen.blit(player.play_image, player.plane_rect)

            pygame.display.update()



main()
