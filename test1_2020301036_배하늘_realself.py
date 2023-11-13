# 문장 입력받아서 반환
def get_txt():
    return input("글을 입력해주세요: ")

# 단어리스트 구하여 반환
def get_terms(txt):
    terms = txt.lower().split()
    return terms

# 단어별 횟수를 카운트하여 반환 / termCount 변수는 딕셔너리 변수
def get_termCount(terms):
    termCount = {}  #빈 딕셔너리 termCount
    for term in terms:
        if not term in termCount.keys():
            termCount[term] = 1     #{term:1} 추가
        else:
            termCount[term] += 1
    return termCount    # 딕셔너리 반환

#메인 코드 작성
txt = get_txt()
terms = get_terms(txt)
print("\n단어 리스트 : ", terms)
termCount = get_termCount(terms)
print("\n단어 카운트 : ", termCount) 
