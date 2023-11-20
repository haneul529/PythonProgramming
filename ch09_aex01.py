import random

#함수선언
def getNumber(strData):
    numStr = ''
    for ch in strData:
        if ch.isdigit():
            numStr += ch
    return int(numStr)

#전역변수
data = []
i, k = 0, 0

#메인 작업
if __name__ == '__main__':
    for i in range(0, 10):
        tmp = hex(random.randint(0, 10000))
        tmp = tmp[2:] #접두사 '0x' 제거
        data.append(tmp)

    print('정렬 전 데이터 : ', end='')

    [print(num, end=' ') for num in data]

    for i in range(0, len(data)-1):
        for k in range(i+1, len(data)):
                if getNumber(data[i]) > getNumber(data[k]) :
                    tmp = data[i]
                    data[i] = data[k]
                    data[k] = tmp
    
    print('\n정렬 후 데이터 : ', end='')
    [print(num, end = ' ')for num in data]
    