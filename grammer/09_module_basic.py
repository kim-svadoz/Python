import random
# Built-in Function( 파이썬 내장 함수 ) - 기본적으로 쓸 수 있는 함수
# 내장이지만 필요할 때 import해서 사용할 수 있는 것이 - 모듈
print(dir(random))
pick = random.choice(range(10))
pick1 = random.choice([1, 2, 3, 4, 5])
print(pick)
print(pick1)

# help(random.choice)
# help(random.sample)

pickS = random.sample(range(10), 3)
print(pickS)