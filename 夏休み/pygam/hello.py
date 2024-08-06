import time
import pygame
import random

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))



# 색상 정의
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)

screen.fill(WHITE)
pygame.display.flip()

#
N = random.randint(5,20)
for _ in range(N): 
    RGB = (random.randint(0, 255)),(random.randint(0, 255)),(random.randint(0, 255))
    Size = random.randint(5, 100)
    X, Y = (random.randint(0, 799)), (random.randint(0,599))
    pygame.draw.circle(screen, (RGB), (X, Y), Size)

pygame.display.flip() 
# 화면 업데이트

time.sleep(2)
pygame.display.flip()


# 이벤트 처리
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
# 종료    
pygame.quit()

# 키보드나 마우스가 움직일 때 마다 이벤트가 발생한다.
# 