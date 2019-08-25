import time

def clear(a):
    time.sleep(a)
    print("\n"*100)

'''
숫자 입력, 음,양수 확인
'''
num = int(input("input number >"))

if num == 0:
    print("{} 은 0입니다.".format(num))
elif num > 0:
    print("{}의 부호는 + 입니다.".format(num))
else:
    print("{}의 부호는 - 입니다.".format(num))
clear(2)


'''
세 과목의 점수를 입력받고 합격, 불합격을 판단하는 코드 작성
'''
aSub, bSub, cSub = input("세 과목의 점수를 입력하세요. > ").split()
avg = ( int(aSub) + int(bSub) + int(cSub) / 3 )

if int(aSub) >= 40 and int(bSub) >= 40 and int(cSub) >= 40 and avg >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")
clear(2)


'''
비밀번호를 입력받고 정상인지 확인하는 코드 작성
'''
pw = input("비밀번호를 설정해주세요. > ")
clear(0)
print("비밀번호가 설정되었습니다.")
print()

inputPw = input("비밀번호를 입력하세요. > ")

if inputPw == pw:
    print("입력하신 비밀번호와 설정된 비밀번호가 일치합니다.")
else:
    print("입력하신 비밀번호와 설정된 비밀번호가 일치하지 않습니다.")
clear(2)


'''
현금 인출기 코드 작성
출금 조건: 출금액 < 통장 잔액, 10000원 단위
'''

lMoney = int(input("통장 잔액을 입력하세요. >"))
print("통장 잔액은 {}원 입니다.".format(lMoney))
print()
wMoney = int(input("인출 금액을 입력하세요. >"))

if lMoney >= wMoney and wMoney % 10000 == 0:
    lMoney -= wMoney
    print("{}원이 인출되었습니다. 잔고는 {}원 입니다.".format(wMoney, lMoney))
elif lMoney < wMoney:
    print("출금액은 잔액보다 클 수 없습니다.")
elif wMoney % 10000 != 0:
    print("출금액은 10000원 단위여야 합니다.")
clear(1)
