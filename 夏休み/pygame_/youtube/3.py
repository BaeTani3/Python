import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption("YM_pygame")

# 중심 좌표
x = screen.get_size()[0]//2
y = screen.get_size()[1]//2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    
    
    # 바둑판 만들기
    # for i in range(0,480,30):
    #     pygame.draw.line(screen, (255,0,0) , (i,0), (i,360))
    # for i in range(0,360,30):
    #     pygame.draw.line(screen, (255,0,0), (0, i), (480, i))
    # 선
    # pygame.draw.line(화면, 색, 시작 위치, 끝 위치, 선 굵기)
    pygame.draw.line(screen, (255,0,0) , (x,0), (x,y*2),5)
    pygame.draw.line(screen, (255,0,0) , (0,y), (x*2,y),5)
     
    pygame.draw.polygon(screen, (255,255,0), [[100,100], [400,200], [200,200]] ,10)
    
    pygame.display.update()
    
pygame.quit( )