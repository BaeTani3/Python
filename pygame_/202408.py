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

# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()
# running = True

# # 사각형 정의
# rect1 = pygame.Rect(screen.get_width()/2 - 40 , 0, 80, 40)

# # 객체 이동 속도
# speed = 300 # 300 pixel / second

# count = 0
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN: # 키보드가 눌러졌다.
#             if event.key == pygame.K_LEFT: # 어떤 Key가 눌러졌습니까?
#                  print("왼쪽 화살표 클릭: ", count)
#                  count += 1

#     dt = clock.tick(60) / 1000 # dt 프로그램 실행 멈춤.

#     # <-,  -> Key를 누를 때 사각형을 좌우로 이동.
#     # 키보드 입력 처리
#     keys = pygame.key.get_pressed()

    
#         # 왼쪽 방향키가 눌러졌을 때
#     if keys[pygame.K_LEFT]:
#         rect1.x = rect1.x - speed * dt

#     # 오른쪽 방향키가 눌러졌을 때
#     elif keys[pygame.K_RIGHT]:
#         rect1.x += speed *dt

    
    
#     # 화면을 흰색으로 칠한다.
#     screen.fill((255, 255, 255))

#     pygame.draw.rect(screen, (0, 0, 255), rect1) # Rect 객체 이용
    
    
#     # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
#     pygame.display.flip()
    
    
# pygame.quit()


# pygame.init()

# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()
# running = True

# # 사각형 정의
# rect1 = pygame.Rect(screen.get_width()/2 - 40 , 0, 80, 40)
# rect2 = pygame.Rect(0, 0, 300, 200)
# rect2.center = screen.get_rect().center


# # 객체 이동 속도
# speed = 300 # 300 pixel / second

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     dt = clock.tick(60) / 1000 # dt 프로그램 실행 멈춤    

#     # 빨간색 사각형의 이전 좌표를 저장    
#     previous_pos = rect1.topleft
    
#     keys = pygame.key.get_pressed()
    
#     # 왼쪽 방향키가 눌러졌을 때
#     if keys[pygame.K_LEFT]:
#         rect1.x = rect1.x - speed * dt      

#     # 오른쪽 방향키가 눌러졌을 때
#     if keys[pygame.K_RIGHT]:
#         rect1.x += speed * dt 
        
#     # 아래쪽 방향키가 눌러졌을 때
#     if keys[pygame.K_DOWN]:
#         rect1.y += speed * dt
    
#     # 위쪽 방향키가 눌러졌을 때
#     if keys[pygame.K_UP]:
#         rect1.y -= speed * dt
    
#     # 화면 경계 처리    
#     rect1.x = max(0, min(rect1.x, screen.get_width() - rect1.width))
#     rect1.y = max(0, min(rect1.y, screen.get_height() - rect1.height))

#     # 충돌 감지
#     # if rect1.colliderect(rect2):
#     #     rect1.topleft = previous_pos
 
#     # 화면을 흰색으로 칠한다.
#     screen.fill((255, 255, 255))
#     pygame.draw.rect(screen, (255, 0, 0), rect1) 
#     pygame.draw.rect(screen, (0, 0, 255), rect2) 
   

    
#     # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
#     pygame.display.flip()
    
    
# pygame.quit()

import random
import pygame

pygame.init()

# <<-- 환경 변수 설정
# 화면 사이즈
screen_width = 800
screen_height = 600

# 장애물 사이즈
obs_width = 200
obs_height = 100

# 장애물 개수
num_of_obs = 5

# 아이템 사이즈
item_width = 50
item_height = 50

# 아이템 개수
num_of_item = 10

# 무빙 사각형 사이즈
mr_width = 50
mr_height = 50

speed = 100
## -->>
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True


# 장애물을 랜덤하게 생성
obs_list = []
for _ in range(num_of_obs):
    # 충돌이 일어나기에
    while True:
        rect_x = random.randint(0, screen_width - obs_width) # 0 <= x <= 600
        rect_y = random.randint(0, screen_height - obs_height) # 0 <= y <= 500
        rect = pygame.Rect(rect_x, rect_y, obs_width, obs_height)
        
        # 새롭게 생성된 장애물 사각형이 기 장애물과 충돌이 없다면
        if rect.collidelist(obs_list) == -1:
            # 새롭게 생성된 장애물을 리스트에 추가
            obs_list.append(rect)
            # 반복문 종료
            break
# 아이템을 랜덤하게 생성
item_list = []
for _ in range(num_of_item):
    while True:
        item_x = random.randint(0, screen_width - item_width)
        item_y = random.randint(0, screen_height - item_height)
        item = pygame.Rect(item_x, item_y, item_width, item_height)
        
        # 아이템과 기 아이템 간 충돌이 없어야 되고 and 아이템과 장애물간 충돌이 없어야 된다.
        if item.collidelist(item_list) == -1 and item.collidelist(obs_list) == -1:
            item_list.append(item)
            break
        
# moving rect 만들기
while True:
    mr_x = random.randint(0, screen_width - mr_width)
    mr_y = random.randint(0, screen_height - mr_height)
    moving_rect = pygame.Rect(mr_x, mr_y, mr_width, mr_height)
    
    # 장애물과 아이템과 충돌이 일어나지 않는 x,y 값을 설정
    if moving_rect.collidelist(obs_list) == -1 and\
        moving_rect.collidelist(item_list) == -1:
            break

while running:
    # << -- 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # -- >> 

    previous_pos = moving_rect.topleft
    
    dt = clock.tick(60) / 1000 
    
    keys = pygame.key.get_pressed()

    # 왼쪽 방향키가 눌러졌을 때
    if keys[pygame.K_LEFT]:
        moving_rect.x -= speed * dt      

    # 오른쪽 방향키가 눌러졌을 때
    if keys[pygame.K_RIGHT]:
        moving_rect.x += speed * dt 
        
    # 아래쪽 방향키가 눌러졌을 때
    if keys[pygame.K_DOWN]:
        moving_rect.y += speed * dt
    
    # 위쪽 방향키가 눌러졌을 때
    if keys[pygame.K_UP]:
        moving_rect.y -= speed * dt

    # 화면 경계처리
    moving_rect.x = max(0, min(moving_rect.x, screen.get_width() - moving_rect.width))
    moving_rect.y = max(0, min(moving_rect.y, screen.get_height() - moving_rect.height))

    # 움직이는 사각형과 장애물간에 충돌이 있을 경우, 이전 좌표 복원
    if moving_rect.collidelist(obs_list) != -1:
        moving_rect.topleft = previous_pos

    # 움직이는 사각형과 아이템간의 충돌이 있을 경우, 해당 아이템을 리스트에서 삭제
    col_item_index = moving_rect.collidelist(item_list)
    if col_item_index != -1:
        del item_list[col_item_index]
    if not item_list:
        running = False
    # <<-- 화면 그리기
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    # 장애물 그리기
    for rect in obs_list:
        pygame.draw.rect(screen, (255, 0, 0), rect) # Rect 객체 이용
    
    
    # 아이템 그리기
    for item in item_list:
        pygame.draw.rect(screen, (0,0,255), item)
    
    # 무빙 사각형 그리기
    pygame.draw.rect(screen, (0,0,0), moving_rect)
    
    pygame.display.flip()
    # -->>

pygame.quit()