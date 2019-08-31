import time

def clear(a):
    time.sleep(a)
    print("\n"*100)

def sleep(x):
    time.sleep(x)

'''
입력 한 수 만큼의 '*'를 출력하는 코드를 작성하세요.
'''
star = '*'
a = int(input("input number > "))
b = 0

while b < a:
    print(star)
    b += 1
clear(2)


'''
1 이상의 숫자 5개를 입력받고, 그 합을 구하는 코드를 작성하세요
'''
cnt = 0
sum = 0

while cnt < 5:
    a1 = int(input("숫자 입력 > "))
    sum += a1
    cnt += 1
print("합: {}".format(sum))
clear(2)


'''
입력에 0이 들어올 때 까지의 합을 구하는 코드를 작성하세요
'''
data = 1
total = 0

while data != 0:
    data = int(input("숫자 입력 > "))
    total += data
print(total)
clear(2)

'''
이름, 나이, 성별을 입력받아서 출력하는 코드를 작성하세요.
    이름: 한글 5자 이상은 처리할 수 없습니다.
    나이: 0:130
    성별: m, f의 값만 입력 가능
'''
run = True

name = ''
while run:
    name = input("이름 입력 > ")
    if len(name) < 6:
        run = False

run = True
age = 0

while run:
    age = int(input("나이 입력 > "))
    if age >= 0 and age <= 130:
        run = False

run = True
gen = ''

while run:
    gen = input("성별 입력 > ")
    if gen == 'm' and gen == 'f':
        if gender == 'm':
            gen = '남성'
        else: gen = '여성'
        run = False

print("이름:{}, 나이:{}, 성별:{}".format(name, age, gen))
clear(2)
