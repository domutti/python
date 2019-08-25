#2019 08 25

import time

def clear(a):
    time.sleep(a)
    print("\n"*100)


'''
나이를 입력받아서 성인, 미성년자를 확인
    성인일 경우 청년층 (20:39), 중장년층(40:)으로 분류
    미성년자일 경우 청소년(14:19), 어린이(:13)으로 분류
'''
urAge = int(input("나이를 입력해주세요. > "))
clear(0)
ageParam = 0

if urAge < 20:
    if urAge < 13:
        ageParam = "어린이"
    else:
        ageParam = "청소년"
if urAge >= 20:
    if urAge < 40:
        ageParam = "청년층"
    else:
        ageParam = "중장년"
print("당신의 나이는 {}, {}입니다.".format(urAge, ageParam))
clear(2)


'''
물품의 크기와 무게를 입력받아서 사용 할 수 있는 카트를 확인
크기    무게    종류
small   <50kg   cart -1
small  >=50kg   cart -2
big     <50kg   cart -3
big    >=50kg   cart -4
'''
size, weight = input("크기와 무게를 입력해주세요. > ").split()
cartSTAT = 0

if int(weight) < 50:
    if size == "small":
        cartSTAT = 1
    elif size == "big":
        cartSTAT = 3
    else:
        print("물품의 크기는 \"small\" 또는 \"big\"이여야 합니다.")
elif int(weight) >= 50:
    if size == "small":
        cartSTAT = 2
    elif size == "big":
        cartSTAT = 4
    else:
        print("물품의 크기는 \"small\" 또는 \"big\"이여야 합니다.")
print("물품의 크기는 \"{}\" 이고, 무게는 {}kg이며, 사용하실 수 있는 카트는 cart - {} 입니다.".format(size, weight, cartSTAT))
clear(2)



'''
다이아몬드 개수(10개 단위)에 따라서 상점에서 구매할 수 있는 아이템 목록을 출력
아이템      다이아
목검        5
일반물약    7
불의검      15
빨간물약    17
방어막      25
'''
def switch(a):
    return{
        0: "",
        1: "목검",
        2: "목검, 일반물약",
        3: "목검, 일반묵약, 불의검",
        4: "목검, 일반물약, 불의검, 빨간물약",
        5: "목검, 일반물약, 불의검, 빨간물약, 방어막",
    }.get(a, "ERROR")

urDia = int(input("보유하신 다이아몬드의 개수를 입력하세요. > "))
canITEM = 0
if urDia < 5:
    canITEM = switch(0)
elif urDia >= 5 and urDia < 7:
    canITEM = switch(1)
elif urDia >= 7 and urDia < 15:
    canITEM = switch(2)
elif urDia >= 15 and urDia < 17:
    canITEM = switch(3)
elif urDia >= 17 and urDia < 25:
    canITEM = switch(4)
elif urDia >= 25:
    canITEM = switch(5)
print("{}개의 다이아몬드로 살 수 있는 아이템은 {} 입니다.".format(urDia, canITEM))
clear(2)
