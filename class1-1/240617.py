

def get_stats(*numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average

total, count, average = get_stats(10,20,30,40,50)
print(f"{total}\n{count}\n{average}")


# Lab 1

def print_hello():
    print("hello, world!")
    
print_hello()

# Lab 2

def sum_numbers(a, b):
    return a + b

print(sum_numbers(3, 5))

# Lab 3

def greet_user(name):
    print(f"Hello, {name}!")
    
greet_user('Alice')

# Lab 4

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else :
        return c
    
print(max_of_three(30, 20, 20))

# Lab 5

def is_even(num):
    return num % 2 == 0
    
print(is_even(4))
print(is_even(5))

# Lab 6

def wrap_in_tag(A, B):
    A = f"<{A}>"
    C = f"/{A}"
    return f"{A}{B}{C}"

print(wrap_in_tag('p', 'world'))
print(wrap_in_tag('b', 'world'))


# Lab 7 

def contains(Value_list, Value):
    for _ in Value_list:
        if _ == Value:
            return True

    return False
        
print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))


# Lab 8

def calculate_average(*num):
    total = sum(num)
    average = total / len(num)
    return average

print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average(6, 7, 8))
print(calculate_average(10, 20))

##### ###### # #### # #########

def bar(arg_fnc):
    arg_fnc()
    
def foo():
    print("안녕하세요: ")
    
bar(foo)

