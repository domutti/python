#2019 08 25

import time

def clear(a):
    time.sleep(a)
    print("\n"*100)

'''
다중if: 어떠한 조건의 결과를 다시 세분화 할 때 사용
    > if <...>:
        if <...>:
            // 둘 다 참일 때 실행
        else:
            // 최상위 if는 참, 차상위 if는 거짓일 때 실행
'''

data = int(input("input number >"))
print("data : {}".format(data))

if data >= 0:
    print(" +: ",end = ' ')
    if data % 2 == 1:
        print ("홀수")
    else:
        print("짝수")
else:
    print("- : ",end = ' ')
    if data % 2 == 1:
        print("홀수")
    else:
        print("짝수")
clear(2)

setID = input("ID 입력 > ")
setPW = input("PW 입력 > ")
clear(0)
print("ID, PW 입력 완료")
print()
userID = input("ID 입력 > ")
userPW = input("PW 입력 > ")

if setID == userID and setPW == userPW:
    print("{}님이 로그인 하셨습니다.".format(userID))
elif setID != userID:
    print("ID가 틀렸습니다.")
elif setPW != userPW:
    print("PW가 틀렸습니다.")
clear(2)
