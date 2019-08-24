'''
3.141592 소숫점 셋 째 자리 출력
'''
pi = 3.141592
print("pi: {}".format(round(pi, 3)))
print()

'''
아래의 값 중에서 최대, 최솟값을 구하시오
'''
value = [5, 8, 3, 2, 9]
print("value : {}".format(value))
print("value의 최댓값 : {}, 최솟값: {}".format(max(value), min(value)))
print()

'''
위에서 구한 최댓값의 제곱 값을 구하시오
위에서 구한 최댓값을 최솟값으로 나눈 몫과 나머지를 구하시오
'''

maxVal = max(value)
minVal = min(value)
x, y = divmod(maxVal, minVal)
print("{}의 제곱 값: {}".format(maxVal, pow(maxVal, 2)))
print("{} / {} = {}, 나머지: {}".format(maxVal, minVal, x, y))
print()

'''
소문자 z의 ASCII 값을 구하시오
소문자 h를 대문자로 변환해서 출력하시오
'''
h = 'h'
hASC = ord(h)
H = chr(int(hASC - 32))
print("z의 ASCII 값: {}".format(ord('z')))
print("{}의 ASCII 값: {}, 대문자 변환: {}".format(h, hASC, H))
print()
