# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r , 쓰기 모드(기존 파일 삭제) : w, 추가모드(파일 생성 또는 추가) : a
# .. : 상대경로 / . : 절대경로


# 파일 읽기
# 예제 1

f = open("./resource/review.txt","r")

content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()

print("-----------------------------")
print("-----------------------------")

# 예제 2

with open("./resource/review.txt","r") as f:
    c = f.read()
    print(c) # 리스트로 형변환 가능
    print(iter(c))

print("-----------------------------")
print("-----------------------------")

# 예제 3

with open("./resource/review.txt","r") as f:
    for c in f:
        print(c.strip())
print("-----------------------------")
print("-----------------------------")


# 예제 4

with open("./resource/review.txt","r") as f:
    content = f.read()
    print('>',content)
    content = f.read() # EOF 
    print('>',content) 

print("-----------------------------")
print("-----------------------------")

# 예제 5

with open("./resource/review.txt","r") as f:
    line = f.readline()

    while line:
        print(line, end='>>')
        line = f.readline()

print("-----------------------------")
print("-----------------------------")

# 예제 6

with open("./resource/review.txt","r") as f:
    contents = f.readlines()
    print(contents)

    for c in contents:
        print(c,end='####')

print()
print("-----------------------------")
print("-----------------------------")

# 예제 7

score = []
with open("./resource/score.txt","r") as s:    
    for line in s:
        score.append(int(line))
print("Average : {:6.3}".format(sum(score)/len(score)))


# 파일 쓰기
# 예제 1

with open("./resource/text1.txt","w") as f:
    f.write("Niceman!\n")

# 예제 2

with open("./resource/text1.txt","a") as f:
    f.write("Goodman!\n")

# 예제 3

from random import randint

with open("./resource/text2.txt","w") as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제 4
# writelines : 리스트 -> 파일로 저장

with open("./resource/text3.txt","w") as f:
    list = ['Park\n','Kim\n','Choi\n']
    f.writelines(list)


# 예제 5
# 파일로 로그찍기 용도

with open("./resource/text4.txt","w") as f:
    print("Test Contents1", file=f)
    print("Test Contents2", file=f)
