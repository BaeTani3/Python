import random
import math

# 1
# print("          r'\"7")
# print("r'-_    ,'  /")
# print(" \\.  \". L_r'")
# print("   '~\\/")
# print("      |")
# print("      |")

# 2
# # 킹, 퀸, 룩, 비숍, 폰(기본 값)
# default = [1, 1, 2, 2, 2, 8]

# # 사용자 값
# user = input().split()
# user = [ int(value) for value in user ]
# # or 
# # user = list(map(int, input().split()))

# # - 출력
# # for num in range(6):
#    # print(default[num] - user[num], end=" ")
# # or
# result = [ default - user for default, user in zip(default, user)]
# print(type(result))
# print(' '.join(map(str, result)))

# 3 별찍기
   
# N = 5
# for i in range(1, N + 1):
#    print(' ' * (N - i) + '*' * (2 * i - 1))
# for i in range(N - 1, 0, -1):
#    print(' ' * (N - i)  + '*' * (2 * i - 1) )
   
# 4 팰린드롬인지 확인

# word = input().strip()

# if word == word[::-1]:
#    print(1)
# else:
#    print(0)
   
# word = list(str(input()))

# if word == list(reversed(word)):
#    print(1)
# else:
#    print(0)

# 5 가장 많이 사용된 알파벳 대문자로 출력 
# 1. 
# word = input().strip().upper() # 양쪽 공백을 제거하고 대문자로 저장
# frequency = {} # 빈 딕셔너리 생성

# # 문자열의 각 문자에 대해 빈도수 계산
# for char in word:
#    if char in frequency:
#       frequency[char] += 1
#    else:
#       frequency[char] = 1
      
# # 가장 많이 사용된 문자를 찾기
# # 변수 초기화
# max_count = 0
# max_char = ''
# mutiple_max = False

# for char, count in frequency.items():
#    if count > max_count:
#       max_count = count 
#       max_char = char
#       mutiple_max = False
#    elif count == max_count:
#       mutiple_max = True
# # 결과 출력
# if mutiple_max:
#    print("?")
# else:
#    print(max_char)

# 2.
# word = input().strip().upper()

# frequency = {}

# for char in word:
#    frequency[char] = frequency.get(char, 0 ) + 1
   
# max_count = max(frequency.values())
# max_chars = [char for char, count in frequency.items() if count == max_count]

# if len(max_chars) > 1:
#    print('?')
# else:
#    print(max_chars[0])


## 10951

# while True:
#    try:
#       A, B = map(int, input().split())
#       print(A+B)
#    except:
#       break

# 반복문 합

X = int(input())
N = int(input())
total = 0
for _ in range(N):
   a, b = map(int, input().split())
   total += a * b

if total == X:
   print("Yes")
else:
   print("No")