import pygame
from pygame.locals import *
from sys import exit
import time
import random


# 创建子弹类，把子弹的图片转化为图像对象，设定固定的移动速度
class Bullet():
    def __init__(self, bulletfilename, bulletpos):
        self.bulletimg = pygame.image.load(bulletfilename)
        self.bullet_rect = self.bulletimg.get_rect()
        self.bullet_image = self.bulletimg.subsurface(self.bullet_rect)
        self.bullet_rect.midbottom = bulletpos
        self.speed = 2

    def move(self):
        self.bullet_rect.top -= self.speed


# 创建玩家飞机类，用面向对象的思想来对待
class play_plane_fly():
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


# 生成敌机类，设定固定的移动速度
class Enemy():
    def __init__(self, enemyfilename, enemypos):
        self.img = pygame.image.load(enemyfilename)
        self.enemy_rect = self.img.get_rect()
        self.enemy_image = self.img.subsurface(self.enemy_rect)
        self.enemy_rect.midbottom = enemypos
        self.speed = 1

    def move(self):
        self.enemy_rect.bottom += self.speed




clock = pygame.time.Clock()
def main():
    # 初始化文字屏幕
    pygame.font.init()
    # 初始化图像屏幕
    pygame.init()
    # 设定游戏帧
    clock.tick(50)
    # 设定游戏屏幕大小
    screen = pygame.display.set_mode((660, 950))
    # 设定游戏名称
    pygame.display.set_caption('飞机大战')
    # 加载背景图片，生成图像对象
    background = pygame.image.load('image/background.png').convert()
    backgroundsurface = pygame.transform.scale(background, (660, 950))
    # 加载游戏结束图片，生成图像对象
    gameover = pygame.image.load('image/gameover.png').convert()
    gameoversurface = pygame.transform.scale(gameover, (660, 950))
    playplanefilename = 'image/myself.png'
    planepos = [330, 600]
    player = play_plane_fly(playplanefilename, planepos)
    bulletfilename = 'image/bullet.png'
    # 按频率生成子弹，初始化数字为0
    bullet_frequency = 0
    enemyfilename = 'image/airplane.png'
    # 按频率生成敌机，初始化数字为0
    enemy_frequency = 0
    enemys = []
    myfont = pygame.font.SysFont("arial", 40)
    textImage = myfont.render("Score ", True, (0, 0, 0))
    # 初始化得分为0
    Score = 0
    # 敌机被子弹击中时的动画，将每张图片的图像对象存在列表中
    enenys_down = []
    enemy0_down = pygame.image.load('image/airplane_ember0.png')
    enemy0_down_rect = enemy0_down.get_rect()
    enemydown0 = enemy0_down.subsurface(enemy0_down_rect)
    enenys_down.append(enemydown0)
    enemy1_down = pygame.image.load('image/airplane_ember1.png')
    enemy1_down_rect = enemy1_down.get_rect()
    enemydown1 = enemy1_down.subsurface(enemy1_down_rect)
    enenys_down.append(enemydown1)
    enemy2_down = pygame.image.load('image/airplane_ember2.png')
    enemy2_down_rect = enemy2_down.get_rect()
    enemydown2 = enemy2_down.subsurface(enemy2_down_rect)
    enenys_down.append(enemydown2)
    enemy3_down = pygame.image.load('image/airplane_ember3.png')
    enemy3_down_rect = enemy3_down.get_rect()
    enemydown3 = enemy3_down.subsurface(enemy3_down_rect)
    enenys_down.append(enemydown3)

    while True:
        # 动态显示得分
        score = str(Score)
        myscore = pygame.font.SysFont("arial", 40)
        scoreImage = myscore.render(score, True, (0, 0, 0))
        # 判断事件，防止卡顿或者意外退出
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP] or key_pressed[K_w]:
            player.moveup()
        if key_pressed[K_DOWN] or key_pressed[K_s]:
            player.movedown()
        if key_pressed[K_LEFT] or key_pressed[K_a]:
            player.moveleft()
        if key_pressed[K_RIGHT] or key_pressed[K_d]:
            player.moveright()

        screen.blit(backgroundsurface, (0, 0))

        if not player.is_hitted:
            # 按频率生成子弹
            if bullet_frequency % 30 == 0:
                player.shoot(bulletfilename)
            bullet_frequency += 1
            if bullet_frequency >= 30:
                bullet_frequency = 0
            # 让子弹动起来
            for i in player.bullets:
                i.move()
                screen.blit(i.bullet_image, i.bullet_rect)
                # 当子弹飞出屏幕，删除子弹对象
                if i.bullet_rect.bottom <= 0:
                    player.bullets.remove(i)
            # 按频率生成敌机
            if enemy_frequency % 100 == 0:
                enemypos = [random.randint(30, 630), 0]
                enemyplane = Enemy(enemyfilename, enemypos)
                # 将敌机对象添加到列表中
                enemys.append(enemyplane)
            enemy_frequency += 1
            if enemy_frequency >= 100:
                enemy_frequency = 0
            # 让敌机动起来
            for i in enemys:
                i.move()
                screen.blit(i.enemy_image, i.enemy_rect)
                # 当敌机飞出屏幕，删除敌机对象
                if i.enemy_rect.bottom >= 950:
                    enemys.remove(i)
                # 遍历子弹对象，判断子弹是否击中敌机
                for j in player.bullets:
                    # 如果击中，分数增加，同时移除该子弹和敌机对象
                    if pygame.Rect.colliderect(j.bullet_rect, i.enemy_rect):
                        Score += 100
                        enemys.remove(i)
                        player.bullets.remove(j)
                        for k in enenys_down:
                            screen.blit(k, i.enemy_rect)
                # 遍历敌机对象，判断玩家是否和敌机相撞
                if pygame.Rect.colliderect(player.plane_rect, i.enemy_rect):
                    # 修改is_hitted的值，跳出该层循环
                    player.is_hitted = True
                    break

            screen.blit(player.paneimage, player.planerect)
            screen.blit(textImage, (0, 0))
            screen.blit(scoreImage, (110, 0))
            pygame.display.update()
        # 玩家退出时显示分数和游戏结束
        else:
            screen.blit(gameoversurface, (0, 0))
            screen.blit(textImage, (0, 0))
            screen.blit(scoreImage, (110, 0))
            pygame.display.update()
            time.sleep(2)
            break


main()