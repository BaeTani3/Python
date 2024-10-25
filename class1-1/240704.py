# del과 pop

bar = [10, 20, 30, 40]
# del을 하면 해당 인덱스 값이 삭제되고, 뒤의 요소들이 당겨진다.
del bar[2] # del 보다 이쁜 함수 pop
print(bar.pop(2)) 

# pop 함수는 del과 유사하게 작동하지만, 삭제된 요소를 반환하는 추가 기능이 있다.
foo = [10, 20, 30, 40]
while len(foo) > 0:
    item = foo.pop(0)
    print(item) # 값을 반환한다.

# append 와 insert
bar = [10, 20, 30, 40]
# insert 함수는 리스트의 특정 위치에 새로운 요소를 삽입합니다.
bar.insert(3, 70) 
print(bar)  # 결과: [10, 20, 30, 70, 40]

# append 함수는 리스트의 끝에 새로운 요소를 추가합니다..
bar.append(50)
print(bar) # 결과: [10, 20, 30, 70, 40, 50]

###############2차원#######################
bar = [0, 0, 0, 0, 0, 0]

bar = [ 0 for _ in range(6) ]

print(bar)

bar = [0] * 6

print(bar)

# 3 X 4 행렬 생성 , 모든 값은 0
row = 3
col = 4
matrix = [[0 for _ in range(col)] for _ in range(row)]
print(matrix)

matrix = [[0]*4 for _ in range(3)]
print(matrix)


bar = [[10, 20], [30, 40], [50, 60]]

# bar 리스트의 주소값 출력
print(f"Address of bar: {id(bar)}")

# bar 리스트 내부의 각 리스트의 주소값 출력
for i, sublist in enumerate(bar):
    print(f"Address of bar[{i}]: {id(sublist)}")
    
# 데이터 순회
bar = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]

# 'bar' Matrix의 모든 원소를 순회
for col in bar: # 각 'row'는 'bar'의 한 행을 나타낸다
    for item in col: # 'row'의 각 요소(즉, 각 열의 값)를 'item'으로 순회
        # 현재 'item'을 출력하고, 같은 행의 다음 아이템과 공백으로 구분
        print(item, end = ' ')
    print()
    

row = 2
col = 3

matrix = [value for value in range(1,7)]
print(matrix)

print(matrix[0])


def print_matrix(arg_list):
    for row in arg_list:
        for col in row:
            print(col, "\t", end="")
        print()
        
matrix = [[1,2,3], [4,5], [6,7]]
print_matrix(matrix)

matrix.append([8,9,10,11])
matrix.insert(2,[100,200,300])
print(matrix)


matrix_num = [ value for value in range(1,19)]

bar = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
print(bar)

# 3x3x3 크기의 3차원 리스트를 순서대로 증가하는 숫자로 채우기
size = 3
counter = 1

three_d_list = [[[counter + k + j*size + i*size*size for k in range(size)] for j in range(size)] for i in range(size)]

# 결과 출력
for layer in three_d_list:
    for row in layer:
        print(row)
    print()

# 매트릭스가 2개
bar = [\
    [[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]]]\
    ,[[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]]\
    ]

for matrix_3 in bar:
    for matrix in matrix_3:
        for row in matrix:
            for item in row:
                print(item, "\t", end="")
            print()
        print("-" * 20)
    

