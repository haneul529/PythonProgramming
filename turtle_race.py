import turtle as t
from random import randint

print("********** 거북이 게임을 시작합니다. **********")
print("거북이 선수를 선택하세요.")

name = [0, 0, 0, 0]
name[0] = input("거북이1번 : ")
name[1] = input("거북이2번 : ")
name[2] = input("거북이3번 : ")
name[3] = input("거북이4번 : ")

#경기장 그리기
t.speed(10)
t.penup()
t.goto(-140, 140)

for step in range(15):
    t.write(step, align='center')
    t.right(90)
    t.forward(10)
    t.pendown()
    t.forward(150)
    t.penup()
    t.backward(160)
    t.left(90)
    t.forward(20)
t.hideturtle()

#게임 플레이어 준비
color = ['red', 'yellow', 'greem', 'blue']

player1 = t.Turtle()
player1.color('red')
player1.shape('turtle')
player1.penup()
player1.goto(-160, 100)
player1.pendown()
player1.pensize(5)

player2 = t.Turtle()
player2.color('yellow')
player2.shape('turtle')
player2.penup()
player2.goto(-160, 70)
player2.pendown()
player2.pensize(5)

player3 = t.Turtle()
player3.color('green')
player3.shape('turtle')
player3.penup()
player3.goto(-160, 40)
player3.pendown()
player3.pensize(5)

player4 = t.Turtle()
player4.color('blue')
player4.shape('turtle')
player4.penup()
player4.goto(-160, 10)
player4.pendown()
player4.pensize(5)

#게임 시작!
for run in range(100):
    player1.forward(randint(1,5))
    player2.forward(randint(1,5))
    player3.forward(randint(1,5))
    player4.forward(randint(1,5))

#게임 끝===========================================
x1,y1 = player1.position()
x2,y2 = player2.position()
x3,y3 = player3.position()
x4,y4 = player4.position()

score_x = [x1, x2, x3, x4]
#게임끝 : 거북이 선수 이름 쓰기--------------------
t.penup()
t.goto(x1+17, y1-5)
t.pendown()
t.write(name[0])    #거북이 오른쪽에 선수 이름 쓰기

t.penup()
t.goto(x2+17, y2-5)
t.pendown()
t.write(name[1])

t.penup()
t.goto(x3+17, y3-5)
t.pendown()
t.write(name[2])

t.penup()
t.goto(x4+17, y4-5)
t.pendown()
t.write(name[3])

t.hideturtle()  #커서 감추기
#게임 끝 : 가장 많이 뛴 거북이 찾기----------------
maxValue = score_x[0]
max_i = 0
for i in range(1, len(score_x)):
    if maxValue < score_x[i]:
        maxValue = score_x[i]
        max_i = i

print("%s님, 1등입니다! 축하합니다!!" %name[max_i])
