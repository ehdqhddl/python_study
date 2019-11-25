#Section05-1
#조건문 실습

print(type(True))
print(type(False))

# 기본 형식

# 예제1번
if True:
    print("Yes")


if False:
    #출력되지 않음.
    print("No")

# 예제2번
if False:
    #출력되지 않음.
    print("You can't reach here")
else:
    print("You are here")


#관계연산자

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

#참,거짓 종류
#참: "내용",[내용],(내용),{내용},1,True
#거짓: "",[],(),{},0,False

city = ""

if city:
    print("This is True")
else:
    print("This is False")

#논리연산자
#and or not

a = 100
b = 90
c = 15

print('and : ', a > b and b > c) # a > b > c
print('or : ', a >b or b < c)
print('not : ', not a > b)
print('not : ', not b > c)
print(not True)
print(not False)


# 산술,관계,논리 우선순위
# 산술 > 관계 > 논리 순서로 적용

print('ex1: ', 3 + 12 > 7 + 3)
print('ex2: ', 5 + 10 * 3 > 7 + 3 == 10)
print('ex3: ', 5 + 10 > 3 and 7 + 3 == 10)
print('ex4: ', 5 + 10 > 0 and not 7 + 3 == 10)


score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일경우에 실행

if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다.")
else: 
    print("불합격하셨습니다.")


# 다중조건문

num = 90
if num >= 70:
    print("num ?",num)
elif num >= 60:
    print("num ?",num)
elif num >=40:
    print("num ?",num)
else:
    print("defalut num ",num)

# 중첩 조건문

age = 29
height = 175

if age >= 20:
    if height >= 170:
        print("A지망 지원가능")
    elif height >= 160:
        print("B지망 지원가능")
    else:
        print("지원 불가능")
else:
    print("20세 이상만 가능")

# in, not in

q = [1, 2, 3]
w = {7, 8, 9, 9}
e = {"name": 'Kim', "city": "seoul", "grade": "B"}
r = (10, 12, 14)


print(1 in q)
print(6 in w)
print(12 not in r)
print("name" in e) # key 검색
print("seoul" in e.values()) # value 검색