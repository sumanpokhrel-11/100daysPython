PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


from tkinter import *
import math
# timer mechanism
def start_timer():
    count_down(5*60)



# countdown mechanisms
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000, count_down, count-1)


# ui setup

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

label1 = Label(text='Timer', font=(FONT_NAME, 34, 'bold'), fg=GREEN, bg=YELLOW)
label1.grid(row=0, column= 1)


canvas = Canvas(width=250, height=226, bg= YELLOW, highlightthickness=0, highlightcolor=YELLOW)
pic = PhotoImage(file="100daysbootcamp\day 28\image.png")
canvas.create_image(125, 113, image = pic)
# canvas.create_text(125, 113, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
timer_text = canvas.create_text(120, 130, text='00:00', fill='white',font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


def start():
    pass
def stop():
    pass
btn1 = Button(text='Start', command = start_timer, highlightthickness=0)
btn1.grid(row=2,column=0)

btn2 = Button(text='Reset', command = stop, highlightthickness=0)
btn2.grid(row=2,column=2)

check = "✔️"
label2 = Label(text=check, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
label2.grid(row=3, column=1)


window.mainloop()