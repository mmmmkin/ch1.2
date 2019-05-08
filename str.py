# 한줄 문자열
s = ''
str1 = 'Hello World'
str2 = "Hello World"

print(type(s), type(str1), type(str2))
print(isinstance(str2, str))

# 여러줄 문자열
str3 = """ABC
DEF
가나다라마바사
아자차카타파하"""
print(str3)

# 여러줄 주석 => 여러줄 문자열을 사용한다.
"""ㅁㄴㅇㄹ
ㅁㄴㅇㄹ
ㅁㄴㅇㄹ
"""

# escape
print('hello\nworld\n')
print("I Say \"HelloWorld\"")
print('I Say "HelloWorld"')

# 문자열 연산
str1 = "First String"
str2 = "Second String"
str3 = str1 + '' + str2
print(str3)

str4 = str1 * 3
print(str4)

# 인덱싱
print(str1[0], str1[2], str1[4])

# 슬라이싱(string)
str5 = str2[2:5]
print(str5)
print(str2[2:])

# 연결(+), + 생략가능
str3 = str1 + '' + str2
print(str3)
str6 = 'Hello' '-' 'World'
print(str6)

# 문자열 객체와 정수형 객체는 + 연산을 할 수 없다.
name = '경인'
age = 40
# print(name + age)
print(name + str(age))

# len() 함수 C# 의 length()
print(len(str2))

# in, not in 연산
print("S" in str2)
print("S" not in str2)

# 문자열 객체는 변경할 수 없다. (immutable)
# str1[0] = "f"
# print(str1)

# formating(서식) - tuple
f = "name : %s, age : %d"
print(f)
print(f %('경인', 10))

# formating(서식) - format() 함수
name = "마이콜"
age = 30
print("name =>" + name + "age =>" + str(age))
print("name => " + name + " age => " + format(age,"d"))
print("name => " + format(name, "s") +" age => " + format(age, "d"))

# 대소문자 관련 객체함수
s = "i like Python"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 검색 관련 객체함수
s = "I Like Python, I Like Java Also"
print(s.count("Like"))
print(s.find("Like"))
print(s.find("Like", 5))
print(s.find("JavaScript"))
print(s.rfind("Like"))
