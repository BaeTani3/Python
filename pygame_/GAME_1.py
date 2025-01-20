import pygame
import color
import random
import time


# 1. initialization
## <<--- 초기화
pygame.init()

background_music = pygame.mixer.music.load("푸른산호초.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

otani_sound = pygame.mixer.Sound("오타니.mp3")
otani_sound.set_volume(1)


# <<- 환경변수
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("하니와 오타니")

num_item = 5
num_of_enemy = 5
enemy_width = 70
enemy_height = 70

image = pygame.image.load("인형.PNG")
background = pygame.image.load("hell.jpg")
newjeans = pygame.image.load("하니.png")
otani = pygame.image.load("오타니.png")
baseball = pygame.image.load("baseball.png")


baseball_width = baseball.get_size()[0] 
baseball_height = baseball.get_size()[1]

## <<-- fps 적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
## <<--- 메인 루프
speed = 10
running = True



# 적 설정
enemy_list = []
enemy_speed_list = []

for _ in range(num_of_enemy): 
    enemy = pygame.Rect(random.randint(0, screen_width - 60), 
            random.randint(0, screen_height - 60), enemy_width, enemy_width)
    
        
    enemy_speed = [random.choice([-5, 5]), random.choice([-5, 5])]
    enemy_list.append(enemy)
    enemy_speed_list.append(enemy_speed)
    

# 장애물 생성 함수
def create_obstacles(num_obstacles, size, screen_width, screen_height):
    obstacles = []
    for _ in range(num_obstacles):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size), \
                                random.randint(0, screen_height - size), size, size)
            if not any(rect.colliderect(o) for o in obstacles):
                obstacles.append(rect)
                break
    return obstacles

# 아이템 생성 함수
def create_items(num_items, size, screen_width, screen_height, obstacles):
    items = []
    for _ in range(num_items):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size),\
                                random.randint(0, screen_height - size), size, size)
            if not any(rect.colliderect(o) for o in obstacles) and \
                not any(rect.colliderect(i) for i in items):
                    items.append(rect)
                    break
    return items

# 수풀 생성 함수
def hidebush(num_bush, size, screen_width, screen_height):
    bushs = []
    for _ in range(num_bush):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size),\
                                random.randint(0, screen_height - size), size, size)
            if not any(rect.colliderect(i) for i in bushs) and \
                not any(rect.colliderect(o) for o in obstacles):
                bushs.append(rect)
                break
    return bushs
# 장애물 및 아이템 생성
obstacles = create_obstacles(30, 50, screen_width, screen_height)
items = create_items(num_item, 50, screen_width, screen_height, obstacles)
bushs = hidebush(7, 25, screen_width, screen_height)

# 이동하는 Rect 생성
m_width = m_height = 10
while True:
    # 이동하는 사각형을 랜덤 위치에 생성
    m_x, m_y = random.randint(0, screen_width - m_width), random.randint(0, screen_height - m_height)
    moving_rect = pygame.Rect(m_x, m_y, m_width, m_height)
    # 장애물 및 아이템과 겹치지 않는 위치를 찾기
    if moving_rect.collidelist(obstacles) == -1 and moving_rect.collidelist(items) == -1:
        break
# 이동 속도 설정
velocity = 300
# FPS제어를 위한 Clock객체 생성
clock = pygame.time.Clock()

# 하얀 문 위치 설정
white_door_rect = pygame.Rect(430, 85, 70, 70)

# 3초 대기 후 게임 시작
font = pygame.font.Font(None, 74)
for i in range(3, 0, -1):
    screen.fill((0, 0, 0))
    
    # 장애물 그리기
    for obs in obstacles:
        pygame.draw.rect(screen, color.blue, obs)
        
    # 아이템 그리기
    for item in items:
        screen.blit(otani,item.topleft)
        # pygame.draw.rect(screen, color.yellow, item)
        
    # 이동하는 Rect 그리기
    pygame.draw.rect(screen, color.red, moving_rect)
    start_time = pygame.time.get_ticks()
    
    # bush 그리기
    for bush in bushs:
        pygame.draw.rect(screen, color.green, bush)
    
    # # 적그리기
    for enemy in enemy_list:
        screen.blit(newjeans, enemy.topleft)

    countdown_text = font.render(str(i), True, color.white)
    screen.blit(countdown_text, (screen_width // 2, screen_height // 2))
    pygame.display.flip()
    time.sleep(1)  # 1초 대기

# 타이머 설정 (1분 = 60초)
total_time = 90
start_ticks = pygame.time.get_ticks()

# 2. Event Handling & Image creation
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.mixer_music.stop()
            elif event.key == pygame.K_p:
                pygame.mixer_music.play()
        elif event.type == pygame.MOUSEMOTION:
            x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()
            moving_rect.x = x_pos_mouse 
            moving_rect.y = y_pos_mouse
           
            
    # 이전 위치 저장
    previous_positon = moving_rect.topleft
    
    # delta time
    dt = clock.tick(60) / 1000.0

    # 키 입력 처리
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     moving_rect.x -= velocity * dt 
    # if keys[pygame.K_RIGHT]:
    #     moving_rect.x += velocity * dt
    # if keys[pygame.K_UP]:
    #     moving_rect.y -= velocity * dt
    # if keys[pygame.K_DOWN]:
    #     moving_rect.y += velocity * dt
        
    # 적의 랜덤 이동
    for i, enemy in enumerate(enemy_list):
        enemy.x += enemy_speed_list[i][0]
        enemy.y += enemy_speed_list[i][1]
        
        # 적이 화면 경계를 벗어나면 방향 변경
        if enemy.left < 0 or enemy.right > screen_width:
            enemy_speed_list[i][0] = -enemy_speed_list[i][0]
        if enemy.top < 0 or enemy.bottom > screen_height:
            enemy_speed_list[i][1] = -enemy_speed_list[i][1]
         
        # 적과 플레이어 충돌 감지
        if moving_rect.colliderect(enemy):
            bush_collision_index = enemy.collidelist(bushs)
            if bush_collision_index != -1:
                running = True
            else:
                print("You lose!")
                running = False

    # 충돌 감지
    collision_index = moving_rect.collidelist(obstacles)
    if collision_index != -1:
        # 충돌 시 위치 복원
        print(f"장애물 {collision_index}와 충돌! 위치 복원.")
        moving_rect.topleft = previous_positon
        
    # 아이템 수집
    item_index = moving_rect.collidelist(items)
    if item_index != -1:
        otani_sound.play()
        moving_rect.width += 5
        moving_rect.height += 5
        # 아이템 수집 후 제거
        print(f"아이템 수집! 남은 아이템: {len(items)-1}")
        del items[item_index]
    
    # 모든 아이템 수집 시 게임 종료
    if not items and moving_rect.colliderect(white_door_rect):
        print("모든 아이템을 수집했습니다! 승리!")
        running = False
        
    # 타이머 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    remaining_time = max(0, total_time - elapsed_time)
    
    # 남은 시간이 0이면 게임 종료
    if remaining_time <= 0:
        print("시간 초과! 실패!")
        running = False    
    
    screen.blit(background, (0,0))
    
    # 장애물 그리기
    for obs in obstacles:
        pygame.draw.rect(screen, color.blue, obs)
    # 아이템 그리기
    for item in items:
        screen.blit(otani,item.topleft)
        # pygame.draw.rect(screen, color.yellow, item)
    
    # 이동하는 Rect 그리기

    pygame.draw.rect(screen, color.red, moving_rect)
    start_time = pygame.time.get_ticks()
    
    # bush 그리기
    for bush in bushs:
        pygame.draw.rect(screen, color.green, bush)
    
    # # 적그리기
    for enemy in enemy_list:
        screen.blit(newjeans, enemy.topleft)
    
    
    # 경계선
    moving_rect.x = max(0, min(moving_rect.x, screen.get_width() - moving_rect.width))
    moving_rect.y = max(0, min(moving_rect.y, screen.get_height() - moving_rect.height))
    
    # 타이머 화면에 표시
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Time: {int(remaining_time)}", True, color.white)
    screen.blit(timer_text, (10, 10))
    
    pygame.display.flip()

# 3. Termination
pygame.quit()