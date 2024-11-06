class Point:
    def __init__(self,x=0.0,y=0.0):  #x,y에 값이 들어오면 들어온 값으로, 아니면 0.0(기본값)으로
        self.x=x
        self.y=y
    def __str__(self):
        #출력을 재정의 할 때 사용
        #기본: 타입+인스턴스 주소 문자열 반환
        #재정의 할때 조건,무조건 문자열로 반환해야함
        #(0.0)
        return f"x:{self.x},y:{self.y}"



p=Point()
p=Point(1,2)
p=Point(x=1)
p=Point(y=2)
print(p.x,p.y)
print(p) #출력시 p의 타입과 p의 주소를 출력함
print(1)
print(1.1)  #print는 "문자"또는 "문자열"을 출력함. 즉 지금 출력되는 1과 1.1은 "문자"형태다


class Rectangle:
    def __init__(self,x=0.0,y=0.0,w=0.0,h=0.0):
        self.x=x
        self.y=y
        self.width=w
        self.height=h
    #현재 사각형의 둘레를 구해서 반환하는 메소드
    def getRoundlength(self):
        return (self.width*2)+(self.height*2)

r=Rectangle(3,5,10,5)
print(r.getRoundlength())
class Subject:
    def __init__(self,num,nm,t=None,g=None):
        self.grade=g
        self.students=nm
        self.number=num
        self.teacher=t

Subject('001','파이선')
Subject('001','파이선','이인하')

class Student:
    def __init__(self,nm,num,dt,ppl_num):
        self.name=nm
        self.number=num
        self.dept=dt
        self.ppl_number=ppl_num

class Rectangle2:
    def __init__(self,sp=Point(),w=0.0,h=0.0):
        self.start_point=sp
        self.widht=w
        self.height=h

class Rectangle3:
    def __init__(self,sp=Point(),ep=Point()):
        self.spoint=sp
        self.epoint=ep

r=Rectangle3()
r.spoint.x=1
r.spoint.y=1
r.epoint.x=10
r.epoint.y=21

print(p)

