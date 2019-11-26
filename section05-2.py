# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습


# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is",v1)
    v1 += 1

print()

for v2 in range(10):
    print("v2 is",v2)

print()

for v3 in range(1,11):
    print("v3 is",v3)

# 1 ~ 100합

sum0 = 0
for v4 in range(1,101):
    sum0 += v4
print(sum0)

print('1 ~ 100 : ', sum(range(1,101)))
print('1 ~ 100 (짝수 합) : ', sum(range(1,101,2))) # 시작, 끝, 단위(공차)

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전

names = ["Kim","Park","Cho","Yoo","Choi"]

for name in names:
    print(name)

word = "dreams"

for s in word:
    print("Word : ", s)

my_info = {
    "name" : "Park",
    "age"  : 29,
    "city" : "Seoul"
}

# 기본 값은 키

for key in my_info:
    print("my_info_defalut : ",key)

for key in my_info.values():
    print("my_info_value : ",key)

for key in my_info.keys():
    print("my_info_key : ",key)

for key,val in my_info.items():
    print("my_info_dict : ",key,val)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())


# break
numbers = [13,3,4,5,6,7,20,24,38,9,19,22,19,100]

# for - else

for num in numbers:
    if num == 400:
        print("Found 400")
        break
    else:
        print("Not found 400")
else:
    print("The list has not 400")

# continue

lt = ["1",2,5,True,4.3,complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입 : ",type(v))


name = "ParkJongjin"

print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))