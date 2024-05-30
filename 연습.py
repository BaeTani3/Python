import random
import turtle

# 화면을 설정합니다.
screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")

width = screen.window_width() // 2
height = screen.window_height() // 2 

print("윈도우 가로 x 세로", width, height)
# 거북이를 생성
t = turtle.Turtle()

def move_forward():
    t.forward(100)
    x, y = t.position()
    if x >= width or x <= -width or y >= height or y <= -height:
        t.right(180)
    # x, y = t.position()
    
    # if x >= width or x <= -width or y >= height or y <= -height:
    #     t.right(180)
    #     t.backward(50)

def move_backward():
    t.backward(100)
    
def turn_left():
    t.left(90)

def turn_right():
    t.right(90)
    
def change_color_to_black():
    t.pencolor("black")

def change_color_to_red():
    t.pencolor("red")


def inverse_color():
    current_color = t.pencolor()
    if current_color == "red":
        t.pencolor("black")
    elif current_color == "black":
        t.pencolor("red")
    
# 펜 색깔 변경 함수를 정의
def move_random():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.pencolor(random.choice(colors))
    
# def change_color():
    
#     print("색깔 선택\n1.파란색\n2.검정색\n3.노란색")
#     while True:
#         input_value = int(input("숫자 입력: "))
        
#         if 1 <= input_value <= 3:
#             # 중첩 if문 (and 조건 성립)
#             if input_value == 1:
#                 t.pencolor("blue")
#             elif input_value == 2:
#                 t.pencolor("black")
#             elif input_value == 3:
#                 t.pencolor("yellow")

#         break
           
#     # 좀 더 나이스한 방법
#     while not (1 <= input_value <= 3):
#         input_value = int(input("숫자 입력: "))
        
#     if input_value == 1:
#         t.pencolor("blue")
#     elif input_value == 2:
#         t.pencolor("black")
#     elif input_value == 3:
#         t.pencolor("yellow")

        
# print(change_color())         

# 키보드 이벤트를 설정
screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_random, "c")
screen.onkey(change_color_to_black, "b")
screen.onkey(change_color_to_red, "r")
screen.onkey(inverse_color, "i")


screen.mainloop()

