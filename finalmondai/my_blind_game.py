
# 영어 단어입력 (5이상, 20이하) 
# 유효 범위 벗어나면 재입력 요구

import random

English_word = []

for _ in range(3):
    
    while True:
        word = input("사용자 입력")
        if 5 <= len(word) <= 20 :
            English_word.append(word)
            break
        
        print("5이상 20이하")
        # ["aaaaaii" , "bbbcc", "dddeee"]


# 단어 선택 3개의 단어 중 임의 선택
selected_word = [ char for char in English_word[random.randint(0, 2)]]

# 프린트하여 출력할 리스트 생성
# 리스트 복사
printed_word = selected_word[:]
printed_word_length = len(printed_word)

# blind 처리할 단어 개수
# 홀수 단어일 경우 if문 써서 올림하기
blind_length = printed_word_length / 2 
if blind_length > printed_word_length // 2 :
    blind_length += 1
# 정수로 변환
blind_length = int(blind_length)

# 선택된 단어의 글자 중 50% 랜덤하게 Blind 처리

# 랜덤하게 Blind 처리하기 위해 인덱스 값의 리스트 생성
index_list = [ value for value in range(printed_word_length)]
print(index_list)
# Blind 하지 않을 단어를 랜덤하게 뺀다.
for char in range(printed_word_length - blind_length):
    
    del index_list[random.randint(0, len(index_list) - 1)]
print(index_list)
# Blind _ 변환
for i in index_list:
    printed_word[i] = "_"
print(printed_word)

# 게임 시작
# 알파벳 입력  while

while True :
    
    input_value = input("단어를 입력하세요: ")
    print("printed_word",printed_word)
    # 입력받은 알파벳이 단어 내 존재할 경우 blind 해제
    for index in index_list:
        if selected_word[index] == input_value:
            printed_word[index] = input_value
        
    
        # 존재하지 않을 경우 "없음" 메세지 출력
    if input_value != selected_word[index] :
        print("없음")
    
  
    # 모든 글자를 맞출 경우 게임 종료
    if printed_word == selected_word :
        print("게임 종료")
        break 
    
# 결과출력
print(selected_word)