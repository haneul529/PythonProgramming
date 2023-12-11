import sqlite3
import os

path = os.getcwd()

# 변수 선언 부분
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# 메인 코드 부분
con = sqlite3.connect(path + "/myDB")  # 현재 작업 폴더에 새 DB 파일 생성하여 연결
cur = con.cursor()

# 테이블 생성
cur.execute("CREATE TABLE IF NOT EXISTS productTable(pCode char(5), pName TEXT, price int, amount int)")

# 테이블에 데이터(레코드) 저장
while True:
    data1 = input("제품코드(입력을 끝내려면, 엔터를 누르세요) => ")
    if data1 == "":
        break
    data2 = input("제품명 ==> ")
    data3 = input("가격 ==> ")
    data4 = input("제품수량 ==> ")
    
    sql = "INSERT INTO productTable VALUES('" + data1 + "','" + data2 + "'," + data3 + "," + data4 + ")"
    print("완성된 sql >> ", sql)
    
    cur.execute(sql)

print("작업한 테이블을 DB에 저장합니다.")
con.commit()
con.close()
