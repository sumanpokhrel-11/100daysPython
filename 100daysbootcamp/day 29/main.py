from tkinter import *
from tkinter import messagebox
import random, pyperclip, json
# ==========================Password Generator=================

def generate_pw():
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
            'X','Y','Z' ]
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol = ['@', '#','$','%','&','/','+','~']

    letterSize =  random.randint(1,8)
    numberSize = random.randint(1,3)
    symbolSize = random.randint(1,4)

    letter_pw = [random.choice(letter) for _ in range(letterSize)]
    number_pw = [random.choice(number) for _ in range(numberSize)]
    symbol_pw = [random.choice(symbol) for _ in range(symbolSize)]


    passwordList = letter_pw + number_pw + symbol_pw
    random.shuffle(passwordList)
    myPassword = "".join(passwordList)
    pass_entry.insert(0,myPassword)
    pyperclip.copy(myPassword) # this method copy the password in the clipboard 
# ===========================Save Password====================
def save():
    email_data = email_entry.get()
    web_data = web_entry.get()
    pass_data = pass_entry.get()
    dict_data = {
        web_data : {
            'email' : email_data,
            'password' :pass_data
        }
    }
    # checking validation in the input datas
    if len(web_data)==0 or len(pass_data) <=0:
        messagebox.showinfo(title='Warning', message="Don't Leave the fields empty")

    else:
        try:
            with open('100daysbootcamp\day 29\data.json', 'r') as data_file:
                # reading the old file
                data = json.load(data_file)
                # updating the new data in the old file
        except FileNotFoundError:
            with open('100daysbootcamp\day 29\data.json', 'w') as data_file:
                # writing the new data in the old file
                json.dump(data, data_file, indent=4)
        else:
            data.update(dict_data)
        
            with open("100daysbootcamp\day 29\data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0,END)


# =========================searching data=========================
def find_password():
    website = web_entry.get()
    try:
        files = open("100daysbootcamp\day 29\data.json", 'r')
        file = json.load(files)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='File Not Exist')
    else:
        if website in file:
            e_data = file[website]['email']
            p_data = file[website]['password']
            messagebox.showinfo(title=website, message=f"Email : {e_data}\nPassword : {p_data}")

        else:
            messagebox.showinfo(title=website, message=f"Info for {website} not Available")
    finally:
        files.close()
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
web.grid(row=1, column=0, pady=10)

web_entry = Entry(width=17)
web_entry.grid(row=1, column=1)
web_entry.focus()

# search button
search = Button(text='   Search   ', command=find_password)
search.grid(row=1, column=2, )

# email/username
email = Label(text="Email/Username: ")
email.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,'suman@gmail.com')
# password
password = Label(text="Password: ")
password.grid(row=3, column=0, pady=10)

pass_entry = Entry(width=17)
pass_entry.grid(row=3, column=1)

pass_btn = Button(text="Generate Password", command=generate_pw)
pass_btn.grid(row=3, column=2, padx=0)

# add
add = Button(text="ADD", width=30, command=save)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()