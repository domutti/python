#2019 08 24
'''
제어문
    - 프로그램은 위에서부터 코드를 읽어서 실행된다. 제어문은 이 흐름을 변경할 때 사용한다.
    - 제어문의 조건식이 있는 다음 라인에서는 들여쓰기를 사용하여 해당 코드가 제어문에 종속되어 있음을 표기
    - 제어문의 끝에는 ':' 기호를 붙임
'''


'''
if: 조건식이 참일 경우에 실행코드가 실행됨, 조건식이 거짓일 경우에는 if문을 빠져나옴
    > if <조건식> : 
        <실행코드>
'''

money = 1000

print("money: {}".format(money))
if money >= 2000:
    print("당신의 돈은 2000보다 많습니다.")
else:
    print("당신의 돈은 2000보다 작습니다.")
print()

value = int(input("input num > "))

if value % 2 == 1:
    print("{} : 홀수".format(value))
elif value % 2 == 0:
    print("{} : 짝수".format(value))
print()

cash = 1000

print("cash : {}".format(cash))
if cash >= 720:
    print("cash >= 720")
    cash -= 720
    print("잔고: {}".format(cash))
else:
    print("cash < 720")
print()

data = int(input("정수 입력 > "))

print("data : {}".format(data))
if data > 0 and data < 11:
    print("데이터는 10 이하의 자연수 입니다.")
elif data >= 0:
    print("data는 양수입니다.")
elif data < 0:
    print("data는 음수입니다.")
else:
    print("data가 int의 범위에 속하지 않습니다.")
print()


word = "python"

search = input("검색 문자 입력 > ")
print()
print("string : {}".format(search), end = ', ')
if word in search:
    print("python이 검색어에 포함되어 있습니다.")
else:
    print("python이 검색어에 포함되지 않았습니다.")
