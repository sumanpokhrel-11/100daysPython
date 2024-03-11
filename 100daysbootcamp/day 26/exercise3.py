first = open('100daysbootcamp\day 26\one.txt', 'r')
second = open('100daysbootcamp\day 26\wo.txt', 'r')
first_num = [int(num) for num in first]
second_num = [int(num) for num in second]
final = []
for number in first_num:
    if first_num[number] == second_num[number]:
        final.append(first_num[number])

print(final)