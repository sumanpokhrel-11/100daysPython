import tkinter as tk

window = tk.Tk()
window.title("Learning Tkinter")
window.minsize(width=500, height= 800)
label = tk.Label(text='This is the label', font=('Ariel', 20, 'bold'))
label.pack()


window.mainloop()


# learning *agr 
def add(*num):
    sum = 0
    for i in num:
        sum +=i
    return print(sum)
add(2, 3, 5, 2,7)