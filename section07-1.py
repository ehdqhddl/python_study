# Section07-1
# 파이썬 클래스 상세 이해
# self,  클래스, 인스턴스 변수

# 예제1
# 선언

class UserInfo:
#   pass 예약어를 사용하면 구현하지 않아도 오류가 나지않음.
#   클래스는 속성과 메소드로 구성
    def __init__(self,name):
        self.name = name
    def user_info_p(self):
        print("Name :",self.name)

user1 = UserInfo("ParkJongJin")
user2 = UserInfo("KimJuEun")

user1.user_info_p()
user2.user_info_p()

# id() 메모리 출력
print(id(user1))
print(id(user2))

# 네임스페이스 출력
print(user1.__dict__)
print(user2.__dict__)


# 예제2
# self의 이해

class SelfTest:
    @staticmethod
    def func1():
        print("func1 called!")
    def func2(self):
        print("func2 called!")

SelfTest.func1()
self_test = SelfTest()
self_test.func2()


# 예제3
# 클래스 변수, 인스턴스 변수
# 클래스 변수 = java의 static 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self,name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Park')
user2 = WareHouse('Kim')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스

# 예제4
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(B,A,Z):
    pass


print(M.mro())