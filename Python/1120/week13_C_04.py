#id:202444076
#name: limsuyoung

import datetime
from datetime import datetime as dt

parseDate="%Y-%m-%d %H:%M:%S"
book=[]
while True:
    bookcode=input("도서번호: ").strip()
    if bookcode=="": #if not bookcode
        break
    borrow_time=input("빌린 시간: ")
    return_time=input("반납시간: ")
    changedBorrowTime=dt.strptime(borrow_time,parseDate)
    changedReturnTime=dt.strptime(return_time,parseDate)
    diec={"bookcode": bookcode,"borrow_time":changedBorrowTime,"return_time":changedReturnTime}
    book.append(diec)

for books in book:
    print(books["bookcode"],books["borrow_time"],books["return_time"])

    
