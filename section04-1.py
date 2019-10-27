# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "GoodBoy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Park",
    "age" : 29
}
v_list = [1,2,4] # 배열의 개념
v_tuple = 3,5,7
v_set = {7,8,9}

print(type(v_dict))
print(type(v_set))
print(type(v_tuple))
print(type(v_bool))
print(type(v_int))
print(type(v_list))


i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999999999999999999999999
big_int2 = 7777777777777777777777777777777777777777777777777777777
f1 = 1.234
f2 = 9.873
f3 = .5
f4 = 10.

print(big_int1 * big_int2)
print(f1 ** f2)
print(f4+i2)

a = 5.
b = 4

print(type(a),type(b))

result2 = a+b

print(result2)

# 형변환

print(int(result2))
print(result2)


y = 100
y += 100

# 수치 연산 함수

print(abs(-7))

n,m = divmod(100,8) # 몫과 나머지
print(n,m)

import math

print(math.ceil(5.1))
print(math.floor(3.874))
