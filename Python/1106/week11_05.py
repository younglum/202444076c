class Test:
    def __init__(self):
        self.name=None
        self.age=None
        
    def func(self,name,age):
        self.name=name
        print(age)

t=Test()
print(t.name)     #__init__은 생성자를 한번이라도 사용했다면 그 생성자를 저장해둠
print(t.age)
t.func("김인하",20)
print(t.name)
print(t.age)

print("-"*30)



class In:
    def func(self):
        print("In.func()")

class Out:
    def  method(self):
        print("Out.method()")

#안되면 주석
#method()
#func()

#Out.method()
#In.func()

i=In()        #i는 In이 만든 인스턴스를 의미함
o=Out()    #반드시 인스턴스를 만들고 함수를 불러와야함

Out.method(o)
In.func(i)

#실제로는 이걸 많이 사용함
o.method()
i.func()


#작동하긴 하지만 정상적으로 되지 않을 가능성이 큼
In.func(o)
Out.method(i)

#아예 실행되지 않음
#o.func()
#i.method()
