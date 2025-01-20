import pygame
import random
## <<--- 초기화
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

x = screen.get_size()[0]//2
y = screen.get_size()[1]//2

## <<-- fps 적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
fps = 30

# 이동속도
speed = 300 # 10픽셀 * 30프레임 = 300픽셀/초
radius = 40
color = [(255,0,0),(0,0,0),(255,255,0),(0,255,0),(0,0,255)]
current_color = random.choice(color)
## <<--- 메인 루프
running = True
while running:
    
    delta_time = clock.tick(fps) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                new_color = random.choice(color)
                while new_color == current_color:
                    new_color = random.choice(color)
                current_color = new_color
    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed * delta_time
    if keys[pygame.K_RIGHT]:
        x += speed * delta_time
    if keys[pygame.K_UP]:
        y -= speed * delta_time
    if keys[pygame.K_DOWN]:
        y += speed * delta_time
    if keys[pygame.K_SPACE]:
        y -= 30
    
    
    # 화면 경계체크
    if x - radius < 0 :
        x = radius
    if x + radius > screen_width:
        x = screen_width - radius
    if y - radius < 0:
        y = radius
    if y + radius > screen_height:
        y = screen_height - radius
        
    # 화면 그리기
    screen.fill((0, 0 , 0))
    pygame.draw.circle(screen, current_color, (x,y), radius)
    # 업데이트
    pygame.display.flip()
## 게임 종료
pygame.quit()