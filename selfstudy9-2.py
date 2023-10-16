##숫자1, 연산자, 숫자2 순서로 입력받기##
##제곱(**)연산자를 추가한다##
##0으로 나누려고 하면 메시지를 출력하고 계산되지 않도록 한다.##
import sys
def calc(v1, v2, op) :
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        if v2 == 0:
            print("0으로는 나누면 안됩니다.ㅜㅜ\n계산불가")
            
        else:
            result = v1 / v2
    elif op == '**' :
        result = v1 ** v2

    return result

res = 0
var1, var2, oper = 0, 0, ""

next = 'y'
while next == "y" or next =="Y":
    var1 = int(input("첫 번째 수를 입력하세요 : "))
    oper = input("계산을 입력하세요(+, -, *, /, **) : ")
    var2 = int(input("두 번째 수를 입력하세요 : "))
    
    res = calc(var1, var2, oper)
    if oper != '/' and var2 != 0:
        print("##계산기 : %d %s %d = %d"%(var1, oper, var2, res))
    next = input("계속하려면 Y를 눌러주세요: ")
print("프로그램을 종료합니다.")
sys.exit(1)



