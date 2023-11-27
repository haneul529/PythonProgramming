from tkinter import*
from random import*
import os
current_folder = os.path.dirname(os.path.abspath(__file__))
btnList = [None]*9
fnameList = ["froyo.gif", "gingerbread.gif","honeycomb.gif", "marshmallow.gif", "nougat.gif"]
photoList = [None]*9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

##메인 코드 부분##
window = Tk()
window.geometry("210x210")

shuffle(fnameList)

for i in range(0, 9):
    photoList[i] = PhotoImage(file = current_folder + "/gif/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])
    
for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70
        
window.mainloop()