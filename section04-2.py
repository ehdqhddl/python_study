# Section04-2 문자열 실습
# 문자열, 문자열연산, 슬라이싱

str1 = "I am a boy!"
str2 = 'Nice man!'
str3 = ''
str4 = str(123)
str5 = str()

print(len(str1), len(str2), len(str3), len(str4), len(str5))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)

escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
raw_s2 = r"\\a\\a"

print(raw_s1)
print(raw_s2)

# Multiline
# 변수 다음 \ 기호가 나오면 문자열이 이어진다는 의미

multi = \
"""
문자열 
 
멀티라인

테스트 
"""

print(multi)

# String Cal

str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "NiceMan"

print(str_o1 * 100)
print(str_o2 * 100)
print('a' in str_o4)
print('z' not in str_o4)

#문자열 형 변환

print(str(777) + 'a')
print(str(10.5))

#문자열 함수

# a = 'niceman'
# b = 'orange'

# print(b.endswith('e'))
# print(a.capitalize())
# print(a.replace('nice','good'))
# print((list(reversed(b))))

a = 'niceman'
b = 'orange'

print(a[0:])
print(a[:])

print(b[0:4:2])
print(b[1:-2])
print(b[::-1])