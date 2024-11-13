
class Subject: #Subject()-> __new__() = new Subject() ->__init__()
    def setGrade(self,grade):
        if grade!=None and (grade < 0 or grade>4.5):
           grade=None
        self.grade = grade
    def __init__(self,number,name,teacher=None,grade=None):
       self.number=number
       self.name=name
       self.teacher=teacher
       self.setGrade(grade)
    def __str__(self):
        return f"[{self.number}] {self.name}"
''''
sub=Subject("CS0001","컴퓨터개론",grade=100.9)
print(sub.grade)
sub=Subject("CS0001","컴퓨터개론",grade=100.9)
sub.setGrade(100.9)
print(sub.grade)
sub=Subject("CS0001","컴퓨터개론")
print(sub.grade)
'''
class Student:
    def totalGrade(self):
        if self.subjects:
            grades=[sub.grade for sub in self.subjects if sub.grade != None]
            if grades:
                return sum(grades)/len(grades)
        else:
            #print("수강과목이 없어요")
            return None #파이썬에서는 return을 넣지 않으면 자동으로 None을 반환
    def __init__(self,number,name,dept,birthyear,*subjects):  #*붙은 것은 가변 매게변수
        self.number=number
        self.name=name
        self.dept=dept
        self.birthyear=birthyear
        if subjects:
            self.subjects=list(subjects) #가변 매게변수로 받는 값은 tuple형
        else:
            self.subjects=list()
        
    def __str__(self):
        return f"[{self.number}] {self.name}"

st = Student("1","임수영","컴정",2024)
print(st)
print(st.totalGrade())

st = Student("2","홍길동","컴정",2024,Subject("001","파이썬","김인하"),Subject("002","자바스크립트","전헤경"))
print(st)
print(st.totalGrade())

st = Student("3","김유신","컴정",2024,Subject("001","파이썬","강인하",grade=4.5),Subject("002","자바스크립트","공진우"), Subject("003","오픈소스","김테간",grade=4.0))
print(st)
print(st.totalGrade())
    
