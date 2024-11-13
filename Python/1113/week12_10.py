def Test():
    raise NotImplementedError("test함수 미작성")  #일부러 에러를 발생

while True:
    try:
        dvd = int(input("피제수: "))
        dvs = int(input("제수: "))
        result = dvd/dvs
        print(result)
        Test()
    except ValueError:   #입력값 오류가 발생했을 때 만 실행
        print("올바른 값을 입력해주세요.")
    except ZeroDivisionError: #제수값에 0이 들어갔을 때 만 실행
        print("제수는 0을 넣으면 안됩니다.")
    except Exception as e:   #아무 에러가 발생했을 때 만 실행
        print(e)  #왜 죽었는지를 출력
    else:
        print("try문이 완벽히 실행하면 할것")
    finally:  #끝났을 때 반드시 실행
        print("안녕히 계세요.")
    #except:   #예외가 발생했을 때 만 실행
    #    print("dead")
