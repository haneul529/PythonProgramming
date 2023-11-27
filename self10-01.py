from tkinter import*
import os
current_folder = os.path.dirname(os.path.abspath(__file__))

window = Tk()
window.title("냥이들 ^^")

photo1 = PhotoImage(file = current_folder + "/gif/cat.gif")
label1 = Label(window, image=photo1)

photo2 = PhotoImage(file = current_folder + "/gif/cat2.gif")
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()