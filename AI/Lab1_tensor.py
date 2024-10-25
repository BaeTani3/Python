
import random
# 범위 내의 난수 리스트 생성
# 사용자로부터 start, End, N의 세 값을 입력 받는다

while True :
    # Start 난수의 시작 범위 (0이상, End보다 작아야 함)
    while True:
        Start = int(input("난수를 생성할 범위와 개수를 입력하세요\nstart (0 이상의 정수): "))
        if Start > 0 :
            break
    # End 난수의 끝 범위 (Start 보다 커야 함)
    while True:
        End = int(input("End (Start보다 큰 정수): "))
        if End > Start:
            break
        print(f"End는 Start({Start})보다 커야 합니다.")
    # N 생성할 난수의 수 start와 End 사이 최대 수 이하
    while True :
        N = int(input("N (생성할 난수의 개수):"))
        if Start <= N < End:
            break
        print(f"N은 {Start}부터 {End}사이의 정수여야 합니다.")
    break

# 리스트 생성
Number_list = []

# 생성할 난수의 수를 초과 할 때 까지 while문
while len(Number_list) < N:
    rand_value = random.randint(Start, End - 1)
    # 중복 값 검사
    for num in Number_list:
        if rand_value == num:
            break
    else :
        Number_list.append(rand_value)

print(Number_list)