# Section06-1 
# 파이썬 함수식 및 람다 실습

# 함수 정의 방법
# def function_name(parameter):
#   code

# 함수호출
# function_name(parameter)

# 함수 선언 위치 중요

# 예제1

def hello(world):
    print("Hello",world)

hello("Python")
hello("Java")

# 예제2

def hello_return(world):
    val = "Hello " + str(world)
    return val

print(hello_return("Python!"))

# 예제3(다중리턴)

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1,y2,y3

val1, val2, val3 = func_mul(100)
print(val1,val2,val3)


def func_mul_lt(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1,y2,y3]
lt = []
lt = func_mul_lt(100)
print(type(lt))

# 예제4 *args(어떤 매개변수가 들어올지 모를때, 갯수가 가변적일 경우, 튜플로 받음), *kwargs

def args_func(*args):
    for i,v in enumerate(args): #enumerate 인덱스를 만들어줌
        print(i,v)

args_func('kim')
args_func('kim','park')

# kwargs

def kwargs_func(**kwargs):
    #print(kwargs)
    for k,v in kwargs.items():
        print(k,v)


kwargs_func(name1='Kim',name2='Park',name3='Choi')


# 전체 혼합

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1,arg2,args,kwargs)


example_mul(10,20)
example_mul(10,20,'park','lee',age1=29,age2=30)

# 예제 5
# 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

# 예제 6

def func_mul_new(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1,y2,y3]

print(func_mul_new(5.0))


# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) ->  메모리 초기화

# 일반적 함수 -> 변수 할당

def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)

lambda_mul_10 = lambda num: num * 10

print(lambda_mul_10(10))

def func_final(x, y, func):
    print(x*y*func(10))

func_final(10,10,lambda_mul_10)

func_final(10,10,lambda x: x * 1000)