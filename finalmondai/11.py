import random


# 단어 입력 받기
Eng_list = []

for index in range(3):
    while True :
        input_value = input("단어를 입력하세요: ")
        
        if 5 <= len(input_value) <= 20:
            Eng_list.append(input_value)
            break
        
        print("5이상 20이하 글자의 단어 입력")
 
 # 랜덤 단어 선택 및 초기 설정       
word_selected = list(Eng_list[random.randint(0, 2)])

    # 화면         # 정답
word_printed = word_selected[:] # 리스트 Copy

# 블라인드 처리할 문자 수 계산
char_num_word = len(word_selected)
blind_num_word = (char_num_word + 1) // 2

# 블라인드 처리할 인덱스 결정
list_blind_index = [ value for value in range(0, char_num_word)]

for index in range(0, char_num_word - blind_num_word):
    del list_blind_index[random.randint(0, len(list_blind_index) - 1)]
    
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
            
    for f_index in found_index_list:
        list_blind_index.remove(f_index)
        
print(word_printed)



