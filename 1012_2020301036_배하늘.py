Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ss = "파이썬최고"
ss[0]
'파'
ss[1:3]
'이썬'
ss[:3]
'파이썬'
ss[3:]
'최고'

============== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code08-01.py =============
파$이$썬$짱$!$

= RESTART: C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1012/code08-01-2.py
파$이$썬$짱$!$

============ RESTART: C:/Users/lucia/OneDrive/바탕 화면/selfstudy8-1.py ============
#이#은#전#미#어#

============ RESTART: C:/Users/lucia/OneDrive/바탕 화면/selfstudy8-1.py ============
파#썬#완#재#있#요

============== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code08-02.py =============
문자열을 입력하세요 :즐거운 Python 프로그래밍
내용을 거꾸로 출력 --> 밍래그로프 nohtyP 운거즐
ss='Python is Easy.그래서 programming이 재미있습니다.^^'
ㄴㄴ.ㅕㅔㅔㄷㄱ()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ㄴㄴ.ㅕㅔㅔㄷㄱ()
NameError: name 'ᄂᄂ' is not defined
ss.upper()
'PYTHON IS EASY.그래서 PROGRAMMING이 재미있습니다.^^'
ss
'Python is Easy.그래서 programming이 재미있습니다.^^'
ss.lower()
'python is easy.그래서 programming이 재미있습니다.^^'
ss
'Python is Easy.그래서 programming이 재미있습니다.^^'
ss.swapcase()
'pYTHON IS eASY.그래서 PROGRAMMING이 재미있습니다.^^'
ss.title()
'Python Is Easy.그래서 Programming이 재미있습니다.^^'
ss.capitalize()
'Python is easy.그래서 programming이 재미있습니다.^^'
ss
'Python is Easy.그래서 programming이 재미있습니다.^^'

============== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code08-03.py =============
입력 문자열 ==> 파이썬 열공 중~~
출력 문자열 ==>Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code08-03.py", line 4, in <module>
    if ss.startwsith('(')==False:
AttributeError: 'str' object has no attribute 'startwsith'. Did you mean: 'startswith'?

============== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code08-03.py =============
입력 문자열 ==> 파이썬 열공중~~
출력 문자열 ==>(파이썬 열공중~~)

============ RESTART: C:/Users/lucia/OneDrive/바탕 화면/selfstudy8-2.py ============
원래 문자열 ==><<<파<<이>>썬>>>
<> 삭제 문자열 ==>파이썬
ss='열심히 파이썬 공부중~~'
ss.replace("파이썬", "Python")
'열심히 Python 공부중~~'
ss='Python을 열심히 공부 중'
ss.split()
['Python을', '열심히', '공부', '중']
ss='하나:둘:셋'
ss.split(':')
['하나', '둘', '셋']
ss='하나\n둘\n셋'
ss.splitlines()
['하나', '둘', '셋']
ss = '%'
ss.join('파이썬')
'파%이%썬'

============== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code08-06.py =============
날짜(연/월/일) 입력 ==>2019/12/31
입력한 날짜의 10년 후 ==>2029년12월31일
before = ['2019', '12, '31']
          
SyntaxError: unterminated string literal (detected at line 1)
before = ['2019', '12', '31']
          
after = list(map(int, before))
          
after
          
[2019, 12, 31]

============== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code08-07.py =============
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code08-07.py", line 20, in <module>
    r = random.radom();g=random.random();b=random.random()
AttributeError: module 'random' has no attribute 'radom'. Did you mean: 'random'?

============== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code08-07.py =============
Exception ignored in: <function Image.__del__ at 0x0000019C46C296C0>
Traceback (most recent call last):
  File "C:\Users\lucia\AppData\Local\Programs\Python\Python311\Lib\tkinter\__init__.py", line 4080, in __del__
    self.tk.call('image', 'delete', self.name)
RuntimeError: main thread is not in main loop

================================ RESTART: Shell ================================

============== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code09-04.py =============
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code09-04.py", line 9, in <module>
    print("100과 200의 plus()함수 결과는 %d"%hap)
TypeError: not all arguments converted during string formatting

============== RESTART: C:\Users\lucia\OneDrive\바탕 화면\code09-04.py =============
100과 200의 plus() 함수 결과는 300

============ RESTART: C:\Users\lucia\OneDrive\바탕 화면\selfstudy9-2.py ============
첫 번째 수를 입력하세요 : 2
계산을 입력하세요(+, -, *, /, **) : **
두 번째 수를 입력하세요 : 10
##계산기 : 2 ** 10 = 1024

============ RESTART: C:\Users\lucia\OneDrive\바탕 화면\selfstudy9-2.py ============
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /, **) : +
두 번째 수를 입력하세요 : 5
##계산기 : 34 + 5 = 39
계속하려면 Y를 눌러주세요: y
첫 번째 수를 입력하세요 : 33
계산을 입력하세요(+, -, *, /, **) : /
두 번째 수를 입력하세요 : 0
0으로는 나누면 안됩니다.ㅜㅜ
계산불가
##계산기 : 33 / 0 = 0
계속하려면 Y를 눌러주세요: Y

============ RESTART: C:\Users\lucia\OneDrive\바탕 화면\selfstudy9-2.py ============

============ RESTART: C:\Users\lucia\OneDrive\바탕 화면\selfstudy9-2.py ============
y
          
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    y
NameError: name 'y' is not defined

============ RESTART: C:\Users\lucia\OneDrive\바탕 화면\selfstudy9-2.py ============
34
          
34
>>> 
============ RESTART: C:\Users\lucia\OneDrive\바탕 화면\selfstudy9-2.py ============
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /, **) : +
두 번째 수를 입력하세요 : 5
##계산기 : 34 + 5 = 39
계속하려면 Y를 눌러주세요: y
첫 번째 수를 입력하세요 : 33
계산을 입력하세요(+, -, *, /, **) : /
두 번째 수를 입력하세요 : 0
0으로는 나누면 안됩니다.ㅜㅜ
계산불가
##계산기 : 33 / 0 = 0
계속하려면 Y를 눌러주세요: Y
첫 번째 수를 입력하세요 : we
Traceback (most recent call last):
  File "C:\Users\lucia\OneDrive\바탕 화면\selfstudy9-2.py", line 29, in <module>
    var1 = int(input("첫 번째 수를 입력하세요 : "))
ValueError: invalid literal for int() with base 10: 'we'
>>> 
============ RESTART: C:\Users\lucia\OneDrive\바탕 화면\selfstudy9-2.py ============
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /, **) : +
두 번째 수를 입력하세요 : 5
##계산기 : 34 + 5 = 39
계속하려면 Y를 눌러주세요: y
첫 번째 수를 입력하세요 : 33
계산을 입력하세요(+, -, *, /, **) : /
두 번째 수를 입력하세요 : 0
0으로는 나누면 안됩니다.ㅜㅜ
계산불가
계속하려면 Y를 눌러주세요: Y
첫 번째 수를 입력하세요 : 23
계산을 입력하세요(+, -, *, /, **) : **
두 번째 수를 입력하세요 : 3
##계산기 : 23 ** 3 = 12167
계속하려면 Y를 눌러주세요: 
프로그램을 종료합니다.
