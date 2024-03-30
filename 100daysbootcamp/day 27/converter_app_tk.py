# converting km from miles
# 1 mile = 1.6 km
from tkinter import *

window = Tk()
window.minsize(height=100, width=200)
window.title('Miles to Km Converter')
window.config(padx=100, pady=100)



def converter():
    miles = float(input.get())
    km =round(miles*1.609)
    return my_label2.config(text=f"{km}")


# 1
input = Entry(width=5)
input.get()
input.grid(row=0, column=4)

# 2
my_label = Label(text='Miles', font=('Arial', 14, 'bold'))
my_label.config(text="Miles")
my_label.grid(row=0,column=6)


# 3
my_label1 = Label(font=('Arial', 14, 'bold'))
my_label1.config(text="is equals to")
my_label1.grid(row=1,column=2)


# 4
my_label2 = Label(text='0', font=('Arial', 14, 'bold'))
my_label2.config(text='0')
my_label2.grid(row=1,column=4)

my_label3 = Label(text='km', font=('Arial', 14, 'bold'))
my_label3.config(text='km')
my_label3.grid(row=1,column=6)



btn = Button(text='Calculate', command=converter)
# my_label.config(text = converter())
btn.grid(row=2,column=4)
# my_label.grid(row=2, column=3)


window.mainloop()