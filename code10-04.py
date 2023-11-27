from tkinter import*
import os
current_folder = os.path.dirname(os.path.abspath(__file__))

window = Tk()

photo = PhotoImage(file = "gif/dog.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()