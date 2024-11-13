import week12_06 as m
from week12_06 import PI  #week12_06파일의 PI를 따로 불러와 사용
from week12_06 import PI as pi  #week12_06파일의 PI를 따로 불러와 pi로 정의

print(m.PI)
print(PI)
print(pi)
print(m.add(m.PI,4.4))
obj=m.Math()
print(obj.solv(2))
