import time

def clear(a):
    time.sleep(a)
    print("\n"*100)

def sleep(x):
    time.sleep(x)

'''
while문: 조건문이 거짓일 때 까지 반복, 조건문이 항상 참이면 무한루프, break로 탈출
    > while <...>:
        <...>
'''

###########################################################

line = 1

while line < 6:
    print("===============")
    line += 1
clear(2)

###########################################################

loop = 5
cnt = 0

while cnt < loop:
    print("{} 회전".format(cnt+1))
    cnt += 1
clear(2)

###########################################################

val = 10

while val:
    print(val)
    val -= 1
clear(2)

###########################################################

data = 0
run = True

while run:
    print(data)
    data += 1
    if data == 10:
        run = False
clear(2)

###########################################################

text = ""

print("text 입력기(정지 : stop)")
while text != "stop":
    text = input("input string >>>")
    print(text)
    clear(0)
print("end")
clear(2)

###########################################################

user = 0
run = True

while run:
    user = int(input("1:10 사이의 정수 입력 > "))
    if user > 0 and user < 11:
        run = False
    else:
        clear(0)
        print("1:10인 정수를 입력해주세요.")
print("입력된 값 : {}".format(user))
clear(2)
