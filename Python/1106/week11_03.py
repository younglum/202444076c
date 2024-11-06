class Point:
    def __init__(self):
        self.x=0.0
        self.y=0.0



p=Point()
print(p.x,p.y)


class Rectangle:
    def __init__(self):
        self.x=0.0
        self.y=0.0
        self.width=0.0
        self.height=0.0

class Subject:
    def __init__(self):
        self.grade=0.0
        self.students=" "
        self.number=" "
        self.teacher=" "

class Student:
    def __init__(self):
        self.name=" "
        self.number= " "
        self.dept=" "
        self.ppl_number=0

class Rectangle2:
    def __init__(self):
        self.start_point=Point()
        self.widht=0.0
        self.height=0.0

class Rectangle3:
    def __init__(self):
        self.spoint=Point()
        self.epoint=Point()

r=Rectangle3()
r.spoint.x=1
r.spoint.y=1
r.epoint.x=10
r.epoint.y=21

