
# # 중복되지 않은 난수 값 3개 생성

# import random

# count = 0
# rand_list = []

# while count < 3 :
#     rand_value = random.randint(0, 9)
    
#     for index in range(count):
#         if rand_list[index] == rand_value :
#             break
#     else :
#         rand_list.append(rand_value)
#         count += 1

# count_trial = 0
# count_strike_out = 0 # 루프가 돌 때 마다 매번 초기화 되지 않기 위해서

# while True :
#     count_strike = 0
#     count_ball = 0
    
#     # 사용자로 부터 정수 3개 입력
#     input_values = input()
    
#     input_list = [int(value) for value in input_values.split()]

#     print(input_list)
    
#     # strike, ball 판별
#     for i in range(3):
#         for j in range(3):
#             if rand_list[i] == input_list[j]:
#                 if i == j :
#                     count_strike += 1
#                 else :
#                     count_ball += 1
#     print(f"스트라이크 : {count_strike}, 볼 : {count_ball}")
#     # strike out 판별
#     if count_strike == 0 and count_ball == 0:
#         count_strike_out += 1
#         print(f"스트라이크 아웃: {count_strike_out}")
        
#     # 게임종료 조건
#     # strike 3개
#     if count_strike >= 3:
#         print(f"사용자 승리!")
#         break
    
#     # strike out 2번
#     # 시도 횟수 5번 이상
#     if count_strike_out >= 2 or count_trial >= 5:
#         print(f"사용자 패배")
#         break
    
#     count_trial += 1

#------------------------------------------------------------

# # 중복되지 않은 난수 값 3개 생성 (0 ~ 9)
# import random

# count = 0

# # 랜덤 값 리스트
# random_list = []

# # 랜덤 값 생성
# while count < 3 :
#     randvalue = random.randint(0,9)
    
#     # 중복 값 검사
    
#     for num in random_list:
#         if num == randvalue:
#             break
        
#     else :
#         random_list.append(randvalue)
#         count += 1
       
        
# print(random_list)
        
        


# game_count = 0
# count_strie_out = 0

# while True :
#     strike_count = 0
#     ball_count = 0
    
#     # 사용자로 부터 정수 3개 입력
#     user_num = input()
    
#     user_list = [ int(value) for value in user_num.split() ]
    
#     print(f"시도 {game_count + 1}: 입력한 숫자 - {user_list}")
    
#     # strike, ball 판별
#     # strike out 판별
#     for i in range(3):
#         for j in range(3):
#             if random_list[i] == user_list[j]:
#                 if i == j :
#                     strike_count += 1
#                 else :
#                     ball_count += 1
            
#     print(f"결과: {strike_count} strike, {ball_count} ball")

#     game_count += 1
#     # strike out 판별
#     if strike_count == 0 and ball_count == 0:
#         count_strie_out += 1
#         print(f"{count_strie_out} out")

# # 게임종료 조건

# # strike 3개 (승리조건)
#     if strike_count >= 3 :
#         print(f"결과: 승리\n정답: {random_list}")
#         break
# # strike out 2번 (패배조건 1)
#     if count_strie_out >= 2 :
#         print(f"게임 종료 : 패배 아웃 2개\n정답: {random_list} ")
#         break
# # 시도 횟수 5번 이상 (패배조건 2)
#     if game_count >= 5 :
#         print(f"게임 종료 : 시도 횟수 5회 초과\n정답: {random_list}  ")
#         break
    
    
###################GPT
import random

# 중복되지 않은 난수 값 3개 생성 (0 ~ 9)
def generate_unique_randoms(count, start, end):
    random_list = []
    while len(random_list) < count:
        randvalue = random.randint(start, end)
        if randvalue not in random_list:
            random_list.append(randvalue)
    return random_list

random_list = generate_unique_randoms(3, 0, 9)
print(f"랜덤 숫자: {random_list}")

game_count = 0
count_strike_out = 0

def check_game_end(strike_count, ball_count, game_count, count_strike_out, random_list):
    if strike_count >= 3:
        print(f"결과: 승리\n정답: {random_list}")
        return True
    if count_strike_out >= 2:
        print(f"게임 종료 : 패배 아웃 2개\n정답: {random_list}")
        return True
    if game_count >= 5:
        print(f"게임 종료 : 시도 횟수 5회 초과\n정답: {random_list}")
        return True
    return False

while True:
    strike_count = 0
    ball_count = 0
    
    # 사용자로부터 정수 3개 입력
    user_num = input("정수 3개를 입력하세요 (예: 1 2 3): ")
    user_list = [int(value) for value in user_num.split()]
    
    if len(user_list) != 3:
        print("정확히 3개의 숫자를 입력해주세요.")
        continue
    
    print(f"시도 {game_count + 1}: 입력한 숫자 - {user_list}")
    
    # strike, ball 판별
    for i in range(3):
        if random_list[i] == user_list[i]:
            strike_count += 1
        elif user_list[i] in random_list:
            ball_count += 1
            
    print(f"결과: {strike_count} strike, {ball_count} ball")

    game_count += 1
    
    # strike out 판별
    if strike_count == 0 and ball_count == 0:
        count_strike_out += 1
        print(f"{count_strike_out} out")
    
    # 게임 종료 조건 확인
    if check_game_end(strike_count, ball_count, game_count, count_strike_out, random_list):
        break