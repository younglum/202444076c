socnum = input("주민등록번호:")

a = "-"in socnum
b="-"not in socnum

if b==True:
    index = 6
else:
    index=7

gender = int(socnum[index])%2

if gender == 0:
    msg="여성"
elif gender == 1:
    msg="남성"
else:
    msg="지구인이 아님"

print(f"성별 : {msg}")
