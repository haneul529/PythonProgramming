import os

abspathTest = os.path.dirname(os.path.abspath(__file__))
print("os.path.dirname(os.abspath(__file__))로 구한 절대경로->>", abspathTest)

relpathTest = os.getcwd()
print("os.getcwd()로 구한 현재 폴더 경로->>", relpathTest)

print("현재파일의 VS Code [경로복사] ->> C:\\Users\\lucia\\OneDrive\\바탕 화면\\하늘\\2023\\2학기\\전공\\오픈소스프로그래밍\\My_Python_VS_1123\\file_path_test.py")
print("현재파일의 VS Code [상대경로복사]->> file_path_test.py")