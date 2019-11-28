# Section07-1
# 파이썬 클래스 상세 이해
# self,  클래스, 인스턴스 변수


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