
data2=[[1,2,3],[10,20],[11,12,13,14]]
data3={"김인하":[1,2],"이인하":[10,20,30,40,50,60,70],"송인하":[11,12,13,14]}

def print_info(datas):
    for j,y in enumerate(datas):
        print(f"[{j}] {y}",end="")
    print()
    print("sum",sum(datas))
    print("max",max(datas))
    print("min", min(datas))
    print("avg",sum(datas)/len(datas))

def analyze_list(datas):
    for i ,c in enumerate(datas):
        print(f"{i+1}번째 :",end="")
        print_info(c)

def analyze_dict(datas):
    for k,i in enumerate(datas):
        print(f"{i} : ",end="")
        print_info(datas[i])

def analyze_score(datas):
    if isinstance(datas, list):
        analyze_list(datas)
    elif isinstance(datas,dict):
        analyze_dict(datas)
    else:
        print("분석불가")



analyze_score(data2)
analyze_score(data3)

"""
OS, DS 중요
stackoverflow = os에서 할당해준 스택의 용량을 초과하여 발생하는 에러






    
