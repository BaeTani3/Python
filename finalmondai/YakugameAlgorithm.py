
# 중복되지 않은 1~10사이 정수 3개 생성
# in, not in, list 내 중복되지 않은 랜덤 정수 생성 함수 사용금지

import random

# 리스트 생성

com_list = list()

count = 0


# 반복문 작성
def getRandValue():
    while count < 3 :
        rand_value = random.randint(1, 10)
        found_duplicated_value = False
        
        for sub_count in range(count):
            # 중복 값이 있을 경우
            if rand_value == com_list[sub_count]:
                found_duplicated_value = True
                break
            
        if not found_duplicated_value: # not은 역접
            com_list.append(rand_value)
            count += 1
            
    print(com_list)
            
    

count_game_trial = 0
count_strike_out = 0
count_strike = 0

count_list = getRandValue()





# 중복되지 않은 1~10사이 정수 3개 생성
# in, not in, list 내 중복되지 않은 랜덤 정수 생성 함수 사용금지

# 3 7 4 : computer
# 2 3 4 : user
# result : 1 strike, 1 ball

import random


def getRandValue():
    rand_list = list()

    count = 0

    while count < 3:
        rand_value = random.randint(1, 10)
        found_duplicated_value = False
        
        for sub_count in range(count):
            # 중복 값이 있을 경우
            if rand_value == rand_list[sub_count]:
                found_duplicated_value = True
                break
        
        if not found_duplicated_value:
            rand_list.append(rand_value)
            count += 1
            
    return rand_list


com_list = getRandValue()
print(com_list)
