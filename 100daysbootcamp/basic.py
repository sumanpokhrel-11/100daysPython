# for loop
x=5
for x in range(1, 11):
    if x==10:
        print(x)
        break
    break
# for loop in list
fruits = ["apple", 'banana', 'grapes', 'mango','peach']
for fruit in fruits:
    print(fruit)
    break

# for loop in 'range'
for x in range(1, 21, 2):
    print(x)
    break

# boolean logic in python 'and' 'or' 'not'

username= 'admin'
password = '12345'

if username =='admin' and password =='12345':
    print("Valid User")
else:
    print("Invalid User")

#while loop in python

counter = 1
while(counter<10):
    print(counter+1)
    counter+=1
    