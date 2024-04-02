from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")


canvas = Canvas(width=200, height=200)
# picture
pic = PhotoImage(file='100daysbootcamp\day 29\password.png')
canvas.create_image(100,100, image=pic)
canvas.grid(row=0, column=1)

# website
web = Label(text="Website: ")
web.grid(row=1, column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)


# email/username
email = Label(text="Email/Username: ")
email.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

# password
password = Label(text="Password: ")
password.grid(row=3, column=0)

pass_entry = Entry(width=17)
pass_entry.grid(row=3, column=1)

pass_btn = Button(text="Generate Password")
pass_btn.grid(row=3, column=2)

# add
add = Button(text="ADD", width=30)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()