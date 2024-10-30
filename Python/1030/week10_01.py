myfile = "C:\\Users\\PC\\Documents\\202444076\\1030\\lim.txt"

#열기
#f = open(myfile,'w')  #쓰기모드(덮어쓰기)
f = open(myfile,'a')   #기존 파일이 있으면 추가모드

#처리

f.write("임수영\n")
#print(f.read())
#닫기

f.close()








f = open(myfile, 'r')  #읽기 모드
print(f.read())


f.close()
