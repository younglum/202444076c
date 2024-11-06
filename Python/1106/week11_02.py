import datetime

class Test: 
        def __init__(self):#클래스 생성의 기본, self는 매개변수,지역변수
            name="a"    #지역변수
            self.name="b"   #지역변수의 값을 출력하고 싶을 때
            self.age=20
            print(datetime.datetime.now())

t=Test()
print(t.name)

#실행단게
#1번째 : Test() 생성자 호출
#2번쨰 : __new__() 메소드 자동 호출
#            Test의 인스턴스를 생성
#3번째 : __init__()메소드 자동 호출
#            Test의 인스턴스를 초기화
#4번쨰: 생성한 인스턴스의 참조를 반환

t2 = Test()
print(t.name)

t.name="김인하"
t2.name="이인하"

print(id(t),id(t2))
print(type(t)==(type(t2))  #True,같은 Test타입
print(t==t2)    #False,주소값이 다름
print(t.name==t2.name)  #False, name에 들어있는 값이 서로 다름
print(t.age==t2.age)  #True,age에 들어있는 값이 모두 20으로 같음
