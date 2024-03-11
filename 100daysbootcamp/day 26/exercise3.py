first = open('100daysbootcamp\day 26\one.txt', 'r')
second = open('100daysbootcamp\day 26\wo.txt', 'r')
first_num = [int(num) for num in first]
second_num = [int(num) for num in second]

# using list comprehension
final = [first_num[i] for i in range(len(first_num)) if first_num[i] in second_num]
print(final)

first.close()
second.close()

# using normal for loop
# final = []
# for i in range(len(first_num)):
#     if first_num[i] in  second_num:
#         final.append(first_num[i])

# print(final)