# 10 ~ 20사이 정수 중 짝수의 합을 계산하라.

sum = 0
for num in range(10,21):
    if num % 2 == 0:
        sum += num
        
print(sum)

# 2번째
sum = 0

for value in range(10, 21, 2):
    sum = sum + value
print(sum)


for dan in range(2,10):
    
    if dan == 5 or dan == 7:
        continue
    
    for num in range(1,10):
        print(f"{dan} X {num} = {dan*num}")
        
    print("----------------")