import tkinter as tk
# learning tkinter basics
window = tk.Tk()
window.title("Learning Tkinter")
window.minsize(width=500, height= 800)
label = tk.Label(text='This is the label', font=('Ariel', 20, 'bold'))
label.pack()


window.mainloop()


