
import os

mypath="C:\\Users\\PC\\Documents\\202444076\\1030"
myfile="lim_2.txt:"

if False == os.path.exists(mypath):   #파일이 있는지 확인하는 코드
    os.mkdir(mypath)   #없을 시 해당 경로에 만들어주는 코드
myfullfile= mypath+"\\"+myfile
if os.path.exists(mypath):
    scores=[]
    with open(myfullfile,'r') as f:
        lines = f.readlines()
        for line in lines:
            dict_scores={}
            sub_scores=line.strip().split('|')  #line 안의 문자열을 \n을 무시하고 | 마다 쪼개어 sub_score에 넣음
            for sub_score in sub_scores:
               kv=  sub_score.split(',') #sub_score 안의 문자열을 ,가 나올때마다 쪼개줌
               dict_scores[kv[0]]=int(kv[1])
            if dict_scores:
                scores.append(dict_scores) 
    if scores:
        for score in scores:
            print(score)
else:
    f=open(myfullfile,'w')
    f.close()
