import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("YM")

fps = pygame.time.Clock()

x_pos = screen.get_size()[0]//2 # 240
y_pos = screen.get_size()[1]//2 # 180

to_x = 0
to_y = 0

running = True
# 파일 계속해서 실행하기 위한 while문
while running:
    deltatime = fps.tick(120) # 1초에 60번만 돌거야
    for event in pygame.event.get():
        RGB = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # print(event.type)
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y = -1
            elif event.key == pygame.K_DOWN:
                to_y = 1
            elif event.key == pygame.K_LEFT:
                to_x = -1
            elif event.key == pygame.K_RIGHT:
                to_x = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_y = 0
            elif event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0
            elif event.key == pygame.K_RIGHT:
                to_x = 0
            
    x_pos += to_x
    y_pos += to_y
    
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (RGB), (x_pos, y_pos), 50)
    # pygame.draw.circle(surface, color, center, radius)
    pygame.display.flip()
    
pygame.quit()
