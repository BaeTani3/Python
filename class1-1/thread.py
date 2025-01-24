import threading
from time import sleep

##############################
#1
# def bar():
#     for _ in range(5):
#         print("hello")

# my_thread = threading.Thread(target=bar, daemon=True)

# my_thread.start()
# my_thread.join()

# print("finish")

############################
#2
# my_lock = threading.Lock()

# def bar():
#     for count in range(1, 6):
#         with my_lock:
#             print(f"bar: {count}")

# def foo():
#     for count in range(1, 6):
#         with my_lock:
#             print(f"foo: {count}")

# thread_1 = threading.Thread(target=bar)
# thread_2 = threading.Thread(target=foo)

# thread_1.start()
# thread_2.start()

# print("finish")

###############################
#3
balance = 0

def deposit():
    global balance
    amount = 10
    for count in range(10):
        balance = balance + amount
        sleep(0.01)
        print(f"Deposit!, balance : {balance}")

def withdraw():
    global balance
    amount = 10
    for count in range(10):
        balance = balance - amount
        sleep(0.01)
        print(f"withdraw!, balance : {balance}")

thread_1 = threading.Thread(target=deposit)
thread_2 = threading.Thread(target=withdraw)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f"[balance]: {balance}")
