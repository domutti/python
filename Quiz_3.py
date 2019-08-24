'''
숫자가 5의 배수인지 확인하는 코드를 작성하시오.
'''
num = int(input("input number > "))

if num % 5 == 0:
    print("{}는 5의 배수입니다.".format(num))
else:
    print("{}는 5의 배수가 아닙니다.".format(num))
print()


'''
서로 다른 두 수 중 큰 수를 찾아서 출력하는 코드를 작성하시오.
'''
n1, n2 = input("서로 다른 두 수 입력 > ").split()
max1 = 0

if n1 == n2:
    print("서로 다른 두 수를 입력하세요.")
elif n1 > n2:
    max1 = n1
elif n1 < n2:
    max1 = n2
print("두 수 중 큰 수는 {} 입니다.".format(n1))
print()


'''
서로 다른 세 수 중 큰 수를 찾아서 출력하는 코드를 작성하시오.
'''
x1, x2, x3 = input("서로 다른 세 수 입력 > ").split()
max2 = 0

if x1 == x2 or x2 == x3:
    print("서로 다른 세 수를 입력하세요.")
elif x1 > x2 and x2 > x3:
    max2 = x1
elif x1 < x2 and x2 > x3:
    max2 = x2
elif x1 < x3 and x2 < x3:
    max2 = x3
print("제일 큰 수는 {} 입니다.".format(max2))
print()


'''
두 점의 위치를 입력받아 두 점 사이의 거리를 구하는 코드를 작성하시오.
'''
l1, l2 = input("두 점의 위치 입력 > ").split()

print("{}와 {} 사이의 거리: {}".format(l1, l2, abs(int(l1) - int(l2))))
print()
