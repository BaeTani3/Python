import pygame
import color
import random
pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('collidelist Example')

obstacles = [
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
    pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150))
]

moving_rect = pygame.Rect(0, 0, 4, 4)

speed = 300
clock = pygame.time.Clock()
## <<--- 메인 루프
running = True

# 2. Event Handling & Image creation
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 이전 위치 저장
    previous_position = moving_rect.topleft
    dt = clock.tick(60) / 1000.0
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += speed * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= speed * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += speed * dt
    
    # 충돌 감지
    collision_index = moving_rect.collidelist(obstacles)
    if collision_index != -1:
        print(f"{collision_index}")
        
        moving_rect.topleft = previous_position    
        
    screen.fill((255,255,255))
    
    # 장애물 그리기
    for obs in obstacles:
        pygame.draw.rect(screen, color.rand, obs)
        
    pygame.draw.rect(screen, color.red, moving_rect)
    
    pygame.display.flip()
# 3. Termination
pygame.quit()

# 
    
