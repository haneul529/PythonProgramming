import sqlite3

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

## 메인 코드 부분 ##
con = sqlite3.connect("C:\\Users\\lucia\\OneDrive\\바탕 화면\\하늘\\2023\\2학기\\전공\\오픈소스프로그래밍\\My_Python_VS_1207\\myDB")
cur = con.cursor()

cur.execute("SELECT * FROM productTable")

print("제품코드    제품명     가격      재고수량")
print("---------------------------------------")

while(True):
    row = cur.fetchone()
    if row == None:
        break;
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s  %15s %d    %d"%(data1, data2, data3, data4))

con.close()