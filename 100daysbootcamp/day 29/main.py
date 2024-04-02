from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")


canvas = Canvas(width=200, height=200)
pic = PhotoImage(file='100daysbootcamp\day 29\password.png')
canvas.create_image(100,100, image=pic)
canvas.pack()

window.mainloop()