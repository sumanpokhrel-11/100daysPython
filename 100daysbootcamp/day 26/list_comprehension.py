square = []
for num in range(1,11):
    square.append(num*num)

print(square)

# using list comprehension
square = [num*num for num in range(1,11)]
print(square)

name_list = ['suman', 'doe', 'floki', 'ragner', 'nisha']
myname = [name for name in name_list if len(name)==5]
print(myname)

# exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square = [num*num for num in numbers ]
print(square)

# exercise 2
even_numbers = [num for num in numbers if num%2==0]
print(even_numbers)