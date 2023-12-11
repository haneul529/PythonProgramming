# [응용예제 13-1] 문자 발생빈도를 DB 저장하기
import sqlite3

#문자열
inStr = ''' 죽는 날까지 하늘을 우러러 한 점 부끄럼이 없기를,
잎새에 이는 바람에도 나는 괴로웠다.
별을 노래하는 마음으로 모든 죽어가는 것을 사랑해야지.
그리고 나한테 주어진 길을 걸어가야겠다.
오늘 밤에도 별이 바람에 스치운다. '''

#변수 선언
con, cur = None, None
onechar, count = "", 0

#메인 코드
if __name__ == '__main__':
    con = sqlite3.connect("countDB")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS countTable") #이미 테이블이 있으면 삭제하기~
    cur.execute("CREATE TABLE countTable(onechar TEXT, count INT)") #테이블 새로 만들기
    
    for ch in inStr:
        cur.execute("SELECT * FROM countTable WHERE onechar - '" + ch + "'")
        row = cur.fetchone()
        