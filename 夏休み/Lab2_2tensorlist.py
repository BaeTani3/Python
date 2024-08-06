# 2차원 리스트 조작
# 사용자로부터 행과 열의 수를 입력 받는다.
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

# 사용자가 각 요소에 들어갈 값을 직접 입력
# matrix 리스트 생성
matrix = [[]*col for _ in range(row)]
print(matrix)
for rows in range(row):
    for cols in range(col):
        value = int(input(f"Enter value for [{rows}][{cols}]: "))
        matrix[rows].append(value)
# 입력이 완료되면 완성된 2차원 리스트를 출력
for rows in matrix:
    for col in rows:
        print(col,end=" ")
    print()