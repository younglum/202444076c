data1=[1,2,3,4]
'''
summary=sum(data1)
maximum=max(data1)
minimun=min(data1)
average=sum(data1)/4  #summary/len(data1)

print(summary)
print(maximum)
print(minimun)
print(average)

print("*"*30)

for i in data1:    #리스트의 값만 필요할 경우
    print(i)

print("*" * 30)

for i in range(len(data1)):    #index 사용,  값을 제어할 때 주로 사용
    print(i+1)

print("*" *30)
'''
for i in range(len(data1)):
    print(f'data1[{i}]:{data1[i]}')   #F-스트링 복습필요, inumalate는 여러개의 값을 처리할 때는 불편

print("*"*30)

#for i ,f in enumerate(data1):    #enumerate가 뽑는 값은 tuple, 학습 필요
    #print(f"data1[{f[0]}]:{f[1]}")

#for i ,f in enumerate(data1):    #enumerate가 뽑는 값은 tuple, 학습 필요
    #print(f"data1[{i}]:{f}")

data2=[[1,2,3],[10,20],[11,12,13,14]]

for i in data2:
    print(i)

print("*"*30)

for i in data2:
    print("sum",sum(i))
    print("max",max(i))
    print("min", min(i))
    print("avg",sum(i)/len(i))

print("*"*30)

for i ,c in enumerate(data2):
    print(f"{i+1}번째: {c}")
    print("sum",sum(c))
    print("max",max(c))
    print("min", min(c))
    print("avg",sum(c)/len(c))

print("*"*30)


for i ,c in enumerate(data2):
    print(f"{i+1}번째 :",end="")
    for j,y in enumerate(c):
        print(f"[{j}] {y}",end="")
    print()
    print("sum",sum(c))
    print("max",max(c))
    print("min", min(c))
    print("avg",sum(c)/len(c))

print("*"*30)

data3={"김인하":[1,2],"이인하":[10,20,30,40,50,60,70],"송인하":[11,12,13,14]}

for k in data3:  #data3.keys()와 동일, data3에 들어있는 key값만 출력
    print(k)

print("*"*30)

for k in data3:
    print(data3[k])

print("*"*30)

for k in data3:
    print(f"{k} : {data3[k]}")

print("*"*30)

for k,i in enumerate(data3):
    print(f"{i} : ",end="")
    for j ,l in enumerate(i):
        print(f"[{j}]{l}",end="")
    print()
    print("sum" ,sum(data3[k])
    print("max" ,max(data3[k])
    print("min" ,min(data3[k])
    print("avg", sum(data3[k])/len(data3[k])







    
