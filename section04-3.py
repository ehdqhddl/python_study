# Section04-3 List 실습
# 리스트의 특징 : 순서O, 중복O, 수정O, 삭제O
# 기존 언어들의 배열과 유사

a = []
b = list()
c = [1,2,3,4]
d = [10,100,'Pen','Apple']
e = [10,100,['Pen','Apple']]

# 인덱싱
print(d[-2])
print(d[2])
print(d[0]+d[1])

print(e[2][1])
print(e[-1][-1])

# 슬라이싱
print(d[0:3])
print(e[2][0:2])


# 연산
print(c + d)
print(c * 3)

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100,1000,10000]
print(c)

c[1] = ['a','b','c']
print(c)

del c[1]
print(c)

print()
print()
print()
print()

# 리스트 함수

y = [5,2,3,1,4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7)
print(y)
y.remove(1)
print(y)
y.pop()
print(y)

ex=[88,77]
y.append(ex) # 인덱스로 추가
y.extend(ex) # 리스트를 이어붙이기
print(y)

# 튜플의 특징 : 순서O, 중복O, 수정X, 삭제X

t1 = ()
t2 = tuple()
t3 = (1,)
t4 = (1,2,3,4)
t5 = (10,100,('a','b','c'))

print(t4[2])
print(t5[2][-1])
print(t4 + t5)

print()
print()

# 튜플 함수
z = (5,2,1,3,1)

print(z)
print(3 in z)
print(z.index(5)) # 해당 값이 있는 인덱스를 반환
print(z.count(1)) # 해당 값이 있는 갯수를 반환