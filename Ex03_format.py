#2019 08 11
'''
format()
> print("{}".format(value))
  {}: format field - 안에 원하는 값을 출력 할 수 있음
'''

num = 1
title = "원피스"

print(num, "권 -", title)
# compile 결과: 1 권 = 원피스
print("{} 권 = {}".format(num, title))
# compile 결과: 1 권 = 원피스
print()

##############################################################################

'''
print("{:.nf}".format{value})
 -실수형 데이터를 소숫점 n의 자리까지 출력
'''

height = 186.33
print("키 : {}".format(height))
# compile 결과: 키 : 186.33
print("키 : {:.1f}".format(height))
# compile 결과: 키 : 186.3
print()

##############################################################################
'''
진수 변환 출력
> print("{:b}".format{value})
 - 2진수 출력
> print("{:o}".format{value})
 - 8진수 출력
> print("{:x}".format{value})
 - 16진수 출력
'''

n = 10
print("n : {}".format(n))
print("{} 의 2진수는 {:b} 입니다.".format(n, n))
print("{} 의 8진수는 {:o} 입니다.".format(n, n))
print("{} 의 16진수는 {:x} 입니다.".format(n, n))
# 10 의 2진수는 1010 입니다.
# 10 의 8진수는 12 입니다.
# 10 의 16진수는 a 입니다.
print()

##############################################################################
'''
출력 폭 지정
> print("{:int(n)}".format(value))
 - 정수 값 n 만큼의 공간 확보를 하고 값을 출력
> print("{:<int(n)}".format(value))
 - 좌측 정렬
> print("{:^int(n)}".format(value))
 - 중앙 정렬
> print("{:>int(n)}".format(value))
 - 우측 정렬
'''

print("{:5}|".format(123))
print("{:<5}|".format(123))
print("{:^5}|".format(123))
#   123|
# 123  |
#  123 |
print("{:5}|".format("ABC"))
print("{:>5}|".format("ABC"))
print("{:^5}|".format("ABC"))
# ABC  |
#   ABC|
#  ABC |
print()
