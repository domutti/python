import time

def clear(a):
    time.sleep(a)
    print("\n"*100)

def sleep(x):
    time.sleep(x)

'''
1~ 30까지의 수를 아래와 같은 형태로 출력하는 코드를 작성하세요
1   2   3   4   5   6   7   8   9   10
11  12  13  14  15  16  17  18  19  20
21  22  23  24  25  26  27  28  29  30
'''
ran = range(1, 31)
k = 0

print("1부터 30까지의 수를 출력합니다.")
sleep(1)
for k in ran:
    if k % 10 == 0:
        print(k)
    else:
        print(k, end = '\t')
clear(2)


'''
1~ 입력받은 수 까지 출력하는 코드를 작성하세요
'''
ran2 = int(input("input number > "))
i = 0

print("1부터 {}까지의 수를 출력합니다.".format(ran2))
sleep(1)
for i in range(1, ran2 + 1):
    print(i)
clear(2)


'''
1~20 사이의 5의 배수를 출력하는 코드를 작성하세요
'''
ran3 = range(1, 21)
j = 0

print("1부터 20 사이의 5의 배수를 출력합니다.")
sleep(1)
for j in ran3:
    if j % 5 == 0:
        print(j)
clear(2)


'''
1~ 입력받은 수 까지의 합을 구하는 코드를 작성하세요
'''
cnt = 0
ran4 = int(input("input number > "))
sum = 0

print("1부터 {}까지의 합을 출력합니다.".format(ran4))
sleep(1)
for cnt in range(1, ran4 + 1):
    sum += cnt
print(sum)
clear(2)


'''
1~ 입력받은 수 까지의 홀수를 출력하고 합을 구하는 코드를 작성하세요
'''

cnt2 = 0
ran5 = int(input("input number > "))
sum2 = 0

print("1부터 {}까지의 홀수와 그 합을 출력합니다.".format(ran5))
sleep(1)
for cnt2 in range(1, ran5 + 1):
    if cnt2 % 2 == 1:
        sum2 += cnt2
        print(cnt2)
print()
print("1 ~ {}까지의 홀수의 합 : {}".format(ran5, sum2))
clear(2)


'''
구구단 값 하나를 입력받아서, 해당 단을 모두 출력하세요
'''
row = int(input("input row > "))
column = 1
val = 0
k = 0

print("구구단 {}단을 출력합니다.".format(row))
sleep(1)
for k in range(1, 10):
    val = row * column
    print("{} * {} = {}".format(row, column, val))
    column += 1
    val = 0
clear(2)


'''
두 수를 입력받고, 그 사이의 합을 출력하세요
'''
first = int(input("input first number > "))
last = int(input("input last number > "))
sum = 0
v = 0

print("{}부터 {}까지의 수의 합을 구합니다.".format(first, last))
if first > last:
    for v in range(first, last + 1):
        sum += v
else:
    for v in range(last, first + 1):
        sum += v
print("합: {}".format(sum))
clear(2)


'''
A:Z 출력
'''
print("A부터 Z까지 출력합니다.")
sleep(1)
for l in range(65, 91):
    print("{}".format(chr(l)), end = ' ')
clear(2)


'''
"have a nice day"를 변수에 저장하고, 위 문장에서 찾을 문자 하나를 입력받습니다.
찾는 문자가 문장안에 몇 개 있는지를 구하는 코드를 작성하세요
'''
string1 = "have a nice day"
cnt = 0
j = 0
print(string1)
SearchString = input("찾을 문자를 입력하세요 > ")

for j in range(0, 15):
    if string1[j] == SearchString:
        cnt += 1
print("{}은 {} 개".format(SearchString, cnt))


'''
통장에 첫날에는 1원을 입금하고,
둘째날부터는 전날 입금액의 2배씩 입금해서 30일동안 입금한 총 금액을 구하세요
'''
x = 0
sum = 0
cnt = 0

for x in range(1, 31):
    if day == 1:
        sum = 1
    else:
        sum *= 2
    cnt += sum
print("30일동안 입금한 총 금액은 {}원 입니다.".format(cnt))
