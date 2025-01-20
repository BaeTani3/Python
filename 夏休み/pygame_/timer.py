import pygame
import color

pygame.init()

start_time = pygame.time.get_ticks()

while True:
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    print(f"Elapsed time:{elapsed_time:.2f} seconds")
    
    if elapsed_time > 10.0:
        break
    