import random
import math

# 영어 단어 3개를 입력 받아 리스트에 저장
# 단어의 글자 범위는 5이상, 20이하
word_list = ["aaaabbb", "bbbccc", "iieoo"]

# 단어 임의 선택
word_selected = list(random.choice(word_list))
word_printed = word_selected[:]

# 디버깅용 출력 (필요할 때만 활성화)
# print("Selected word (for debugging):", ''.join(word_selected))

# 선택된 단어의 글자 중 50% blind처리
# 홀수이면 올림하여 처리
blind_word_count = math.ceil(len(word_selected) / 2)
print(blind_word_count)

# 블라인드할 인덱스를 무작위로 선택
blind_index = random.sample(range(len(word_selected)), blind_word_count)

# 블라인드 처리
for index in blind_index:
    word_printed[index] = "_"

user_monitor = ''.join(word_printed) # 문자열을 결합하는 join메서드

# 게임시작-------------------
count = 1
while True:
    # 키보드로부터 알파벳 한 글자 입력
    print(user_monitor)
    user_input = input(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.")
    
    # 입력받은 알파벳이 단어 내에 존재할 경우 블라인드 해제
    if user_input in word_selected:
        for index in range(len(word_selected)):
            if word_selected[index] ==  user_input:
                word_printed[index] = user_input
    else:# 존재하지 않을 경우 "없음" 메세지 출력
        print("없음")
        
    # 업데이트된 단어 상태 출력
    user_monitor = ''.join(word_printed) 
    count += 1
    
    # 모든 글자를 맞출 경우 게임이 종료
    if '_' not in word_printed:
        print("Clear")
        print(f"총 시도 횟수: {count}")
        break