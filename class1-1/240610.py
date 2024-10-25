'''
# 정수 3개를 입력 받아 합계와 평균을 출력하는 프로그램을 작성하라

def get_int(arg_num):
    input_values = []
    for _ in range(arg_num):
        input_values.append(int(input("입력 값:")))
    
    return input_values    

def get_sum_avg(arg_list):
    sum = 0
    for value in arg_list:
        sum += value
        
    avg = sum / len(arg_list)
    
    return sum, avg

    
def get_sum(arg_list):
    sum = 0
    for value in arg_list:
        sum += value
    
    return sum

input_list = get_int(5)

sum, avg = get_sum_avg(input_list)
print(sum, avg)

# 교수님은 쪼개고, 일반화 작업(누구나 쓸 수 있게) 을 한다.
# 프로그래머에 대한 필수 능력 1.신속 2.정확 3. 확장성

def sum (arg_first, arg_second):
    sum = arg_first + arg_second
    
    if sum < 0 :
        print("음수")
        return
    # 함수 정의 시 return 있어도 되고 없어도 된다. 즉 option 이다
    return sum

result = sum(2, 3)
print(result)

result = sum(-2, -3)
print(result)


def trial(arg_num):
    
    if arg_num % 2 == 0 :
        return "짝수"
    else :
        return "홀수"
    
arg_num = int(input("하나의 수 입력: "))
print(trial(arg_num))

#------------------------------------------------------#

def get_even_odd(arg_value):
    msg = "짝수" if arg_value % 2 == 0 else "홀수" 
    
    return msg

# 함수에 인자 값 4개를 입력 받아 합계와 평균을 반환하는 함수를 작성하라
# 그리고 반환된 합계와 평균을 화면에 출력하라

def get_sum_avg(arg1, arg2, arg3, arg4):
    sum = arg1 + arg2 + arg3 + arg4 
    avg = sum / 4
    # 파이썬 만의 특징 = 반환값이 2개 이상이면 tuple로 변환 후 반환
    return sum , avg    

sum, avg = get_sum_avg(1, 2, 3, 4)
print(sum, avg)

value = get_sum_avg(1, 2, 3, 4)
print(value[0], value[1])


# 변수를 나누면 primitive (값 그 자체를 저장)  num/ str/ boolean
# reference (메모리 주소값을 저장)



kin = [1, 2]
kin[0] = 1 # [ 를 만나는 순간, 해당 주소값으로 점프를 해야하구나 
하나의 수식이다.

6-12--------------------------------------------------------------#

argument 

1) positional argument

def foo(arg_a, arg_b, arg_c):
    print(arg_a,arg_b,arg_c)
    
foo(1, 2, 3)

# 2) keyword argument
# 순서가 의미가 없다. 매개변수의 이름을 이용해서 지정
def pos(arg_a, arg_b, arg_c):
    print(arg_a, arg_b, arg_c)

pos(arg_c = 1, arg_b = 2, arg_a = 3)

# 왜 키워드 인자값을 사용할까? 굳이

# 3) default argument

def kin(arg_a, arg_b, arg_c = 3, arg_d = 4):
    print(arg_a, arg_b, arg_c, arg_d)
    

kin(6, 7, 8, 9)
kin(6, 7, arg_d= 10)

print("hello","no","hi", end = "")


# 구구단

def printMulTable(arg_start, arg_end = None):
    
    # 인자 값이 한개가 입력 되었을 경우 start 값만 출력
    arg_end = arg_start + 1 if arg_end is None else arg_end + 1
    
    for i in range(arg_start, arg_end): 
        for j in range(1,10):
            print(f"{i} X {j} = {i * j}")
            
printMulTable(2)
print("-" * 10)
printMulTable(2,5)

# variable parameter : 가변 파라미터
# 1) *  -> 가변 : tuple로 받겠다.
# 2) ** ->

def foo(*args):
    if len(args) == 1:
        start = end = args[0] # chainning
        
    elif len(args) == 2:
        start, end = args
    else :
        return
    
    for dan in range(start, end + 1):
        for num in range(1, 10):
            print(f"{dan} X {num} = {dan*num}")

foo(2)
foo(3,5)'''

def bar(**args):
    print(len(args))
    
    for key, value in args.items():
        print(f"key: {key}, value : {value}")
        
bar(test = 2, king = 3) # 1
bar(test = 2, king = 3, lion = 4)  # 1


def foo(arg_a, arg_b, arg_c, arg_d, arg_e):
    print(arg_a, arg_b, arg_c, arg_d, arg_e)

# foo(1,2,3,4,5) 하나하나 치기 힘들다.
arg_list = [value for value in range(1, 6)]

foo (*arg_list)
print(type(arg_list))