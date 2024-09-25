for i in range(10):
    print(i,end=" ")


print()
for i in range(1,10):
    print(i,end=" ")

print()
for i in range(1,10,2):
    print(i,end=" ")

print()
for i in range(10,1,-2):  #10에서 1까지 2씩 줄어듬
    print(i,end=" ")

print()
a=range(10)
print(a,type(a))  #range타입. a에 "range(1,10)이 들어감
b=list(a)
print(b,type(b))  #list 타입. a를 실행한 결과값이 B에 들어감

