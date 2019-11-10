# Section04-4 딕셔너리, 집합 실습

# 딕셔너리(Dict) : 순서X, 중복X, 수정O, 삭제O
# Key와 Value로 구성

a = {'name': 'Kim', 'Phone' : '010-1234-1234', 'birth' : 910101}
b = {0: 'Hello Python',1: 'Hello Java'}
c = {'arr':[1,2,3,4,5]}

print(type(a))

# 출력테스트

print(a['name'])
print(a.get('age'))
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1,3,4]
a['rank2'] = (10,100,300)
print(a)

# keys, values, items
print(a.keys())
print(list(a.keys())[1:3])
print(a.values())
print(a.items())
print(1 in b)


# 집합
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

print(s1.difference(s2))
print(s1 - s2)

# 추가 & 제거
s3 = set([7, 8, 10, 15])
s3.add(19)
print(s3)

s3.remove(19)
print(s3)