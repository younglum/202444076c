# week02_04.py

decimal = int(13)  #10진수
binary= int(0b1101)   #2진수
octal = int(0o15)      #8진수
hexadecimal=int(0xD)    #16진수
print(decimal, binary, octal, hexadecimal)

a =int(5)
b=int(2)
c=float(2.4)
add = a+b
sub=b-c
print(add,sub)

mul1=a*b
mul2=a*c
print(mul1,mul2)
print("*" *20)

div1 = a/b  #5/2=2.5 알맞게 나온다.
div2=a//b   #5/2에서 정수인 2만 나온다.
div3=a%b
div4=c/b
div5=c//b
div6=c%b
print(div1,div2,div3)
print(div4,div5,div6)

sqr1 =a**b  # **은 제곱 함수 5의 2제곱 = 25
sqr2=b**c
print(sqr1,sqr2)
print("*" *20)
