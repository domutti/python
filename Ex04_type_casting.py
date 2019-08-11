#2019 08 11
'''
자료형: 데이터를 보관하고 공간의 형식을 정의한 것
int: 정수형 데이터 - -2^16~2^16
float: 실수형 데이터
bool: 참, 거짓을 표현하는 부울린 - 0을 제외한 모든 값: True, 0: False
str: 문자열 클래스
None: Null
type(): 값이 저장된 메모리 주소의 자료형을 확인하는 함수
'''
t = True
print("t : {}".format(t))
print("t : {}".format(type(t)))
print()
# t : True
# t : <class 'bool'>

N = 10
print("N : {}".format(N))
print("N : {}".format(type(N)))
print()
# N : 10
# N : <class 'int'>

R = 1.2
print("R : {}".format(R))
print("R : {}".format(type(R)))
print()
# R : 1.2
# R : <class 'float'>

a_1 = 'string'
a_2 = "문자열"
print("a_1 : {}".format(a_1))
print("a_1 : {}".format(type(a_1)))
print("a_2 : {}".format(type(a_2)))
print()
# a_1 : string
# a_1 : <class 'str'>
# a_2 : <class 'str'>

##############################################################################
'''
casting: 자료형을 일시적으로 변환 할 때 사용
> <int, float, bool, ...>(value)
'''

# bool() 변환
val1 = 1
c_val1 = bool(val1)
print("val1 : {}".format(type(val1)))
print("c_val1 : {}".format(type(c_val1)))
print("val1 : {}".format(val1))
print("c_val1 : {}".format(c_val1))
print()
# val1 : <class 'int'>
# c_val1 : <class 'bool'>
# c_val1 : True

# str() 변환
val2 = 123
c_val2 = str(val2)
print("val2 : {}".format(type(val2)))
print("c_val2 : {}".format(type(c_val2)))
print("val2 : {}".format(val2))
print("c_val2 : {}".format(c_val2))
print()
# val2 : <class 'int'>
# c_val2 : <class 'str'>
# val2 : 123
# c_val2 : 123

# int() 변환
print("{}, {}".format(int(True), int(False)))
print("{}, {}".format(int("11"), int("-12")))
print("{}, {}".format(int(1.1), int(-11.1)))
print()
# 1, 0
# 11, -12
# 1, -11

val3 = "100"
c_val3 = int(val3)
print("val3 : {}, {}".format(val3, type(val3)))
print("c_val3 : {}, {}".format(c_val3, type(c_val3)))
print()
# val3 : 100, <class 'str'>
# c_val3 : 100, <class 'int'>

# float() 변환
print("{}, {}".format(float(True), float(False)))
print("{}, {}".format(float("11"), float("-12")))
print("{}, {}".format(float(1.1), float(-11.1)))
print()
# 1.0, 0.0
# 11.0, -12.0
# 1.1, -11.1
val4 = "100.12312"
c_val4 = float(val4)
print("val4 : {}, {}".format(val4, type(val4)))
print("c_val4 : {}, {}".format(c_val4, type(c_val4)))
print()
# val4 : 100.12312, <class 'str'>
# c_val4 : 100.12312, <class 'float'>
