outFp = None
outStr =""

outFp = open("C:\\Users\\lucia\\OneDrive\\바탕 화면\\하늘\\2023\\2학기\\전공\\오픈소스프로그래밍\\My_Python_VS_1123\\data2.txt", "w", encoding='utf-8')

while True:
    outStr=input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break
    
outFp.close()
print("~~~ 파일에 정상적으로 써졌음 ~~~")