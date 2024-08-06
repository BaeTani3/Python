'''import random

def getRandList(argNumRandValues, argStartValue, argEndValue):
    # 컴퓨터가 생성한 랜덤 값을 저정하기 위한 리스트
    # 1 - 10 사이 유일한 값 3개를 생성 후 저장
    random_list = []

    # 현재 생성된 랜덤 값의 개수 : 0 -> 2
    rand_trial_count = 0

    # 랜덤 값 3개를 생성하기 위해 while문 사용
    while rand_trial_count < argNumRandValues:
        
        # 랜덤 값 생성
        rand_value = random.randint(argStartValue, argEndValue)
        
        # 중복 값 확인을 위한 플래그 변수
        found_dup_value = False
        
        # 중복값 검사를 위한 반복문 : 반복회수 현재 N번째 -> N-1
        for index in range(rand_trial_count):
            if random_list[index] == rand_value:
                found_dup_value = True
                break
            
        # 생성된 랜덤 값이 중복되지 않을 경우
        if not found_dup_value:
            random_list.append(rand_value) # 리스트에 랜덤 값을 추가
            rand_trial_count += 1 # 다음 랜덤 값 생성 실행
            
    return random_list
            
com_random_list = getRandList(3, 0, 9)

print("컴퓨터 랜덤 값: ", com_random_list)

count_game_trial = 0
count_strike_out = 0

while True:
    count_strike = 0
    count_ball = 0
    
    # 사용자 입력
    print("사용자 입력 : ")
    user_input = [int(input()) for _ in range(3)]
    
    # strkie, ball 판정
    for i in range(3):
        for j in range(3):
            if com_random_list[i] == user_input[j]:
                if i == j:
                    count_strike += 1
                else:
                    count_ball += 1
                
                break
    count_game_trial += 1  
          
    # 스트라이크 아웃
    if count_strike == 0 and count_ball == 0:
        count_strike_out += 1
        print("스트라이크 아웃")
    else:
        print("Strike: ", count_strike, "\tBall: ", count_ball)
        
    # 종료 조건
    # 1) Lose
    #   - 시도 회수 5번 이상
    #   - 스트라이크 아웃 2번 이상
    if count_game_trial >= 5 or count_strike_out >= 2:
        msg = "5회 이상 실행" if count_game_trial >= 5 else "스트라이크 아웃 2회 이상"
        print(msg, "\t 게임 종료")
        break
    
    # 2) Win
    #   - strike 3개
    if count_strike >= 3:
        print("승리\t게임 종료")
        break'''


#############################2회차#####################################

# 컴퓨터의 랜덤 숫자 생성
# 0~9 사이의 중복되지 않는 정수 3개를 생성합니다.
import random

# 리스트 생성
rand_list = []
count = 0 

while count < 3 :
    rand_value = random.randint(0, 9)
    
    for i in range(count):
        # 중복 값 있을 시
        if rand_list[i] == rand_value:
            break
    # 중복 값 없을 시
    else : 
        rand_list.append(rand_value)
        count += 1
        
print(rand_list)

# 플레이어 입력
# 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력합니다.

game_trial = 0
strike_out_count = 0

while True:
    strike_count = 0
    ball_count = 0
    
    user_input = input()
    user_input = [ int(value) for value in user_input.split() ]
    
    for i in range(3):
        for j in range(3):
            if rand_list[i] == user_input[j]:
                if i == j:
                    strike_count += 1
                else :
                    ball_count += 1
    print(f"스트라이크 : {strike_count} 볼 {ball_count}")
    
    if strike_count == 0 and ball_count == 0 :
        strike_out_count += 1
    
    game_trial += 1
    
# 게임 패배 조건
# 시도 횟수가 5번 이상일 경우. 스트라이크 아웃(Strike out) 횟수가 2번
    if game_trial >= 5 or strike_out_count >= 2:
        print("게임 패배")
        break

# 게임 승리 조건 스트라이크 3개
    if strike_count >= 3:
        print("게임 승리")
        break