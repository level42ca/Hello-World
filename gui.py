from tkinter import *

def close():
    exit()

window = Tk()
menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Close", command=close)

menubar.add_cascade(label="File", menu=filemenu)

window.config(menu=menubar)
window.mainloop()
