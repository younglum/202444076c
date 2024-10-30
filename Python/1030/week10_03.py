myfile="C:\\Users\\PC\\Documents\\202444076\\1030\\lim_2.txt"

f = open(myfile,'r')

#type1
'''
d=f.read()
print(d)


#type2
while True:
    d=f.readline()  #한줄씩 읽기(\n까지 읽음)
    print(d.strip())  #.strip()= 줄넘김 무시
    if not d:
        break

'''
#type3
d=f.readlines()
for line in d:
    print(line.strip())

f.close()
