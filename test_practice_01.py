##문장을 입력받아서 txt리스트에 저장한 후에, 단어 리스트를 만들기##
##단어별 출현 횟수를 카운트하여 출력하는 프로그램##

##조건1. 문장을 입력 받아 반환하는 작업은 get_txt() 함수에서 수행한다.                      ==>     txt=get_txt()                       ##
##조건2. 단어 리스트를 구하여 반환하는 작업은 get_terms() 함수에서 수행한다.                ==>     terms=get_terms(txt)                ##
##조건3. 단어별 횟수를 카운트하여 반환하는 작업은 get_termCount() 함수에서 수행한다.        ==>     termCount=get_termCount(terms)      ##
##함수의 작업결과를 저장하는 termCount 변수는 딕셔너리 변수를 사용하여라.##

##함수 정의##
def get_txt():
    return input("글을 입력해주세요: ")

def get_terms(txt):
    terms=txt.lower().split()
    return terms

def get_termCount(terms):
    tCnt = {}
    for term in terms:
        if not term in tCnt.keys():
            tCnt[term] = 1
        else:
            tCnt[term] += 1
    return tCnt

#1.글 입력받기
txt = get_txt()
#2. 단어 리스트 만들기
terms = get_terms(txt)
print("\n단어 리스트 :", terms)
#3. 단어별 출현 횟수를 구해 출력하기
termCount=get_termCount(terms)
print("\n단어 카운트:", termCount)
