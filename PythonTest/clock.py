from tkinter import *
from datetime import datetime

# Colors
black: str = "#3d3d3d"  # Preto
white: str = "#fafcff"  # Branco
green: str = "#21c25c"  # Verde
red: str = "#eb463b"  # Vermelho
grey: str = "#dedcdc"  # Cinza
blue: str = "#3080f0"  # Azul

wallpeper: str = white
color = black

window = Tk()
window.title("Digital Clock")
window.geometry("380x150")
window.resizable(width=FALSE, height=FALSE)
window.configure(bg=white)

bt = Button(window, width=20, text='OK')
bt.place(x=100, y=150)


def clock():
    time = datetime.now()

    hour = time.strftime("%H:%M:%S")
    week_day = time.strftime("%A")
    day = time.day
    mont = time.strftime("%B")
    year = time.strftime("%Y")

    text.config(text=hour)
    text.after(1000, clock)
    text1.config(text=week_day + " " + str(day) + "/" + str(mont) + "/" + str(year))


text = Label(window, text="", font='Arial 70 ', bg=wallpeper, fg=color)
text.grid(row=0, column=0, stick=NW, padx=5)

text1 = Label(window, text="", font="Arial 20 italic", bg=wallpeper, fg=color)
text1.grid(row=1, column=0, stick=NW, padx=5)

clock()
window.mainloop()
