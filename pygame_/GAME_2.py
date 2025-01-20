import pygame
import color

# 1. initialization
## <<--- 초기화
pygame.init()

screen_width = 800
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height))

# 환경 변수
rect_width = 400
rect_height = 400
rect = (0,0,color.blue,rect_width,rect_height)

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
    pygame.draw.rect(screen,(0,0),rect)
# 3. Termination
pygame.quit() 

[]