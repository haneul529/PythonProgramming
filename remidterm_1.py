def get_score():
    scoreTbl = [['홍길동', 79, 86, 90, 96], ['나소웨', 93, 89, 96], ['이대한', 95, 89, 91, 93], ['오서경', 81, 96]]

def get_avg():
    for std in scoreTbl:
        hap = 0
        n = len(std)
        for score in std[1:]:
            hap += score
        std.append(hap/(len(std)-1))

def print_get_max():
    print('\n')
    for std in scoreTbl

#1. 점수표 받아오기
scoreTbl = get_score()
print(scoreTbl)
#2. 학생별 평균 점수 구해서 추가하기
get_avg(scoreTbl)
print(scoreTbl)
#3, 학생별 평균과 최고 점수 출력하기
