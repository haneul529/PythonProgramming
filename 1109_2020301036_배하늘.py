Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Module1.func1()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Module1.func1()
NameError: name 'Module1' is not defined

========= RESTART: C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/Module1.py ========
Module1.func1()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    Module1.func1()
NameError: name 'Module1' is not defined
Module1.func1()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Module1.func1()
NameError: name 'Module1' is not defined
import Module1
Module1.func1()
Module1.py의 func1()이 호출됨.

============ RESTART: C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/A.py ===========
Module1.py의 func1()이 호출됨.
Module2.py의 func1()이 호출됨.
Module3.py의 func1()이 호출됨.

============ RESTART: C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/B.py ===========
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/B.py", line 1, in <module>
    from Module1 import func1, unc2, func3
ImportError: cannot import name 'unc2' from 'Module1' (C:\Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109\Module1.py)

============ RESTART: C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/B.py ===========
Module1.py의 func1()이 호출됨.
Module2.py의 func1()이 호출됨.
Module3.py의 func1()이 호출됨.

======== RESTART: C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/code09-14.py =======
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/code09-14.py", line 12, in <module>
    turtle.setup(width = swidth + 50, hieght = sheight + 50)
TypeError: setup() got an unexpected keyword argument 'hieght'

======== RESTART: C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/code09-14.py =======
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/code09-14.py", line 21, in <module>
    tX, tY, tAngle, txtSize = getXYAS(swidth, sheight)
  File "C:\Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109\myTurtle.py", line 18, in getXYAS
    x = random,randrange(-sw/2, sw/2)
NameError: name 'randrange' is not defined

======== RESTART: C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/code09-14.py =======

======== RESTART: C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/code09-14.py =======
def hap(num1, num2):
    res = num1 + num2
    return res

Exception ignored in: <function Image.__del__ at 0x000001764BF696C0>
Traceback (most recent call last):
  File "C:\Users\lucia\AppData\Local\Programs\Python\Python311\Lib\tkinter\__init__.py", line 4080, in __del__
    self.tk.call('image', 'delete', self.name)
RuntimeError: main thread is not in main loop

========================================= RESTART: Shell =========================================
print(hap(10, 20))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(hap(10, 20))
NameError: name 'hap' is not defined. Did you mean: 'map'?
def hap(num1, num2)L
SyntaxError: incomplete input
def hap(num1, num2):
    res = num1 + num2
    return res

print(hap(10, 20))
30
hap2 = lambda num1, num2 : num1 + num2
print(hap2(10, 20))
30
hap3 = lanbda num1 = 10, num2 = 20 : num1+num2
SyntaxError: invalid syntax
hap3 = lambda num1 = 10, num2 = 20 : num1+num2
print(hap3())
30
p
print(hap3(100, 200))
300
myList = [1, 2, 3, 4, 5]
def add10(num):
    return num + 10

for i in range(len(myList)):
    myList[i] = add10(myList[i])

    
print(myList)
[11, 12, 13, 14, 15]
myList = [1, 2, 3, 4, 5]
add100 = lambda num : num + 10
mtList = list(map(add10, myList))
>>> print(myList)
[1, 2, 3, 4, 5]
>>> myList = [1, 2, 3, 4, 5]
>>> myList = list(map(lambda num : num + 10, myList))
>>> print(myList)
[11, 12, 13, 14, 15]
>>> list1 = [1, 2, 3, 4]
>>> list2 = [10, 20, 30, 40]
>>> hapList = list(map(lambda n1, n2 : n1+n2, list1, list2))
>>> print(hapList)
[11, 22, 33, 44]
>>> def count(num):
...     if num >= 1:
...         print(num, end =' ')
...         count(num-1)
...     else:
...         return
... count(10)
SyntaxError: invalid syntax
>>> count(20)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    count(20)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> 
====== RESTART: C:/Users/lucia/OneDrive/바탕 화면/하늘/2023/2학기/전공/오픈소스프로그래밍/1109/section06_01.py ======
10 9 8 7 6 5 4 3 2 1 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
>>> def factorial(num):
...     print("factorial(%d) 호출" %num)
...     if num <= 1:
...         return num
...     else:
...         return num*factorial(num-1)
... 
...     
>>> factorial(4)
factorial(4) 호출
factorial(3) 호출
factorial(2) 호출
factorial(1) 호출
24
>>> factorial(10)
factorial(10) 호출
factorial(9) 호출
factorial(8) 호출
factorial(7) 호출
factorial(6) 호출
factorial(5) 호출
factorial(4) 호출
factorial(3) 호출
factorial(2) 호출
factorial(1) 호출
3628800
