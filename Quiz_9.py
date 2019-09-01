import time
import random

def clear(a):
    time.sleep(a)
    print("\n"*100)

def sleep(x):
    time.sleep(x)

'''
1~100사이의 랜덤 수 10개를 출력하는 코드를 작성하세요
'''
from random import randint

for i in range(1, 11):
    print(randint(1, 100))
clear(2)

'''
a:z 소문자 5개를 출력
'''
for j in range(1, 6):
    rdi2 = randint(ord('a'), ord('z'))
    rdi2 = chr(rdi2)
    print(rdi2)
clear(2)



'''
사용자 고유번호 (숫자, 대문자) 5자리를 생성하는 코드를 작성하세요
'''
usercheck = ''

for cnt in range(5):
    make = randint(1, 2)
    if make == 1:
        usercheck += chr(randint(ord('0'), ord('9')))
    else:
        usercheck += chr(randint(ord('A'), ord('Z')))
print(usercheck)
clear(2)
'''
UpDown게임 구현
컴퓨터에게 1~100 사이의 랜덤값 하나를 부여합니다.
키보드 입력을 통해 컴퓨터가 가진 값을 맞추는 게임입니다.
틀린 값을 입력하면 아래와 같이 힌트를 줍니다.
[up]: 컴퓨터가 가진 값보다 낮은 값을 입력했을 때
[down]: 컴퓨터가 가진 값보다 높은 값을 입력했을 때
'''
run = True
randval = randint(1, 100)

print("UpDown 게임 입니다.")
while run:
    num = int(input("input number > "))
    if num == randval:
        run = False
    elif num > randval:
        print("[DOWN]")
    elif num < randval:
        print("[UP]")
else:
    print("컴퓨터의 값과 입력된 값이 일치합니다.\n게임을 종료합니다.")
clear(2)
