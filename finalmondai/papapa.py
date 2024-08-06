
import random

# 단어 입력

word_list = ["aabbe", "kkoouu", "qqeerri"]

# 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장합니다.

# 단어의 글자 범위는 5 이상, 20 이하로 제한됩니다.
# 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구합니다.


# 단어 선택
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택합니다.
rand_word = word_list[random.randint(0, 2)]
rand_word = list(rand_word)

print(rand_word)

# 게임 시작
# 선택된 단어의 길이 절반 구하기
rand_word_length = len(rand_word)
rand_word_half = rand_word_length / 2

# 만약 절반의 길이가 몫 보다 크면 + 0.5
if rand_word_half > rand_word_length // 2:
    rand_word_half += 0.5
rand_word_half = int(rand_word_half)
print(rand_word_half)

# 선택된 단어의 index값 리스트
index_list = [ value for value in range(rand_word_length)]
print(index_list)

# index리스트에서 절반 값을 뺀 나머지를 구한다
for i in range(rand_word_length - rand_word_half):
    del index_list[random.randint(0, rand_word_half)]
print(index_list)

# 출력용 리스트 생성
word_printed = rand_word[:]

# 선택된 단어의 글자 중 50%를 Blind 처리합니다.
for index in index_list:
    word_printed[index] = "-"

print(word_printed)


# 시도 count
count = 1

# 모든 단어를 채울 때 까지 진행되어야 하니 while문
while True :

    # 알파벳 입력
    # 키보드로부터 알파벳 한 글자를 입력받습니다.
    user_input = input(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n")
    count += 1 
    # Blind 해제
    # 입력받은 알파벳이 단어 내에 존재할 경우 Blind를 해제합니다.
    if user_input in rand_word :
        for index in index_list:
            if user_input == rand_word[index]:
                word_printed[index] = user_input
        print(word_printed)
     # 존재하지 않을 경우 “없음” 메시지를 출력합니다
    else :
        print(word_printed)
        print("단어 내 포함되지 않은 알파벳입니다.")
   
    
    
    # 게임 종료
    # 단어의 모든 글자를 맞출 경우 게임이 종료됩니다
    if word_printed == rand_word :
        print(f"Clear - 선택된 단어: {rand_word}, 총 시도 횟수: {count - 1}")
        break
    # 결과 출력
    # 게임 종료 시 시도 횟수를 출력합니다