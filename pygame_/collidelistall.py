import pygame

pygame.init()

obstacles = [
    pygame.Rect(350, 150, 100, 100),
    pygame.Rect(300, 300, 150, 50),
    pygame.Rect(500, 200, 50, 150),
    pygame.Rect(400, 400, 200, 50)
]
# 충돌 감지를 수행할 대상
moving_rect = pygame.Rect(420, 220, 100, 100)

collision_indices = moving_rect.collidelistall(obstacles)

if collision_indices:
    print(f"moving_rect가 obstacles[{collision_indices}]와 충돌")
else:
    print("충돌이 없습니다.")