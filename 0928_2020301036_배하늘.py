Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tt1=(10, 20, 30); tt1
(10, 20, 30)
tt2 = 10, 20, 30; tt2
(10, 20, 30)
tt3=(10);tt3
10
tt4=10;tt4
10
tt5=(10,);tt5
(10,)
tt6=10,;tt6
(10,)
tt1.append(40)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tt1.append(40)
AttributeError: 'tuple' object has no attribute 'append'
tt1[0] = 40
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tt1[0] = 40
TypeError: 'tuple' object does not support item assignment
del(tt1[0])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    del(tt1[0])
TypeError: 'tuple' object doesn't support item deletion
tt1 = (10, 20, 30, 40)
tt1[0]
10
tt1[0] + tt1[1] + tt1[2]
60
tt2 = ('A', 'B')
tt1 + tt2
(10, 20, 30, 40, 'A', 'B')
tt2*3
('A', 'B', 'A', 'B', 'A', 'B')
myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
myTuple=tuple(myList)
myTuple
(10, 20, 30, 40)
dic1={1:'a', 2:'b', 3:'c'}
dic1
{1: 'a', 2: 'b', 3: 'c'}
student1={'학번':1000, '이름':'홍길동', '학과':'컴퓨터학과'}
student1
{'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과'}
student1['연락처']='010-1111-2222'
student1
{'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과', '연락처': '010-1111-2222'}
student1['학과']='파이썬학과'
student1
{'학번': 1000, '이름': '홍길동', '학과': '파이썬학과', '연락처': '010-1111-2222'}
del{student1['학과']}
SyntaxError: incomplete input
del(student1['학과'])
student1
{'학번': 1000, '이름': '홍길동', '연락처': '010-1111-2222'}
student1={'학번':1000, '이름':'홍길동', '학과':'파이썬학과', '학번':2000}
student1
{'학번': 2000, '이름': '홍길동', '학과': '파이썬학과'}
student1['학번']
2000
student1['이름']
'홍길동'
student1['학과']
'파이썬학과'
list(student1.keys())
['학번', '이름', '학과']
student1.items()
dict_items([('학번', 2000), ('이름', '홍길동'), ('학과', '파이썬학과')])

===== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code07-08.py =====
이름 --> 트와이스
구성원 수 --> 9
데뷔 --> 서바이벌 식스틴
대표곡 --> SIGNAL

===== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code07-09.py =====
[('Edward', '에드워드'), ('Gothen', '고든'), ('Henry', '헨리'), ('James', '제임스'), ('Thomas', '토마스')]

===== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code07-10.py =====
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code07-10.py", line 6, in <module>
    myfood=input(str(list(foods.keys()) + " 중 좋아하는 음식은?"))
TypeError: can only concatenate list (not "str") to list

===== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code07-10.py =====
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code07-10.py", line 6, in <module>
    myfood=input(str(list(foods.keys()) + " 중 좋아하는 음식은?"))
TypeError: can only concatenate list (not "str") to list

===== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code07-10.py =====
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code07-10.py", line 6, in <module>
    myfood=input(str(list(foods.keys() + " 중 좋아하는 음식은?")))
TypeError: unsupported operand type(s) for +: 'dict_keys' and 'str'

===== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code07-10.py =====
Traceback (most recent call last):
  File "C:/Users/lucia/OneDrive/바탕 화면/code07-10.py", line 6, in <module>
    myfood=input(list(foods.keys()) + " 중 좋아하는 음식은?")
TypeError: can only concatenate list (not "str") to list

===== RESTART: C:/Users/lucia/OneDrive/바탕 화면/code07-10.py =====
['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살'] 중 좋아하는 음식은?치킨
<치킨> 궁합 음식은 <치킨무>입니다.
['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살'] 중 좋아하는 음식은?라면
<라면> 궁합 음식은 <김치>입니다.
['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살'] 중 좋아하는 음식은?짬뽕
그런 음식이 없습니다. 확인해 보세요.
['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살'] 중 좋아하는 음식은?끝
mySet1 = {1, 2, 3, 4, 5}
mySet2 = {4, 5, 6, 7}
mySet1&mySet2   #교집합
{4, 5}
>>> mySet1|mySet2   #합집합
{1, 2, 3, 4, 5, 6, 7}
>>> mySet1-mySet2   #차집합
{1, 2, 3}
>>> mySet1^mySet2   #대칭 차집합
{1, 2, 3, 6, 7}
>>> numList = [num*num for num in range(1, 6)]
>>> numList
[1, 4, 9, 16, 25]
>>> numList = [num for num in range(1, 21) if num%3 ==0]
>>> numList
[3, 6, 9, 12, 15, 18]
>>> foods = ['떡볶이', '짜장면', '라면, '피자', '맥주', '치킨', '삽겹살']
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> foods = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삽겹살']
...          
>>> sides = ['오뎅', '단무지', '김치']
...          
>>> for food, side in zip(foods, sides):
...          print(food. ' --> ', side)
...          
SyntaxError: invalid syntax
>>> for food, side in zip(foods, sides):
...          print(food, ' --> ', side)
... 
...          
떡볶이  -->  오뎅
짜장면  -->  단무지
라면  -->  김치
>>> foods=['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
...          
>>> sides =['오뎅', '단무지', '김치']
...          
>>> typList = list(zip(foods, sides))
...          
>>> dic = dict(zip(foods, sides))
...          
>>> tupList
...          
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    tupList
NameError: name 'tupList' is not defined. Did you mean: 'typList'?
>>> typList
...          
[('떡볶이', '오뎅'), ('짜장면', '단무지'), ('라면', '김치')]
>>> dic
...          
{'떡볶이': '오뎅', '짜장면': '단무지', '라면': '김치'}
