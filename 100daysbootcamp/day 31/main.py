from tkinter import *

BACKGROUND_COLOR = "#B1EDE0"

window = Tk()
window.title('Learn French')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage("100daysbootcamp\day 31\images\card_front.png")
canvas.create_image(400, 263, image = front_img)
canvas.create_text(400, 150, text="Title", font=('Ariel', 35, 'italic'))
canvas.create_text(400, 263, text="Word", font=('Ariel', 40, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row= 0, column= 0, columnspan=2)

cross_img = PhotoImage(file="100daysbootcamp\day 31\images\wrong.png")
cross_btn = Button(image=cross_img, highlightthickness=0)
cross_btn.grid(row=1, column=0)

right_img = PhotoImage(file="100daysbootcamp\day 31\images\correct.png")
right_btn = Button(image = right_img, highlightthickness=0)
right_btn.grid(row=1, column=1)

window.mainloop()

