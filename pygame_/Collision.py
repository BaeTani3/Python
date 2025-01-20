import pygame
import color

# 1. initialization
## <<--- 초기화
pygame.init()

screen = pygame.display.set_mode((800, 600))
## <<-- fps 적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
fps = 30
## <<--- 메인 루프
running = True

# 사각형 초기화 
rect1 = pygame.Rect(300, 220, 60, 60) 
rect2 = pygame.Rect(100, 100, 60, 60)
rect1_speed = [10, 10]
rect2_speed = [5, 5]

# 2. Event Handling & Image creation
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    clock.tick(fps)
    
    # 사각형 움직임
    rect1 = rect1.move(rect1_speed)
    rect2 = rect2.move(rect2_speed)
    
    # 화면 경계에 충돌 처리 (rect1)
    if rect1.left < 0 or rect1.right > 800:
        rect1_speed[0] = -rect1_speed[0]
    if rect1.top < 0 or rect1.bottom > 600:
        rect1_speed[1] = -rect1_speed[1]
    # rect2
    if rect2.left < 0 or rect2.right > 800:
        rect2_speed[0] = -rect2_speed[0]
    if rect2.top < 0 or rect2.bottom > 600:
        rect2_speed[1] = -rect2_speed[1]
    # 충돌 감지
    if rect1.colliderect(rect2):
        print("Collision Detected!")
    
    screen.fill(color.black)
    pygame.draw.rect(screen, color.rand, rect1)
    pygame.draw.rect(screen, color.rand, rect2)
    
    pygame.display.flip() 
       
# 3. Termination
pygame.quit()