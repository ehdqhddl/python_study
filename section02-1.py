# section02-1
# Print 구문의 이해

# 기본출력

print('Hello Python!')
print('''Hello Python!''')
print("Hello Python!")
print("""Hello Python!""")

print()

# Separator 옵션 사용

print('T','E','S','T', sep = '->') # sep의 값으로 문자를 붙여준다.
print('ehdqhddl91','gmail.com', sep = '@')


# End 옵션 사용

print('Welcome To', end='=>') # 끝 부분을 다음 출력 값과 줄바꿈 없이 붙여준다.
print('the Black Sea.')

# Format 사용

print('{} and {}'.format('You','Me'))
print('{0} and {1} and {0}'.format('You','Me'))
print('{a} and {b}'.format(a='You',b='Me'))

# %s : 문자, %d : 정수, %f : 실수

print("%s's favorite number is %d" % ('JJP',7))

print("Test1: %5d, Price: %4.2f" % (1234567,987654.234))
print("Test1: {0:5d}, Price: {1:4.2f}".format(1234567,9876543.234))
print("Test1: {a:5d}, Price: {b:4.2f}".format(a=1234567,b=9876543.234))

"""
\n : 개행
\t : 탭
\\ : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자

"""