a="%d%%" % 10
print(a)

#%를 format과 함께 출력하고 싶을때 사용법

print(len("a"))
print(len([1,2]))
print(len((1,2,3)))    #len(lengt)함수는 콜랙트 함수가 가지는 갯수를 출력
#"a".len()
"a".count("a")
#count("a")
test="i am a BOY"
print(test.count("a"))
print(test.count("A"))
print(test.find("a"))

print(test.find("q"))      #find,index가 표시하는 값은 "위치" 값임
print(test.find("am"))
print(test.find("qm"))

print(test.index("a"))
#print(test.index("q"))     #index는 맞는 값을 찾지 못하면 프로그램이 죽어버림
print(test.index("am"))
if "qm" in test:
    print(test.index("qm"))
else:
    print("없다")

print(test.upper())   #문자를 대문자로 변경
print(test.lower())     #문자를 소문자로 변경
print(test.title())      #문자열의 첫 글자들을 대문자로 변경해줌
print(test.capitalize())
print("/".join(test))   #모든 문자 뒤에 /를 붙여줌

print("|"+test.strip()+"|")
print("|"+test.lstrip()+"|")
print("|"+test.rstrip()+"|")

print(test.replace("i am a BOY","High School"))    #문자열 바꾸기 앞은 바꿀 문자열을 작성,뒤는 출력될 문자열을 작성
print(test)

print(test.split())
print(test.split("i"))


