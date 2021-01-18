from tkinter import *
from PIL import ImageTk

window = Tk()
window.title("test")
window.geometry("1000x1000")
window.resizable(width=True, height = True)

photo = ImageTk.PhotoImage(file="4.jpg")
label = Label(window, image=photo)

txt = Label(window, text = "text")

label.pack()
txt.pack()

window.mainloop()