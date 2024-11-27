# week13_B_08_1.py
# id:20240000
# name:jang eunmee

from week13_c_book import Book2 as Book
from week13_c_book import TimeStamp
from datetime import datetime as dt
import os

dtformat = "%Y-%m-%d %H:%M:%S"


def diff_seconds(intime, outtime):
    if not outtime:
        outtime = dt.now()
    return (outtime - intime).total_seconds()


if __name__ == "__main__":
    mydir = "c:\\book2_202444076"
    #myfile = "list.txt"
    #myfullfile = os.path.join(mydir, myfile)

    if not os.path.isdir(mydir):
        os.mkdir(mydir)

    books = []

    # read 작업해야 할 곳!
    # 파일이 있는지 확인
    # 있으면 파싱, 없으면 그대로 밑으로 떨어지면 됨.
    members=os.listdir(mydir)
    for member in members:
        member_fullName=os.path.join(mydir,member)
        if os.path.isfile(member_fullName):
            file_ext=os.path.splitext(member)
            #111.txt->111, .txt
            if file_ext and len(file_ext)==2 and file_ext[-1]==".txt":
                number = file_ext[0].strip()
                book=Book(number)
                with open(member_fullName,'r',encoding="utf-8") as f:
                    for line in f:
                        split_datas=line.strip().split("|")
                        if split_datas and len(split_datas)==2:
                            intime=dt.strptime(split_datas[0],dtformat)
                            if split_datas[1].strip():
                                outtime=dt.strptime(split_datas[1],dtformat)
                            else:
                                outtime=None

                            book.add_TimeStamp(intime,outtime)
                if book.history:
                    books.append(book)
    while True:
        number = input("차량번호:").strip()
        if not number:
            break
        search_book=[book for book in books if book.number == number]
        if not search_book:
            book=Book(number)
            boks.append(book)
        else:
            book=search_book[0]
            for timestamp in book.history:
                if timestamp.is_rent():
                    print("반납 필요")
                    continue
                #여기서 반납할껀지 물어보기
                

        while True:
            try:
                intime = input("입차시간:").strip()
                if intime:
                    intime = dt.strptime(intime, dtformat)
                    break
            except:
                pass

        while True:
            try:
                outtime = input("출차시간:").strip()
                if not outtime:
                    outtime = None
                    break
                outtime = dt.strptime(outtime, dtformat)
                break
            except:
                pass

        #book = {"num": number, "in": intime, "out": outtime}
        #time = { "in": intime, "out": outtime}
        #books[number].append(time)
            book.add_TimeStamp(intime,outtime)

        bookFullName=os.path.join(mypath,number+".txt.")
        with open(bookFullName,"a",encoding="utf-8") as f:
            intime = dt.strptime(intime.dtformat)
            if outtime:
                outtime=dt.strptime(outtime,dtformat)
                f,write(f"{intime}|{outtime}\n")
            else:
                f,write(f"{intime}|")

    for book in books:
        print("책번호",book.number)
        for timestamp in book.history:
            print(timestamp.renttime, timestamp.returntime)
            print(timestamp.diff_seconds(timestamp.renttime, timestamp.returntime))

