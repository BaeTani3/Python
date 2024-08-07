import pygame
import color

# # 1. initialization
# ## <<--- 초기화
# pygame.init()

# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Image Movement")
# ## <<-- fps 적용을 위한 시간 객체 생성
# clock = pygame.time.Clock()
# fps = 60
# ## <<--- 메인 루프
# running = True

# # 이미지 로드
# blue_image = pygame.image.load("blue_rect.png")
# red_image = pygame.image.load("red_rect.png")

# # 이미지 초기 위치 설정
# blue_rect = blue_image.get_rect()
# blue_rect.topleft = (100, 100)

# red_rect = red_image.get_rect()
# red_rect.topleft = (200, 200)

# speed = 300
# delta_speed = 0

# # 2. Event Handling & Image creation
# while running:
#     delta_speed = speed * (clock.tick(fps) / 1000.0)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
            
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         blue_rect.x -= delta_speed
#     if keys[pygame.K_RIGHT]:
#         blue_rect.x += delta_speed
#     if keys[pygame.K_UP]:
#         blue_rect.y -= delta_speed
#     if keys[pygame.K_DOWN]:
#         blue_rect.y += delta_speed
#     if keys[pygame.K_a]:
#         red_rect.x -= delta_speed
#     if keys[pygame.K_d]:
#         red_rect.x += delta_speed
#     if keys[pygame.K_w]:
#         red_rect.y -= delta_speed
#     if keys[pygame.K_s]:
#         red_rect.y += delta_speed    
#     blue_rect.x = max(0, min(blue_rect.x, screen.get_width() - blue_rect.width))    
#     blue_rect.y = max(0, min(blue_rect.y, screen.get_height() - blue_rect.height))
#     red_rect.x = max(0, min(red_rect.x, screen.get_width() - red_rect.width))    
#     red_rect.y = max(0, min(red_rect.y, screen.get_height() - red_rect.height)) 
    
    
#     screen.fill(color.rand)
    
#     screen.blit(blue_image, blue_rect)
#     screen.blit(red_image, red_rect)
#     if red_rect.colliderect(blue_rect):
#         print("충돌 발생")
#         break
#     else:
#         print("충돌 없음")
    
#     pygame.display.flip()
# # 3. Termination
# pygame.quit()

# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()
# running = True

# # 사각형 정의
# rect1 = pygame.Rect(screen.get_width()//2 - 40, 0, 80, 40)

# # 객체 이동 속도
# speed = 200 # 200 pixel / 1 sec
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     dt = clock.tick(30) / 1000

#     rect1.y += speed * dt
    
#     # if rect1.x + rect1.width 값이 > screen.width
#     #    rect1.x = screen.width - rect1.width
    
#     # if rect1.x + rect1.width > screen.get_width():
#     #     rect1.x = screen.get_width() - rect1.width
#     #     speed = -speed 
#     # if rect1.x < 0:
#     #     rect1.x = 0
#     #     speed = -speed
    
#     if rect1.bottom > screen.get_height():
#         rect1.y = screen.get_height() - rect1.height
#         speed = -speed
#     if rect1.top < 0:
#         rect1.y = 0
#         speed = -speed
        
    
#     # 화면을 흰색으로 칠한다.
#     screen.fill((255, 255, 255))

#     pygame.draw.rect(screen, (255, 0, 255), rect1) # Rect 객체 이용
    
    
#     # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
#     pygame.display.flip()
    
    
# pygame.quit()

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 사각형 정의
rect1 = pygame.Rect(screen.get_width()/2 - 40 , 0, 80, 40)

# 객체 이동 속도
speed = 300 # 300 pixel / second

count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: # 키보드가 눌러졌다.
            if event.key == pygame.K_LEFT: # 어떤 Key가 눌러졌습니까?
                 print("왼쪽 화살표 클릭: ", count)
                 count += 1

    dt = clock.tick(60) / 1000 # dt 프로그램 실행 멈춤.

    # <-,  -> Key를 누를 때 사각형을 좌우로 이동.
    # 키보드 입력 처리
    keys = pygame.key.get_pressed()

    
        # 왼쪽 방향키가 눌러졌을 때
    if keys[pygame.K_LEFT]:
        rect1.x = rect1.x - speed * dt

    # 오른쪽 방향키가 눌러졌을 때
    elif keys[pygame.K_RIGHT]:
        rect1.x += speed *dt

    
    
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), rect1) # Rect 객체 이용
    
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    
pygame.quit()



