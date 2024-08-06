import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Random circle drawer")

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            RGB = (random.randint(0, 255)),(random.randint(0, 255)),(random.randint(0, 255))
            radius = random.randint(10, 100)
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (RGB), (pos), radius)
            
        if event.type == pygame.KEYDOWN:
            if pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()              
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

            
    pygame.display.flip()
   
    
pygame.quit()