Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code09-07.py =============
func1()에서 a값 10
func2()에서 a값 10

====================== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py =====================
메인 시작에서 a값 20
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py", line 15, in <module>
    func1()
  File "C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py", line 5, in func1
    print("func1()에서 a값 %d" %a)
TypeError: %d format: a real number is required, not str

====================== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py =====================
메인 시작에서 a값 20
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py", line 15, in <module>
    func1()
  File "C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py", line 4, in func1
    a = HI
NameError: name 'HI' is not defined
>>> 
====================== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py =====================
메인 시작에서 a값 20
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py", line 15, in <module>
    func1()
  File "C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py", line 4, in func1
    a == HI
NameError: name 'HI' is not defined
>>> 
====================== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py =====================
메인 시작에서 a값 20
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py", line 15, in <module>
    func1()
  File "C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py", line 4, in func1
    a = Hi
NameError: name 'Hi' is not defined
>>> 
====================== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code09-07-2.py =====================
메인 시작에서 a값 20
func1()에서 a값 Hi
func2()에서 a값 Hi
메인 끝에서 a값 Hi
>>> 
======================= RESTART: C:/Users/lucia/OneDrive/바탕 화면/code09-09.py ======================
multi()에서 돌려준 값 ==> 300, -100
>>> 
======================= RESTART: C:\Users\lucia\OneDrive\바탕 화면\code09-11.py ======================
매개변수가 2개인 함수를 호출한 결과 ==> 30
매개변수가 3개인 함수를 호출한 결과 ==> 60
>>> 
======================= RESTART: C:/Users/lucia/OneDrive/바탕 화면/code09-12.py ======================
매개변수가 2개인 함수를 호출한 결과 ==> 30
매개변수가 10개인 함수를 호출한 결과 ==> 550
>>> def dic_func(**para):
...     for k in para.keys():
...         print("%s --> %d명 입니다." %(k, para[k]))
... 
...         
>>> dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4, 방탄소년단 = 7)
트와이스 --> 9명 입니다.
소녀시대 --> 7명 입니다.
걸스데이 --> 4명 입니다.
블랙핑크 --> 4명 입니다.
방탄소년단 --> 7명 입니다.
