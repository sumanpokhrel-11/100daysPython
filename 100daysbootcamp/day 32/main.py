# smtp.gmail.com is the provider of email by google
#  to make this work out, 2 factor authentication should be disabled
# new password is created for an new app, which should be pasted in my_password
# all the credentials should be valid


import smtplib
my_email = "11pksuman@gmail.com"
my_password = "My password"
receiver = "mynameissumanpokhrel@gmail.com"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password=my_password )
    connection.sendmail(from_addr=my_email,
to_addrs=receiver,
msg="Subject:Birthday Message \n \n Happy birthday to You.")