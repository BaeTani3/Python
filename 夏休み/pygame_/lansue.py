import pygame

## <<--- 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))

## <<-- fps 적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
fps = 60
## -->>
x = screen.get_width()/2
y = screen.get_height()/2
speed = 100 # pixel/second => 1초에 10픽셀
radius = 40 

## <<--- 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    
    dt = clock.tick(fps)/1000.0 # tick이 ms으로 갖고오기에 1000.0ms으로 나누면 sec으로 가져온다.
    x += (speed * dt)
    print(dt)
    
    pygame.draw.circle(screen, (255,0,0), (x,y), radius)
   
    pygame.display.update()
    # ## <<-- pygame fps 설정
    clock.tick(fps)
    ## -->>
## -->> 이미지 생성

## 게임 종료
pygame.quit()
