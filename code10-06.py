from tkinter import *
from tkinter import messagebox

import os
current_folder = os.path.dirname(os.path.abspath(__file__))

## 함수 선언 부분 ##
def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")

## 메인 코드 부분 ##
window = Tk()

photo = PhotoImage(file = current_folder + "/gif/dog2.gif")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

window.mainloop()