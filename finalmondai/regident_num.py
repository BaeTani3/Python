

# def regident_check(num):
#     check_list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
#     total = 0
#     count = 0
    
#     for i in num:
#         if i != "-" and count < 12:
#             total += int(i) * check_list[count]
#             count += 1

         
#     print(total)
    

# regident_num = "790608-2552416"
# regident_check(regident_num)


######## 교수님 ##########

def get_check_digit(arg_ssid):
    weight = [(value % 8) + 2 for value in range(12)]

    # 인자값 변환
    ssid = [int(value) for value in arg_ssid]
    
    sum_values = sum([ssid[index] * weight[index] for index in range(12)])
    
    return (11 - (sum_values % 11)) % 10

# 유효한 주민번호 -> True else False
def is_valid_ssid(arg_ssid):
    
    arg_ssid = arg_ssid.replace("-", "")
    
    if len(arg_ssid) != 13:
        return False

    # 체크 값 계산 알고리즘 구현 필요
    check_digit = get_check_digit(arg_ssid[:-1])
    
    if check_digit == int(arg_ssid[-1]):
        return True
    else :
        return False

print(is_valid_ssid("790608-2552416"))