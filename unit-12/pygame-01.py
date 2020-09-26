import pygame   #导入pygame库
import sys      #导入sys库的exit()函数

#初始化游戏
## 1.创建游戏实例
pygame.init()
## 2.初始楷游戏窗口
screen = pygame.display.set_mode((480,640))
## 3.设置窗口标题
pygame.display.set_caption("外星人入侵")
# 数据准备
## 载入背景图片
# bgimgs = pygame.image.load("/images/bg.jpg")
bgcolor = (233,233,233)

screen.fill(bgcolor)

# 事件件处理
while True:
    event = pygame.event.wait()
    #
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    #显示处理

    pygame.display.update()





