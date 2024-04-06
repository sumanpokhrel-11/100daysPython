from tkinter import *
from tkinter import messagebox


# ===========================Save Password====================
def save():
    email_data = email_entry.get()
    web_data = web_entry.get()
    pass_data = pass_entry.get()

    is_ok = messagebox.askokcancel(title=web_data, message= f"These are the details entered: \n Email Address : {email_data}\n Password : {pass_data} \n Click Ok to save the data")

    if is_ok:
        file = open('100daysbootcamp\day 29\data.txt','a')
        file.write(f"{web_data} | {email_data} | {pass_data} \n")
        file.close 

    web_entry.delete(0, END)
    pass_entry.delete(0,END)






# -------------------------UI-----------------------------------------
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
web_entry.focus()

# email/username
email = Label(text="Email/Username: ")
email.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,'suman@gmail.com')
# password
password = Label(text="Password: ")
password.grid(row=3, column=0)

pass_entry = Entry(width=17)
pass_entry.grid(row=3, column=1)

pass_btn = Button(text="Generate Password")
pass_btn.grid(row=3, column=2)

# add
add = Button(text="ADD", width=30, command=save)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()