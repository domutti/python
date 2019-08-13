'''
아이디를 입력받아서, 입력받은 아이디로 email 주소를 생성해서 출력하세요
'''
id = input("아이디 입력 >")
print("E-mail : {}@gmail.com".format(id))
print()


'''
이름, 나이, 전화번호를 입력받아서 출력하세요
'''
name = input("이름을 입력하세요 > ")
age = input("{}님의 나이를 입력하세요 > ".format(name))
phoneNum = input("{}님의 전화번호를 입력하세요 > ".format(name))
print("당신의 이름은 {}, {} 세, 전화번호는 {} 입니다.".format(name, age, phoneNum))
print()


'''
태어난 년도를 입력받아서 나이를 계산하는 코드를 작성하세요
'''
presentYear = int(input("현재 년도 입력 > "))
birthYear = int(input("태어난 년도 입력 > "))
urAge = presentYear - birthYear + 1
print("당신의 나이는 {} 세 입니다.".format(urAge))
print()


'''
C언어, java, python 세과목의 점수를 입력받으세요
세과목의 총점과 평균을 구해서 출력하세요
- 평균은 소수점 첫째자리까지 출력하세요
'''
cScore, jScore, pScore = input("C언어, java, python 세 과목의 점수를 입력하세요 > ").split()
sumScore = int(cScore) + int(jScore) + int(pScore)
avgScore = sumScore / 3
print("C언어 점수: {}, java 점수: {}, python 점수: {} 이며,\n총점은 {} 점, 평균은 {:.1f} 점 입니다.".format(cScore, jScore, pScore, sumScore, float(avgScore)))
print()
