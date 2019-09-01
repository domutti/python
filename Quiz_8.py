import time

def clear(a):
    time.sleep(a)
    print("\n"*100)

def sleep(x):
    time.sleep(x)

'''
입력값이 0이 나이면 홀수, 짝수인지를 알려주는 코드를 작성하세요, 0이면 종료됩니다.
'''

run = True

while run:
    age = int(input("inpur ur age >> "))
    if age == 0:
        run = False
    elif age < 0:
        print("나이는 양수여야 합니다.")
    elif age % 2 == 1:
        print("당신의 나이는 {}, 홀수입니다.".format(age))
    else:
        print("당신의 나이는 {}, 짝수입니다.".format(age))
