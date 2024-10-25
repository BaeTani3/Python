value = 3

# 조건식의 결과 값의 자료형(Data type) => Boolean
if value == 2:
    print("A")
    print("B")
    print("C")
 # 문법은 매우 중요하다. 1칸이든 3칸이든 같은 그룹은 줄 맞춘다. 
if (value == 3):
 print("A")
 print("B")
 print("C") 
 
#########################################################

model = input("자동차 모델을 입력: ")

list_bmw = ["M1", "M2", "M3", "M4", "M5", "M8", "M9", "M7"]
list_tesla = ["Y", "X"]
list_lexus = ["ES", "LS"]
list_genesis = ["G80", "G90"]

maker = "" # maker = "알 수 없는 모델입니다." 1번째 방법

for model_in_list in list_bmw:
    if model == model_in_list:
        maker = "BMW"
        break
if maker == "":
    for model_in_list in list_genesis:
        if model == model_in_list:
            maker = "Tesla"
            break
for model_in_list in list_lexus:
    if model == model_in_list:
        maker = "Lexus"
        break
for model_in_list in list_genesis:
    if model == model_in_list:
        maker = "Hyundai"
        break

maker = maker if maker != "" else "알 수 없는 모델입니다."   # 2번째 방법 삼항연산자
print(maker) 


# 주석이 없다면 가능한 붙여서 써라 coding style
if model in list_bmw[:]:
    maker = "BMW"
elif model in list_tesla[:]:
    maker = "Tesla"
elif model in list_lexus[:]:
    maker = "Lexus"
elif model in list_genesis[:]:
    maker = "Hyundai"
else :
    maker = "알수 없는 모델 입니다.

###############################################################

model = input("자동차 모델을 입력: ")

list_bmw = ["M1", "M2", "M3", "M4", "M5", "M8", "M9", "M7"]
list_tesla = ["Y", "X"]
list_lexus = ["ES", "LS"]
list_genesis = ["G80", "G90"]

maker = ""

list_model = [list_bmw, list_tesla, list_lexus, list_genesis]

maker_name_list = ["bmw", "tesla", "lexus", "genesis"] # 메이커를 맵핑 할 리스트를 하나 더 만들어준다.
index_count = 0

# 리스트가 2차원으로 구성된다. list_model[1] => list_tesla
# 세로 반복 (회사 목록)
for maker_list in list_model :
    # 가로 반복 (회사별 자동차 모델) -> 반복 회수는 회사 마다 다름
    for model_in_list in maker_list:
        if model == model_in_list:
            # 해당 모델을 선택
            maker = maker_name_list[index_count]
            break
        index_count += 1
    if maker != "" :
        break