#id:202444076
#name:limsuyoung

import datetime
from datetime import datetime as dt
#모듈,class,메소드 순
d1=datetime.datetime.now()
#class,메소드 순
d2=dt.now()

print(type(d1),d1)
print(type(d2),d2)

print(d2.year) #년도
print(d2.month) #월
print(d2.day) #일
print(d2.hour) #시간
print(d2.minute) #분
print(d2.second) #초
print(d2.microsecond) #마이크로초
print('-'*20)

print(d2.weekday())  #요일을 숫자로 바꿔 출력 예시: 월요일=0?

print(d2.date(),type(d2.date()))
print(d2.time(),type(d2.time()))
