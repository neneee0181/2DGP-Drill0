print("hello")

print(1 + 1)

print(1 / 2)
print(1 // 2)

print(2 ** 2)

print(2 ** 1024)

import math

print(math.pi)

print(3 ** 2 * math.pi)

r = 12  # 변수 타입 선언 x

name = "trump"
name2 = 'trump'

statement = " I'm Tom. ''''\\\\///\/\/\'' "
print(statement)

print(type(name))

status = True
status2 = False

# 파이썬은 문자열 x 길이가 3인 문자열?

mins = input("Enter Minutes: ")
print(mins)

mins_int = int(mins)
mins_int = mins_int * 60
print(mins_int)

mins = int(mins)  # 최초 mins의 타입은 str이지만 형 변환을 통해 바꾼 값을 다시 mins에 넣음.

print('SEOUL' == "SEOUL")

first = 'young bin '
last = 'you'
fullName = first, last
print(fullName)
fullName = first + last
print(fullName)

print(fullName * 2)

print(fullName[4])

print(fullName[-1])  # 문자열의 마지막 글자

print(fullName[0:5])  # slice? 0~5번 가져옴

print(fullName[-3:])

print(fullName[::2])  #리버스

print(fullName[::-2])
