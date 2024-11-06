class Student:
    def __init__(self):
        self.name=" "
        self.number= " "
        self.dept=" "
        self.ppl_number=0

students=[]
for i in range(3):
    stu=Student()
    stu.name=input("이름을 입력하세요. : ")
    stu.number=input("학번을 입력하세요.: ")
    stu.dept=input("학과를 입력하세요 : ")
    stu.ppl_number=int(input("생년월일을 입력하세요: "))
    students.append(stu)

for i in students: #type(i) ==> student, 위에서 students에 넣은  값의 타입이 student이기 때문에
    print(i.name)

#(1) 동일한 학번이 들어오면?
#(2) list가 아닌 dict로 구성하면?
#(3) while로 짠다면 언제 멈출지? 어떻게 멈출지?
