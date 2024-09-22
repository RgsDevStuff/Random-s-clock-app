from tkinter import *
from time import *
def update():
    timestr = strftime("%b %d, %Y   |   %I:%M %p")
    TimeL.config(text=timestr,)
    TimeL.after(1,update)
window = Tk()
icon = PhotoImage(file='clock.png')
window.iconphoto(True,icon)
window.resizable(False,False)
window.title("Random's clock app")
TimeL = Label(window,font=("Arial",50),fg="#00ff2a",bg="black",)
TimeL.pack()
update()
window.mainloop()