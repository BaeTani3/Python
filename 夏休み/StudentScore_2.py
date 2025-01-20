# 학생 성적 처리 프로그램

count = 0
student_list = {} 

# 학생 성적 입력 함수
def student_score_input():
    
    id = int(input("학번 입력: "))
    name = input("이름 입력: ")
    kor = int(input("국어 성적: "))
    eng = int(input("영어 성적: "))
    math = int(input("수학 성적: "))
    sum = kor + eng + math 
    avg = sum / 3
    student_list[id] = [name, kor, eng, math, sum, avg]
    print(student_list)
    return 

# 학생 목록 출력 items() 활용하여 튜플 반환
def student_list_output():
    for i in student_list.items():
        print(i)
    
# 전체 학생 평균 값 계산
def student_sum_avg():
    if len(student_list) == 0:
        return 0.0
    avg = 0
    for i in student_list.keys():
        avg += student_list[i][-1]
    
    return round(avg / len(student_list), 2)

# 학번 입력 함수
def student_number_input():
    student_keys = int(input("학번 입력하세요: "))
    print(f"학번: {student_keys} 이름: {student_list[student_keys][0]}\
국어: {student_list[student_keys][1]} 영어: {student_list[student_keys][2]}\
수학: {student_list[student_keys][3]} 합계: {student_list[student_keys][4]}\
평균: {student_list[student_keys][5]}")    
    
    

# 메뉴 생성
MENU = """
=================
1. 학생 성적 입력
2. 학생 목록 출력(입력 순)
3. 학번 입력
4. 프로그램 종료
=================
"""

# 학생 정보 리스트 생성
while True:  
    print(MENU)
    print(f"현 입력데이터 갯수 : {len(student_list)}")
    print(f"전체 학생 평균 값: {student_sum_avg()} ")
    user_value = int(input())
    
    # 1. 학생 성적 입력
    if user_value == 1:
        student_score_input() 
        count += 1
           
    # 2. 학생 목록 출력
    elif user_value == 2:
        student_list_output()
    
    # 3. 학번 입력 (추가)
    elif user_value == 3:  
        student_number_input() 
        
    # 4. 프로그램 종료
    elif user_value == 4:
        print("프로그램 종료")
        break
