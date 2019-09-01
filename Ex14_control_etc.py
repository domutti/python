import time

def clear(a):
    time.sleep(a)
    print("\n"*100)

def sleep(x):
    time.sleep(x)

'''
기타 제어문

break: 반복문 탈출
    > 반복문 실행 중에 사용자가 원할 때 반복문 종료, 다중반복문 에서는 가장 하위 제어문만 탈출
'''

cnt = 0

while True:
    if cnt == 3:
        print("종료")
        break
    print(cnt)
    cnt += 1
clear(2)


i = 0

for i in range(1, 11):
    if i == 7:
        print("seven")
        break
    print(i)
clear(2)


########################################################################################################################################
'''
continue: 반복문 실행 중에 조건식으로 이동해서 다음의 반복을 시행
'''

cout = 0

while cout < 11:
    cout += 1
    if cout == 7:
        print("seven")
        continue
    print(cout)
clear(2)


########################################################################################################################################
'''
while-else, for-else: 반복문이 정상 종료될 때 else의 하위코드를 시행
'''
run = True

while run:
    text = input("input string >> ")
    if text == 'stop':
        run = False
    print(text)
else:
    print("end")
clear(2)

nums = [1, 3, 5, 7]
n = 0

for n in nums:
    if n % 2 == 0:
        print(n)
else: 
    print("홀수")
