import tkinter as tk
# learning tkinter basics
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

# learning **kwargs
class Car:
    def __init__(self, **kw):
        # use get method to use for optional argument
        self.model = kw.get('model')
        self.make = kw.get('make')
        self.color = kw.get('color')
        self.seats = kw['seats'] #this could raise an error if not initialize
car = Car(make='Nissan', model = 'jiplines', seats =7)
print(car.seats)