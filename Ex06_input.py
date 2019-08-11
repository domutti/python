#2019 08 11
'''
입력 함수 : input() - 터미널에 입력한 값을 프로그램 안으로 가져옴
'''
print("데이터 입력 > ", end='')
value = input()
print("입력된 값 : {}".format(value))
print()
value2 = input("문자열 입력 > ")
print("value2: {}".format(value2))
print()
# 데이터 입력 > sad
# 입력된 값 : sad

# 문자열 입력 > asd
# value2: asd

v1 = input("첫 번째 입력 ")
v2 = input("두 번째 입력 ")
vSum1 = v1 + v2
print("{} + {} = {}, type: {}".format(v1, v2, vSum1, type(vSum1)))
print()
# 첫 번째 입력 sad
# 두 번째 입력 asd
# sad + asd = sadasd

#  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# | v1Num = int(v1)         |
# | v2Num = int(v2)         | < 정수형 연산
# | vSum1Num = int(vSum1)   | 
#  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

n1 = int(input("첫 번째 정수 입력 > "))
n2 = int(input("두 번째 정수 입력 > "))
nSum1 = n1 + n2
print("{} + {} = {}, type: {}".format(n1, n2, nSum1, type(nSum1)))
print()
# 첫 번째 정수 입력 > 312312
# 두 번째 정수 입력 > 412312
# 312312 + 412312 = 724624, type: <class 'int'>

one = 1
d1 = int(input("{} 번째 입력 ".format(one)))
two = 2
d2 = int(input("{} 번째 입력 ".format(two)))
print("입력 값 : {}, {}".format(d1, d2))
print()
# 1 번째 입력 412
# 2 번째 입력 314
# 입력 값 : 412, 314

print("정수 2개 입력")
z1 = input()
z2 = input()
print("z1 : {}, z2 : {}".format(z1, z2))
print()

# space로 데이터 구분
# input().split() < space로 데이터를 분리
x1, x2 = input("데이터 2개 연속 입력 > ").split()
print("x1 : {}, x2 : {}".format(x1, x2))
