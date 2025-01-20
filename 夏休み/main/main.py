import sys
import os

# 비표준 경로 추가 : 개인 환경에 맞게 수정
# module_path = os.getcwd() + "\external_module"


module_path = os.getcwd() + "\\module"
print(os.getcwd())

if module_path not in sys.path:
    sys.path.append(module_path)
    
# 모듈 임포트
import external_module

def main():
    greeting = external_module.greet("Python User")
    print(greeting)
    
if __name__ == '__main__':
    main()
    

# print("Current sys.path:")
# for path in sys.path:
#     print(path)
    
# my_module = os.getcwd() + "\sub_module"
# sys.path.append(my_module)

# print("\nUpdated sys.path:")
# for path in sys.path:
#     print(path)

