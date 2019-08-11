# 2019 08 11
'''
문자열: 문자 여러 개를 조합한 데이터 집합, python에서의 문자 한 개의 크기는 2byte
'''

# 문자열 연산: python에서는 문자열끼리 덧셈, 곱셈이 가능


# +연산: 문자열을 이어줌
word_1 = "Hello,"
word_2 = "World!"
print("word_1 : {}".format(word_1))
print("word_2 : {}".format(word_2))
print("word_1 + word_2 : {}".format(word_1 + word_2))
# word_1 : Hello,
# word_2 : World!
# word_1 + word_2 : Hello,World!
wordsum_1 = word_1 + word_2
print("wordsum_1 : {}".format(wordsum_1))
print()
# wordsum_1 : Hello,World!

# *연산: 문자열을 곱한 수 만큼 출력
hello = "안녕"
print("hello : {}".format(hello))
print("hello * 3 : {}".format(hello * 3))
print()
# hello : 안녕
# hello * 3 : 안녕안녕안녕

# index : 문자열 안의 각 문자에 부여된 번호, 0++ 이지만 뒤에서부터는 -1++
#       > variableName[(int)indexNumber]
data = "abc 한글"
print("data : {}".format(data))
print("index 0, 1, 2 : {}, {}, {}".format(data[0], data[1], data[2]))
print("index 3, 4, 5 : {}, {}, {}".format(data[3], data[4], data[5]))
print()
# data : abc 한글
# index 0, 1, 2 : a, b, c
# index 3, 4, 5 :  , 한, 글
