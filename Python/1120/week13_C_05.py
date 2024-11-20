#id:202444076
#name: limsuyoung

import datetime
from datetime import datetime as dt

def diff_seconds(a,b):
    if b!=None:
        b=datetime.datetime.now()
        return b-a
    else:
        return b-a

parseDate="%Y-%m-%d %H:%M:%S"
book=[]
while True:
    bookcode=input("도서번호: ").strip()
    if bookcode=="": #if not bookcode
        break
    while True:
        try:
            borrow_time=input("빌린 시간: ").strip()
            if borrow_time!="":
                changedBorrowTime=dt.strptime(borrow_time,parseDate)
                break
        except ValueError:
                print("올바른 값을 입력해주세요")

    while True:
        try:
            return_time=input("반납시간: ").strip()
            if not return_time:
                return_time=None
            elif return_time!="":
                changedReturnTime=dt.strptime(return_time,parseDate)
                break

        except ValueError:
                print("올바른 값을 입력해주세요")
        
    diec={"bookcode": bookcode,"borrow_time":changedBorrowTime,"return_time":changedReturnTime}
    book.append(diec)

for books in book:
    print(books["bookcode"],books["borrow_time"],books["return_time"])
    print(diff_seconds(books["borrow_time"],books["return_time"]))

    
