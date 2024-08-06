# 자료구조 맵 딕셔너리
# 데이터를 어떻게 보관할것인가에 대한 학문
# 자료구조는 언어와 상관없이 공통된 학문이다.

# 딕셔너리
# 알고리즘과 데이터

import random


dice_list = [0, 0, 0, 0, 0, 0]
N = 100
for _ in range(N):
    dice_list [random.randint(1, 6) - 1] += 1

print(dice_list)

#1 primitive types - 자료 구조론에서 논의 되지 않음
#2 composite types -> primitive 가 2개이상 어떤식으로 묶을 것인가(파이썬은 X)
#3 Abstract Data types -> composite을 기반으로 알고리즘을 추가

# array, Linked list를 composite에서 배우지만(석학들이) 우리는 배우지 않고,
# 실무에 사용하는 3번을 배운다. 
# stack에서 LIFO 처럼 +알고리즘을 추가하여 보관하는 방법 => 3

# Collection 컬렉션 
# 이론, 방법인 자료구조를 프로그래밍 언어로 구현해 놓은 것들
# ex) java의 Collection framework 자바에서 자료구조를 구현해놓은 것
# 파이썬에서 제공하는 내장 컬렉션 list, tuple, dictionary, set ... 총칭

# list and tuple
# Mutable - Immutable 컬렉션 안에 원소들을 변경할수 있나 없나
# sequential - 내가 원하는대로 데이터를 유지할 수 있다.

# set : unique ,set은 집합, 중복값이 있을 수 없다 
# 중복값을 지우고 싶을 때 사용한다.  
# foo = set()
# for _ in range(5):
#     foo.add(input("값: "))
# print(foo)

# Dictionary : key-value 인덱스 - 데이터  map
# 순회 - 각 원소를 처음부터 끝까지 접근하여 처리하는 과정
# 리스트는 데이터의 갯수가 늘어날 수록 확률적으로 탐색 시간이 길어지지만,
# Dictionary는 탐색이 필요없다.
# hash function에 의해 key값을 집어 넣으면 value 값이 나온다.
# key값은 unique 해야한다. 
bar = { "name" : "ycjung", "age" : 20, }

print(bar["name"])

# 파워풀한 추가 방법
bar["email"] = "bae3305@"

## 딕셔너리의 사용 적절성
# 데이터 검색 및 접근이 빈번할 때
# 데이터의 고유성이 중요할 때
# 데이터를 구조화하여 저장할 때

if "email" in bar:
    print("True")
else:
    print("False")
    
# keys() : 키 값
# values() : 데이터 값
# items() : (키 + 데이터)

# 객체 구조화
# dictionary에서 계층은 층의 개수를 의미한다
foo = {"삼성" : {"선수" : {"강민호" : {"성격" : "차분"}, "강민호" : {"능력(컨택, 파워, 주루)" : [60, 60, 70]}}}, "마스코트 점수" : {"호랭이" : 30, "백호" : 20}}

print(foo["삼성"]["선수"]["강민호"]["능력(컨택, 파워, 주루)"][1])

# 딕셔너리 + 리스트
std_grades = {}

std_grades[10] = ["홍길동", 10, 20, 30, 60, 30]
std_grades["안녕"] = ["사", 10, 20, "33"]
print(std_grades)
foo = [ value for i in range(2) for value in range(3)]
print(foo)
bar = print(" s a m e")
print(bar)