def get_score():
    scoreTbl = [['홍길동', 79, 86, 90, 96], ['나소웨', 93, 89, 96], ['이대한', 95, 89, 91, 93], ['오서경', 81, 96]]
    return scoreTbl

def print_get_max(scoreTbl):
    ss = []
    maxi = 0

    for i in scoreTbl[0][1:len(scoreTbl[0])]:
        if(maxi < i):
            maxi = i
    ss.append(maxi)
    maxi = 0
    for i in scoreTbl[1][1:len(scoreTbl[1])]:
        if(maxi < i):
            maxi = i
    ss.append(maxi)
    maxi = 0
    for i in scoreTbl[2][1:len(scoreTbl[2])]:
        if(maxi < i):
            maxi = i
    ss.append(maxi)
    maxi = 0
    for i in scoreTbl[3][1:len(scoreTbl[3])]:
        if(maxi < i):
            maxi = i
    ss.append(maxi)

    print(ss)


#main code
scoreTble = get_score()
print_get_max(scoreTble)
