# Event-Driven Programming의 구성요소 3가지
# While 무한루프
# Event-handler -> 함수 또는 매서드와 매칭이된다.
# Event_listener -> 

import pygame

# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption("Event Listener and Handler Example")
# running = True

# # 이벤트 핸들링 : 함수 사용
# def handle_keydown(event):
#     if event.key == pygame.K_SPACE:
#         print("Spacebar pressed - handled by function.")
        
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             # 키보드의 키를 누르면 발생하는 이벤트
#             # 눌린 키의 이름을 출력
#             print(f"Key pressed: {pygame.key.name(event.key)}")
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # 마우스 버튼을 클릭하면 발생하는 이벤트
#             # 클릭된 위치와 버튼 번호를 출력
#             print(f"Mouse button {event.button} clicked at positon {event.pos}")
            
# pygame.quit()


pygame.init()

screen = pygame.display.set_mode((640, 480))

running = True

while running: # 한 번 돌 때 마다 그림 한 장이 나온다.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            print(f"key pressed: {pygame.key.name(event.key)}")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse button {event.button} cliked at position {event.pos}")
pygame.quit()

