'''
2019 08 10
주석: '#' 기호 사용 - 프로그램 코드 안에 설명을 달아줄 때 사용
프로그램 실행에는 영향을 주지 않음
외따옴표, 쌍따옴표를 세 번 작성하여 여러 줄 주석 사용

프로그램 실행
1. coderunner: Ctrl + <Alt> + n
   or
   Ctrl + F5 

실행 터미널 설정
1. Debug 아이콘
2. vscode 내장 터미널 이용: Python: Current File (Integrated Terminal)
   or
   외부(windows) 터미널 이용: Python: Current File (External Terminal)
'''

###########################################################

'''
출력 함수: print() - ()안의 문자열, 정수, 실수 등의 데이터를 터미널에 출력
여러 개의 데이터 형태를 출력 할 시에는 ','를 사용
'''

print("\" \"를 이용하여 문자열 출력")
print('\' \'를 이용하여 문자열 출력')

###########################################################

'''
Escape 문자 (\ 사용)
문자열 출력시 기능을 수행
'''

#\n: 개행
print("\n\\n: 개행 후 출력")
#\t: 들여쓰기 만큼 이동(tab)
print("\t\\t: 들여쓰기 후 출력")
#\': ' 출력
#\": " 출력
#\\: \ 출력
print("\\\': \' 출력, \\\": \" 출력, \\\\: \\ 출력")

###########################################################

'''
print 함수 옵션: print(*, sep=value)
> 쉼표 위치에 sep 값을 출력, 초기값: " "
'''

print("1", "2", "3")
print("1", "2", "3", sep=',')
print("1", "2", "3", sep='-')

###########################################################

'''
print 함수는 자동으로 개행을 해주는 두 번째 인자가 생략되어 있음
    print(*, end='\n')
개행을 원하지 않을 때에는 sys module import 후 sys.stdout.write() 함수 사용
ex) sys import
    sys.stdout.write(1)
    sys.stdout.write(2)
    sys.stdout.write(3)
or
end value를 ' '로 사용
ex) print(1, end=' ')
    print(2, end=' ')
    print(3, end=' ')
print(*, end=value)
> print 함수의 끝을 지정할 수 있음, 초기값: '\n'
'''
print(1, end=' ')
print(2, end=' ')
print(3)
print(2019, end=' - ')
print('08', end=' - ')
print(10)

