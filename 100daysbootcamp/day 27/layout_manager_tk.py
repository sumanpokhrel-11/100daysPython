from tkinter import *

def button_clicked():
    print("clicked!")
    new_text = input.get()
    my_label.config(text= new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=600)
window.config(padx=50, pady=50) #padding to the window

# label
my_label = Label(text='I M Label', font=('Arial', 24, 'bold'))
my_label.config(text='New text')
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)#applying padding to the fix widget

# button
button = Button(text='Click Me', command=button_clicked)
button.grid(row=1, column=1)

# entry
input = Entry(width=10)
print(input.get())
input.grid(row=3, column=4)

new_btn = Button(text='new btn', command = button_clicked)
new_btn.grid(row=0, column=3)
window.mainloop()