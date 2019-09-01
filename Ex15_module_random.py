import time
import random

def clear(a):
    time.sleep(a)
    print("\n"*100)

def sleep(x):
    time.sleep(x)

'''
module (library): 비슷한 기능을 가진 함수들을 정의해 놓은 파일(*.py)
모듈을 사용하기 위해서는 모듈을 불러와야함
    > import <module>
    ex> import time
모듈에 포함되어있는 변수, 함수를 사용할 때에는 모듈명.함수명 을 사용합니다
    > <module>.<function, variable, ...>
    ex> time.sleep()
모듈명 변경
    > import <module> as <add..>
함수 불러오기
    > from <module> import <function>
    > from <module> import * - 모든 변수, 함수, 클래스 불러옴
    # 컴퓨터에서는 일반적으로 '*'기호를 모든 것이라는 뜻으로 사용
'''
print(random.random())


'''
random: 난수 생성 기능을 가진 모듈

random(): 0~1 사이의 난수 실수를 생성
범위지정: int(random() * 숫자의 개수) + 시작 수
'''
from random import random
rd = random()
print(rd)

rd_1 = random() * 10
print(rd_1)

rd_2 = int(rd_1 * 10)
print(rd_2)

'''
randint()
- 지정한 범위 안에서 난수 정수를 생성
    > randint(a, b)
'''
from random import randint
rdi = randint(1, 190000)
print(rdi)

rdi2 = randint(ord('A'), ord('Z'))
rdi2 = chr(rdi2)
print(rdi2)

'''
randrange(a, b, c)
시작, 종료, 증가값
    :시작부터 증가값만큼 증가시키면서 종료(-1)값사이의 정수 난수 생성
'''
from random import randrange
rr = randrange(1, 11, 2) # 1:11 미만까지 2씩 증가된 범위 안의 정수 난수
print(rr)
