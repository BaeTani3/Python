
import random

def getRandList(argNumRandValues, argStartValue, argEndValue):

# 리스트 생성
    computer_list = []

    # 랜덤 값 카운트 3개 미만
    random_count = 0

    while random_count < argNumRandValues:
        
        # 랜덤 값 생성
        rand_value = random.randint(argStartValue, argEndValue)
        
        # 중복 값 확인
        found_dup_value = False
        
        for index in range(random_count):
            if computer_list[index] == rand_value:
                found_dup_value = True
                break
        
        if not found_dup_value:
            computer_list.append(rand_value)
            random_count += 1
        
    return computer_list

com_random_list = getRandList(3, 0 ,9)

print("컴퓨터 랜덤 값: ", com_random_list)

count_game_trial = 0
count_strike_out = 0

while True : 
    count_strike = 0
    count_ball = 0
    
    # 사용자 입력
    print("사용자 입력 : ")
    user_input = [int(input()) for _ in range(3)]
    
    # strike, ball 판정
    for i in range(3):
        for j in range(3):
            if com_random_list[i] == user_input[j]:
                if i == j:
                    count_strike += 1
                else :
                    count_ball += 1
                
                break
    count_game_trial += 1
    
    # strike out 
    if count_strike == 0 and count_ball == 0 :
        count_strike_out += 1
        print("스트라이크 아웃")
    else:
        print("strike: ", count_strike, "\tBall: ", count_ball)
        
    # 종료 조건
    # 1) Lose
    # -시도 회수 5번 이상, 스트라이크 아웃 2번 이상
    if count_strike_out >= 2 or count_game_trial >= 5:
        msg = "5회 이상 실행" if count_game_trial >= 5 else "스트라이크 아웃 2회 이상"
        print(msg, "\t 게임 종료")
        break
    
    # 2) Win
    # strike 3개
    if count_strike >= 3 :
        print("승리\t게임 종료")
        break