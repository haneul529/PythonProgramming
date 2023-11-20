##함수 선언 부분 ##
def func1():
    print("Module1_full.py의 func1()이 호출됨.")

def func2():
    print("Module1_full.py의 func2()이 호출됨.")

def func3():
    print("Module1_full.py의 func3()이 호출됨.")

def DoIt():
    ## 메인 코드 부분
    func1()
    func2()
    func3()

if __name__ == '__main__':
    ## 메인 코드 함수
    DoIt()