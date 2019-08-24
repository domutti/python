#2019 08 24
'''
함수: function - 기능
    내장 함수: python에서 기본으로 구현된 함수
     - round(): 지정한 자리 까지의 소수점 반올림 후 반환
     - pow(x, n): x의 n승을 반환
     - abs(): 절댓값을 반환
     - divmod(): 몫과 나머지 반환
     - max(): 최댓값 반환
     - min(): 최솟값 반환
     - sum(): 인자들의 합 반환
     - chr(): ASCII 문자 반환
     - ord(): ASCII 숫자 반환
ASCII코드: 0 ~ 127 까지의 숫자를 고유 문자, 기호에 대응시킨 문자 변환 규약표, google - ASCII table 참조
'''
a = 12.123121
print("a: {}".format(a))
print("round(a, 2): {}".format(round(a, 2)))

b = 2
print("2의 4승: {}".format(pow(b, 4)))

c = -5
print("c : {}".format(c))
print("abs(c): {}".format(abs(c)))

f, q = divmod(10, 3)
print("divmod(10, 3): {}, {}".format(f, q))

x = max(1, 2, 3, 4, 5)
print("max(x): {}".format(x))
print("min(x): {}".format(x))


arr = [1, 4, 8]
s = sum(arr)
print("sum(1, 4, 8): {}".format(s))

v1 = 65
print("v1 : {}".format(v1))
print("chr(v1): {}".format(chr(v1)))

v2 = 'A'
print("v2 : {}".format(v2))
print("ord(v2): {}".format(ord(v2)))
