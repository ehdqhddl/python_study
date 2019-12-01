# Section10
# 에러 및 예외 처리

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일 가이드, 문법 체크


# SyntaxError : 잘못된 문법
# print('Test)
# if True
#   pass

# NameError : 참조변수 없음

# a = 10
# b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러

# print(10/0)

# IndexError : 인덱스 범위 오버
# x = [10,20,30]

# print(x[0])
# print(x[3]) # 예외 발생

# KeyError

# dic = {'Name':'Park', 'Age' : 29, 'City'  : 'Seoul'}

# print(dic.get('hobby')) # 에러 미발생 None 반환
# print(dic['hobby']) # 에러 발생

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

# import time

# print(time.time())
# print(time.month())

# ValueError : 참조 값이 없을 떄 발생

# x = [1,5,6]
# x.remove(10)
# x.index(10)

# FileNotFoundError

# f = open('text.txt','r')

# TypeError

# x = [1,2]
# y = (1,2)
# z = "test"

# print(x + y)
# print(x + z)

# print(x + list(y))

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장 (EAFP 코딩 스타일)



# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행 되는 구문

# 예제 1

name = ['Park','Kim','Lee']

try:
    z = 'Cho'
    x = name.index(z)
    print("{} Found it!".format(z))
except:
    print('Not Found it! - Occured ValueError..')
else:
    print('Ok! else!')

# 예제 2

try:
    z = 'Park'
    x = name.index(z)
    print("{} Found it!".format(z))
except:
    print('Not Found it! - Occured ValueError..')
else:
    print('Ok! else!')
finally:
    print('Uhm, Finally Ok!') 

# 예제 3
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print("Try")
finally:
    print("Ok Finally!")


# 예제 4

try:
    z = 'Park'
    x = name.index(z)
    print("{}(indxe:{}) Found it!".format(z,x+1))
except ValueError:
    print('Not Found it! - Occured ValueError..')
except IndexError:
    print('Not Found it! - Occured IndexError..')
except Exception as e:
    print('Not Found it! - Occured Error..',e)
else:
    print('Ok! else!')
finally:
    print('Uhm, Finally Ok!') 


# 예제 5
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Park':
        print("허가")
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)