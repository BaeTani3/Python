# # 행렬 덧셈 2738

# N = 3
# M = 3
# matrix = []

# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# matrix2 = []
# for _ in range(M):
#     row = list(map(int, input().split()))
#     matrix2.append(row)


# result = []
# for i in range(N):
#     result_row = []
#     for j in range(M):
#         result_row.append(matrix[i][j] + matrix2[i][j])
#     result.append(result_row)

# for row in result:
#     print(' '.join(map(str, row)))
    
# # 

# 직접
N, M = map(int,input().split())


matrix_1 = []
for _ in range(N):
    result = list(map(int,input().split()))
    matrix_1.append(result) 

matrix_2 = []
for _ in range(N):
    result = list(map(int,input().split()))
    matrix_2.append(result) 
    
# 합
matrix = []

for i in range(N):
    matrix_mae = []
    for j in range(M):
        matrix_mae.append(matrix_1[i][j] + matrix_2[i][j])
    matrix.append(matrix_mae)

# 출력
for i in matrix:
    print(' '.join(map(str,i)))