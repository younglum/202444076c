# C반
# 학번 : 202444076
# 이름 :임수영

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        # 기본:타입+인스턴스주소 문자열 반환
        # 재정의 할 때 조건, 무조건 문자열 반환
        # (0,0)
        return f"({self.x},{self.y})"


p = Point()
p = Point(1, 2)
p = Point(x=1)
p = Point(y=1)
print(p.x, p.y)
print(p)
print(1)
print(1.1)
print([1, 2])


class Rectangle:
    def __init__(self, x=0.0, y=0.0, w=0.0, h=0.0):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    # (참고) 현재 사각형의 둘레를 구해서 반환하는 메소드
    def getPerimeter(self):
        return (self.width * 2) + (self.height * 2)

    # (숙제) 현재 사각형의 면적을 구해서 반환하는 메소드를 정의
    # (숙제) 현재 사각형의 LeftTop Point를 Point 자료형으로 만들어 반환하는 메소드를 정의
    # (숙제) 현재 사각형의 RightBottom Point를을 Point 자료형으로 만들어 반환하는 메소드를 정의
    # (숙제) 현재 사각형의 LeftTop Point와 RightBottom Point를 ((0,0), (10,10)) 과 같은 문자열로 반환하는 __str__() 메소드 재정의


def getPerimeter(rect):
    return (r.width * 2) + (r.height * 2)


r = Rectangle(3, 5, 10, 5)
print(getPerimeter(r))
print(r.getPerimeter())
print(r.getArea())
print(r.getLeftTopPoint())
print(r.getRightBottomPoint())
print(r)


class Subject:
    def __init__(self, num, nm, t=None):
        self.number = num
        self.name = nm
        self.teacher = t
        self.grade = None

    # (숙제) 현재 과목의 grade를 비교하여 평가를 반환하는 메소드를 정의
    #        4.5 => "최우수"
    #        4.0 이상 => "우수"
    #        3.5 이상 => "준수"
    #        3.0 이상 => "보통"
    #        3.0 미만 => "노력 필요"
    #        None => "성적 부여전"
    # (숙제) grade를 등록하는 메소드를 정의 (호출 형태는 아래 setGrade() 참고)
    #       단. grade가 0.0 미만이면 0.0으로 grade가 4.5를 초과하는 경우는 4.5로 강제 변환한다.
    # (숙제) 현재 과목의 학수번호와 과목이름을 조합하여 같은 문자열로 반환하는 __str__() 메소드 재정의


# Subject()
Subject("001", "파이선")
Subject("001", "파이선", "이인하")
# Subject('001', '파이선', '이인하', 4.5)

subj = Subject("001", "파이선")
print(subj.getReview())
subj.setGrade(3.5)
print(subj.getReview())
print(subj)


class Student:
    def __init__(self, num, nm, d, by):
        self.name = num
        self.number = num
        self.dept = d
        self.birthyear = by

    # (숙제) 현재 학생의 학번과 이름과 조합하여 같은 문자열로 반환하는 __str__() 메소드 재정의


class Rectangle2:
    def __init__(self, sp=Point(), w=0.0, h=0.0):
        self.width = w
        self.height = h
        self.spoint = sp  # LeftTopPoint

    # (숙제) 현재 사각형의 둘레를 구해서 반환하는 메소드를 정의
    # (숙제) 현재 사각형의 면적을 구해서 반환하는 메소드를 정의
    # (숙제) 현재 사각형의 RightBottom Point를을 Point 자료형으로 만들어 반환하는 메소드를 정의
    # (숙제) 현재 사각형의 LeftTop Point와 RightBottom Point를 ((0,0), (10,10)) 과 같은 문자열로 반환하는 __str__() 메소드 재정의


r = Rectangle2(Point(1, 1), 10, 20)
print(r.getPerimeter())
print(r.getArea())
print(r.getRightBottomPoint())
print(r)


class Rectangle3:
    def __init__(self, sp=Point(), ep=Point()):
        self.spoint = sp  # LeftTop Point
        self.epoint = ep  # RightBottom Point

    # (숙제) 현재 사각형의 둘레를 구해서 반환하는 메소드를 정의
    # (숙제) 현재 사각형의 면적을 구해서 반환하는 메소드를 정의
    # (숙제) 현재 사각형의 너비를 구해서 반환하는 메소드를 정의
    # (숙제) 현재 사각형의 높이를 구해서 반환하는 메소드를 정의
    # (숙제) 현재 사각형의 LeftTop Point와 RightBottom Point를 ((0,0), (10,10)) 과 같은 문자열로 반환하는 __str__() 메소드 재정의


r = Rectangle3()
r.spoint.x = 1
r.spoint.y = 1

r.epoint.x = 10
r.epoint.y = 21

print(r.getPerimeter())
print(r.getArea())
print(r.getWidth())
print(r.getHeight())
print(r)
