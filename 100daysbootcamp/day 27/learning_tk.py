import tkinter as tk
# learning tkinter basics
window = tk.Tk()
window.title("Learning Tkinter")
window.minsize(width=500, height= 800)
label = tk.Label(text='This is the label', font=('Ariel', 20, 'bold'))


label['text'] = 'label text using dictionary'


def change_label():
    label.config(text= 'this is a text from using button')
    label.pack()
btn = tk.Button(text='Click Me', command = change_label)
btn.pack()

def say_hello():
    print("Hello")
    enter = tk.Entry()
    name = enter.get()
    enter.pack()
    
    
    label.config(text=name)
    label.pack()
btn = tk.Button(text="Enter Your Name", command= say_hello)
btn.pack()
window.mainloop()


