import pygame
import color
import random

# 1. 스페이스키를 누르면
# 2. 총알 사각형이 생성되고
# 3. 생성된 사각형은 플레이어 사각형의 TOP라인에 중앙에 위치한다.
# 4. 매 프레임(Frame) 마다 총알의 y축 위치를 감소(즉,아래에서 위로 이동)
# 5. 만약 총알 사각형이 떨어지는 사각형과 충돌이 일어나면
#    해당 사각형과 총알을 삭제한다.
# 6. 총알이 충돌하지 않고 화면의 위쪽으로 넘어가면 해당 총알을 삭제한다.

pygame.init()

# 환경 변수
screen_width = 800
screen_height = 600
player_width = 80
player_height = 40
fire_width = 15
fire_height = 15

fall_rect_width = 80
fall_rect_height = 40
fall_rect_list = []

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# 플레이어 사각형 정의 (bottom, top등 값을 바꾸면 도형의 좌표값이 바뀐다.)
player_rect = pygame.Rect(0, 0, player_width, player_height)
player_rect.x = screen_width // 2 - player_width // 2 
player_rect.y = screen_height - player_height - 10

def generate_falling_rect():
    for _ in range(random.randint(2, 6)):
        while True:
            rect_x = random.randint(0, screen_width - fall_rect_width) # 0 <= x <= 720
            rect = pygame.Rect(rect_x, 0, fall_rect_width, fall_rect_height)
            
            # 충돌이 발생하지 않았을 경우
            if rect.collidelist(fall_rect_list) == -1:
                # 사각형을 리스트에 추가
                fall_rect_list.append(rect)
                break 
            
# 객체 이동 속도
speed = 300 # 300 pixel / second

# 사용자 정의 이벤트 생성
fire_rect_list = []
# MY_EVENT는 pygame.USEREVENT에 1을 더하여 고유한 이벤트로 정의
MY_EVENT = pygame.USEREVENT + 1

# 타이머 설정: 2초마다 MY_EVENT는 이벤트가 발생하도록 설정
pygame.time.set_timer(MY_EVENT, 2000)  # 2000밀리초(2초)마다 이벤트 발생


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 2. 총알 사각형이 생성되고
                # 3. 생성된 사각형은 플레이어 사각형의 TOP라인에 중앙에 위치한다.
                fire_rect = pygame.Rect(0, 0, fire_width, fire_height)
                fire_rect.bottom = player_rect.top
                fire_rect.x = player_rect.center[0] - fire_width // 2
                fire_rect_list.append(fire_rect)
        elif event.type == MY_EVENT:
            generate_falling_rect()
                
    dt = clock.tick(60) / 1000 # dt 프로그램 실행 멈춤    

    # 떨어지는 사각형 이동 및 충돌 체크
    for rect in fall_rect_list[:]:
        rect.y += speed * dt
        if rect.colliderect(player_rect):
            print("충돌 발생, 게임 종료")
            running = False
    
    #  총알 이동 처리
    for f_rect in fire_rect_list[:]:
        f_rect.y -= speed * dt
        if f_rect.bottom < 0:  
            fire_rect_list.remove(f_rect)
        
    # 총알과 떨어지는 사각형 충돌 체크
    for fire in fire_rect_list[:]:
        is_collision = False
        
        for fall in fall_rect_list[:]:
            if fire.colliderect(fall):
                fall_rect_list.remove(fall)
                is_collision = True
        if is_collision:
            fire_rect_list.remove(fire)
            
    keys = pygame.key.get_pressed() 
    
    # 왼쪽 방향키가 눌러졌을 때
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed * dt      

    # 오른쪽 방향키가 눌러졌을 때
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed * dt 
  
    # 화면 아래이면 리스트에서 삭제
    for rect in fall_rect_list[:]:
        if rect.y > screen_height:
            fall_rect_list.remove(rect)
    
    # 화면 경계 처리    
    player_rect.x = max(0, min(player_rect.x, screen.get_width() - player_rect.width))

 
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))
    
    # 플레이어 사각형 그리기         
    pygame.draw.rect(screen, (0, 0, 255), player_rect) 
    # 총알 사각형 그리기
    for f_rect in fire_rect_list:
        pygame.draw.rect(screen, color.green, f_rect)
    # 떨어지는 사각형
    for rect in fall_rect_list:
        pygame.draw.rect(screen, color.red, rect)
    
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    print(len(fall_rect_list))

    
pygame.quit()
