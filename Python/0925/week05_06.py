name=""
flag = True
while True:
    name = input("이름:").strip().lower()
    if name == "lim":
        break
    elif name == "임":
        continue
    else:
        print(name)
