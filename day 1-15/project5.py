print("""---------PYTHON PASSWORD GENERATOR---------
    -----------------------------------------------------
      ----------------------------------------------""")

import random
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
          'X','Y','Z' ]
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['@', '#','$','%','&','/','+','~']

letterSize = int(input("How many letters do you want in your password?: "))
numberSize = int(input("How many numbers do you want in your password?: "))
symbolSize = int(input("How many symbol do you want in your password?: "))

passwordList = []
for i in range(0,letterSize+1):
    passwordList.append(random.choice(letter))

for j in range(0, numberSize+1):
    passwordList.append(random.choice(number))

for k in range(0, symbolSize+1):
    passwordList.append(random.choice(symbol))

random.shuffle(passwordList)
myPassword = ""
for char in passwordList:
    myPassword +=char
print(f"Your Password is :\n {myPassword}")