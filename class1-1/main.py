# # main.py

# import random_1
# # 파이썬 초기의 random 모듈을 가져오는게 아니라
# # 내가 만든 모듈을 가져온다.
# random_1.randint(2, 10)

# print(random_1.test_1)

# # 지금까지 import를 통해 모듈을 불러오기만 했지만,
# # 앞으로는 프로젝트를 통해 모듈(하위)을 만들고 패키지(상위)를 관리한다.

# from bar import file_name as b_name
# import foo

# # .연산자를 통해 foo 모듈의 특정 객체를 가져올 수 있다
# foo.print_name(b_name)

# # code에 import를 많이 하게되면 불필요한 메모리사용으로 

# from random_1 import test_1 as num, P as print_name
# print(print_name, num)

# # from 모듈명 import 사용객체 as 별칭

# # 모듈이 위치한 곳 3가지
# # 현재 파일이 있는 폴더, 내장 모듈, pip 서드파티 모듈
# # 찾는 순서 

# import sys # 현재 모듈을 찾는 순서가 디렉토리 별로 출력

# print(type(sys.path))

# for path in sys.path:
#     print(path)
    
# c:\Users\USER\Desktop\programing
# c:\Users\USER\AppData\Local\Programs\Python\Python312\python312.zip
# c:\Users\USER\AppData\Local\Programs\Python\Python312\DLLs
# c:\Users\USER\AppData\Local\Programs\Python\Python312\Lib
# c:\Users\USER\AppData\Local\Programs\Python\Python312
# c:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages -> pip해서 깔리는 폴더

# ----------------------------------------------------------------------
# 내장 변수 (인터프리터가 만듬) 매직변수 

import bingo

from bingo import name as young # 현재 모듈되고 있는 메인의 이름을 출력한다.
print(young)

bingo.print_p()