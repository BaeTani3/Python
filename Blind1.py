
import random

Eng_list = []

for index in range(3):
    while True:
        input_value = input("단어를 입력하세요: ")
        
        if 5 <= len(input_value) <= 20:
            Eng_list.append(input_value)
            break
        
        print("5이상 20이하 글자의 단어 입력")
        
word_selected = list(Eng_list[random.randint(0, 2)]) # 대입을 하기 위해 list로 변환
   
    # 화면         정답
word_printed = word_selected[:] 
# 참조변수의 주소값만 복사하는 것이 아닌
# 이렇게 하면 리스트의 COPY와 같다.

# 선택된 단어의 글자 수
char_num_word = len(word_selected)

# 선택된 단어의 글자 수의 50%를 블라인드 처리
blind_num_word = char_num_word / 2
# 올림 처리 알고리즘
if blind_num_word > char_num_word // 2:
    blind_num_word += 1
# 정수로 변환
blind_num_word = int(blind_num_word)


list_blind_index = [value for value in range(0, char_num_word)]

for index in range(0, char_num_word - blind_num_word): # 블라인드 안 할 알파벳을 빼준다
    del list_blind_index[random.randint(0, len(list_blind_index) -1)]
    
for index in list_blind_index :
    word_printed[index] = "_"



while len(list_blind_index) > 0 :
    print("printed word: ", word_printed)
    
    input_value = input("글자를 입력하세요: ")
    
    found_index_list = []
    
    for index in list_blind_index:
        if word_selected[index] == input_value:
            word_printed[index] = input_value
            found_index_list.append(index)
    
    for f_index in list_blind_index:
        list_blind_index.remove(f_index)
    
print(word_printed)