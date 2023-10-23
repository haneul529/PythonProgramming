## 함수 선언 부분 ##
def func1():
    global a    # 이 함수 안에서 a는 전역변수
    a = 'Hi'
    print("func1()에서 a값 {}" .format(a))

def func2():
    print("func2()에서 a값 {}" .format(a))

## 함수 변수 선언 부분 ##
a = 20          # 전역변수

## 메인 코드 부분 ##
print("메인 시작에서 a값 {}".format(a))
func1()
func2()
print("메인 끝에서 a값 {}".format(a))
