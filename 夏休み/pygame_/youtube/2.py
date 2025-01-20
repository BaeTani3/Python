import pygame
import random

pygame.init()

screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption("BYM")

x_pos = screen.get_size()[0] // 2
y_pos = screen.get_size()[1] // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x_pos, y_pos = pygame.mouse.get_pos()
            # 마우스가 움직일 때마다 색상을 변경
            RGB = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, RGB, (x_pos, y_pos), 5)
    pygame.display.flip()

pygame.quit()