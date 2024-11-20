#id:202444076
#name: limsuyoung

book=[]
while True:
    bookcode=input("도서번호: ").strip()
    if bookcode=="": #if not bookcode
        break
    borrow_time=input("빌린 시간: ")
    return_time=input("반납시간: ")
    diec={"bookcode": bookcode,"borrow_time":borrow_time,"return_time":return_time}
    book.append(diec)

for books in book:
    print(books["bookcode"],books["borrow_time"],books["return_time"])

    
