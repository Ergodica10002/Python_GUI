# this is referenced from https://blog.techbridge.cc/2019/10/19/how-to-build-up-game-with-pygame-tutorial/
import sys
import random
import pygame
from pygame.locals import QUIT

# 初始化
pygame.init()
# 建立 window 視窗畫布，大小為 800x600
screen = pygame.display.set_mode((640, 360))
# 設置視窗標題為 Hello World:)
pygame.display.set_caption('Circle Bouncing!')
# 清除畫面並填滿背景色
screen.fill((255, 255, 255))

color = [255,255,0]
position = [320, 200]
velocity = [random.uniform(0, 0.5), random.uniform(0, 0.5)]
radius = 15

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()

# 事件迴圈監聽事件，進行事件處理
running = True
while running:
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))

    position[0] += velocity[0]
    position[1] += velocity[1]

    if position[0] < 0 or position[0] > 640:
        velocity[0] = -velocity[0]
    if position[1] < 0 or position[1] > 360:
        velocity[1] = -velocity[1]

    pygame.draw.circle(screen, color, position, radius)
    pygame.display.update()