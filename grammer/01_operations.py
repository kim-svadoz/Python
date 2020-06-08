# 01_operations.py
# 논리연산자
# and, or, not
print("_____and_____")
print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("_____or_____")
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print("_____not_____")
print(not True)
print(not [])
print(not False)
print(not True)

# in, not in
print("______in_____")
print('a' in 'apple')
print(1 not in [1,2,3])

# 단축 평가
print('' or 'Text' or 'Text_2')
print('Text' and '' or 'Text_2')