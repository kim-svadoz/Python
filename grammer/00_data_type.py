# 1. 출력해보기
print('Hello, world!')

# 프로그래밍 언어의 기본 3가지
# 1. 변수저장 - 무엇을 저장할 수 있을까?
number = 10
string = '10'
boolean = True
# 파이썬에는 값이 없다는 뜻인 None 타입이 존재
noting = None
print(number, string, boolean, noting)
print(type(noting))

# 1-1. 정수형

float_num = 1.3
complex_num = (3 + 3j)
print(type(number), type(float_num), type(complex_num))

import sys
max_num = sys.maxsize
print(max_num)
super_max = max_num*max_num

# 2. bool
print(type(True))
print(type(False))
# 0, 0.0, [], {}
print (False==0)

# 3. 문자형
# '' ""
greeting =  'hi'
name = "kim"
print(greeting, number)

# 문자열 입력 받기
# input()
age = input("나이를 입력해 주세요 : ")
print(type(age))
print(int(age))
print(type(int(age)))

# string interpolation
name = 'kim'
print('안녕하세요.', name)
print('{},{}' .format(greeting, name))
print(f'{greeting},{name}')

# 연산과 출력 형태 지정
pi = 3.141592
print(f'원주율은 {pi:.3}. 반지름 2인 원의 업ㄹ이는 {pi*2*2}')