import pygame

# 1. initialization
## <<--- 초기화
pygame.init()

screen = pygame.display.set_mode((800, 600))
## <<-- fps 적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
## <<--- 메인 루프
running = True

# 2. Event Handling & Image creation
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    
# 3. Termination
pygame.quit()