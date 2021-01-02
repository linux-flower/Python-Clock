from tkinter import *
import tkinter
from datetime import datetime

#Colors
black = "#3d3d3d" #Preto
white = "#fafcff" #Branco
green = "#21c25c" #Verde
red =  "#eb463b" #Vermelho
grey = "#dedcdc" #Cinza
blue = "#3080f0" #Azul

wallpeper = black
color = white

window=Tk()
window.title("Digital Clock")
window.geometry("440x180")
window.resizable(width=FALSE, height=FALSE)
window.configure(bg=black)

def clock():
    time=datetime.now()

    hour = time.strftime("%H:%M:%S")
    week_day = time.strftime("%A")
    day = time.day
    mont = time.strftime("%B")
    year = time.strftime("%Y")

    text.config(text=hour)
    text.after(1000, clock)
    text1.config(text=week_day + " "+ str(day) + "/" + str(mont) + "/" + str(year))

text=Label(window, text="", font=("Arial.ttf 70"), bg=wallpeper, fg=color)
text.grid(row=0, column=0, stick=NW, padx=5)

text1=Label(window, text="", font=("Arial.ttf 20"), bg=wallpeper, fg=color)
text1.grid(row=1, column=0, stick=NW, padx=5)

clock()
window.mainloop()
