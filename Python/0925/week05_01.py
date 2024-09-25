class test:
    def __init__(self):
        self.a=1
        self.b=2

test1= [1,2]
test2 =(1,2)
test3=test()

print(test1[0])
print(test2[0])
print(test3.a)
print(test1[1])
print(test2[1])
print(test3.b)

test1[0]=3
#test2[0]=3     tuple은 수정이 불가
test3.a=3
print(test1[0])
print(test2[0])
print(test3.a)
