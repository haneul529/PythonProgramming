def get_score():
    scoreTbl = [['홍길동', 79, 86, 90, 96], ['나소웨', 93, 89, 96], ['이대한', 95, 89, 91, 93], ['오서경', 81, 96]]
    return scoreTbl
def get_avg(scoreTbl):
    for i in range(0, len(scoreTbl)):
        hap = 0
        for j in range(1, len(scoreTbl[i])):
            hap += scoreTbl[i][j]
        avg = hap / (len(scoreTbl[i])-1)
        scoreTbl[i].append(avg)
def print_get_max(scoreTbl):
    print("\n")
    for std in scoreTbl:
        mx = 0
        n = len(std)
        for i in range(1, n):
            if std[i] > mx: mx = std[i]
        print("%s => 평균: %.2f 최고점수: (%d학년) %d"%(std[0], std[-1], std.index(mx), mx))

#1. 점수표 받아오기
scoreTbl = get_score()
print(scoreTbl)
#2. 학생별 평균 점수 구해서 추가하기
get_avg(scoreTbl)
print(scoreTbl)
#3. 학생별 평균과 최고 점수 출력하기
print_get_max(scoreTbl)
    
