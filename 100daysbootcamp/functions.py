#basic function calling and defining
def myFunc():
    print("hello People")
myFunc()
#function with arguments
def add(a, b):
    print(a+b)
add(5,6) #calling function add()

#function with return
def multiply(a,b):
    return a*b
a = multiply(5,6)
print(a)

# lambda function in python 
# it is same as anonymous function in php
sum = lambda a, b: a+b
print(sum(90, 9))

square = lambda a: a*a
print(square(5))

# *args, **kwargs in python
# first *args
'''args and kwargs are special keywords which allows functions to
takes any variable length arguments
args pass variable number of non-keyword argument list
kwargs pass variable number of keywords arguments dictionary to function on which 
operations of a dictionary can be  performed
*args and *kwargs make functions flexible'''
def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("sum:", sum)
adder(2)
adder(2, 3)
adder(2,3,4,5,2,7)

# *kwarg in python
def intro(**data):
    print("\n datatype of the argument is :", type(data))
    
    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(firstname='suman', lastname= 'pokhrel', age = 22, rollno = 11)