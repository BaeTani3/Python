
# 학생 성적 관리 프로그램
# 학생들의 성적을 키보드로부터 입력 받아 리스트에 저장하고 
# 입력 값을 출력하는 프로그램을 함수를 이용하여 작성하라
result_list = []
# 함수 구성은 자유
# 학생 성적 입력 함수
def student_score():
    student_number = int(input("학번을 입력하세요\n"))
    name = input("이름을 입력하세요\n")
    Language_score = int(input("국어 성적을 입력하세요\n"))
    English_score = int(input("영어 성적을 입력하세요\n"))
    Math_score = int(input("수학 성적을 입력하세요\n"))
    total = Language_score + English_score + Math_score
    average = total / 3
    result_list.append([student_number, name, Language_score, English_score, Math_score, total, average])
    return result_list

 # 전체 학생 평균 값 계산을 위한 함수
def calculate_average(result_list):
    if not result_list:
        return 0
    total_sum = sum(student[6] for student in result_list)
    total_count = len(result_list)
    return total_sum / total_count
  
  
MENU = """
====================
1. 학생 성적 입력
2. 학생 목록 출력(입력 순)
3. 프로그램 종료
====================
"""

while True:
    print(MENU)
    print(f"현 입력데이터 갯수: {len(result_list)}")
    print(f"전체 학생 평균 값: {calculate_average(result_list):.2f}")
    
    N = int(input())
    
    # 학생 성적 입력
    if N == 1:
        student_score()

    # 학생 목록 출력(입력 순)
    elif N == 2:
        for col in range(len(result_list)):
            print(f"id : {result_list[col][0]} name : {result_list[col][1]}\
kor : {result_list[col][2]} eng : {result_list[col][3]} math : {result_list[col][4]}\
sum : {result_list[col][5]} avg : {result_list[col][6]} ")
    
    # 프로그램 종료
    elif N == 3:
        print("프로그램 종료")
        break


