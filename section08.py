# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대경로


# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("Ex1 : ",Fibonacci.fib2(400))
print("Ex1 Title: ", Fibonacci().title)

# 사용2 (클래스 / 권장 X)

from pkg.fibonacci import * # 리소스낭비 이기에 권장하지 않음

Fibonacci.fib(500)

print("Ex2 : ",Fibonacci.fib2(500))
print("Ex2 Title: ", Fibonacci().title)

# 사용3 (클래스 / alias / 권장 O)

from pkg.fibonacci import Fibonacci as fb

fb.fib(500)

print("Ex3 : ",fb.fib2(500))
print("Ex3 Title: ", fb().title)

# 사용4 (함수)

import pkg.calculations as cal

print("Ex4 add:",cal.add(10,100))
print("Ex4 mul:",cal.mul(10,100))

# 사용5 (함수)

from pkg.calculations import div as d

print("Ex5 div:",d(10,100))

# 사용6 (출력)

import pkg.prints as p  
import builtins

p.prt1()
p.prt2()

print(dir(builtins))