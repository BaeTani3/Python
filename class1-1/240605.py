# 문법이 없으면 그리질 못하고, 있어도 연습이 없으면 막힌다.



for k in range(1, 5):
    for i in range(1, 3):
        for j in range(1, 4):
            if i == 2:
                break
            print(i, ":", j) 
    # 중첩 반복문은 밑에서 부터 봐라
    # 즉, j가 i번 돈다.  (i가 아니라)
    
# 연습 1
# 아래 라인부터 반복문(가로)을 만들고 위 라인 반복문(세로)을 만든다.
for i in range(4):
    for j in range(3):
        print("*", end = '')
    
    if i != 3:
        print("")

print()

# 3x3x3 다차원 리스트 생성
cube = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]

# 3차원 cube 리스트 출력
for layer in cube :
    for row in layer :
        print(row)
    print()
    

print(cube)

for i in range(3):
    for j in range(3):
        for k in range(3):
            cube[i][j][k] = i + j + k

for layer in cube:
    for row in layer:
        for element in row:
            print(element, end=' ')
        print()
    print()


# break 동작 절차
# 1) 위로 올라간다
# 2) 첫 번째 만나는 반복을 종료

# continue 동작 절차 
# 1) 위로 올라간다
# 2) 다음 반복을 실행한다.

# 중첩 반복문은 곱하기다. 2 X 3 =? 3을 2번 더한다
for k in range(1, 5):
    if k == 2:
        continue
    for i in range(1, 3):
        for j in range(1, 4):
            if j == 2:
                continue
            print(i, ":", j)
            
# pass 흐름제어문, 함수, 클래스

value = 3

if value > 3:
    # 메뉴를 출력하라 -> 추후 구현해야됨.
    pass

def sum(a, b, c):
    # 3개의 값을 더한 후 반환
    # 추후 구현
    pass

count = 2

random.randint(1,3)  # ctrl + .
