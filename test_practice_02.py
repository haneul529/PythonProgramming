def get_name_score(score, n):
    for _ in range(n):
        name = (input("이름입력 : "))
        score[name] = int(input("점수입력 : "))
    print("score : ", score)

def get_avg(score):
    hap = 0
    for v in score.values():
        hap += v

    return (hap/len(score))

def get_max(score):
    mx = 0
    for name in score.keys():
        if score[name] > mx:
            ms = score[name]
            mx_key=name

    return mx, mx_key

n = int(input("입력할 학생이 몇 명입니까?"))
score={}

get_name_score(score, n)
avg=get_avg(score)
print("\n평균점수 = %.2f점"%avg)
maxScore, name = get_max(score)
print("\n최고점수 = %s : %d점"%(name, maxScore))
