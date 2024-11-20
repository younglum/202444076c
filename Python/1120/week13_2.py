#id:202444076
#name:limsuyoung

import datetime
from datetime import datetime as dt

#datetime->str->file(text)
#file(text)->str->datetime
'''
%Y  년도
%m  월
%d  일
%H  시간
%M  분
%S   초
%f    마이크로초

'''

parsingFormat=" %Y-%m-%d %H:%M:%S.%f"
d1 = dt.now()
d2=dt.strftime(d1,parsingFormat)#datetime.datetime-> str
d3=dt.strptime(d2,parsingFormat)#str->datetime.datetime, strptime의 p는 parsing.
   
#printf() 의 f는 format

print(type(d2),d2)
print(type(d3),d3)

d4=datetime.datetime(2030,10,2,18,0,2,200)
d5=datetime.datetime(2031,10,3,17,3,3,202)

td=d5-d4
print(type(td),td) #timedelta

print(td.days)
print(td.seconds)
print(td.microseconds)
print(td.total_seconds())
d6=d4+datetime.timedelta(days=29) #기존의 datetime에 값을 더하는 것.
d7=d4+datetime.timedelta(days=-29) #기존의 datetime에 값을 빼는것
print(d6)
print(d7)










