print('''   Tip Calculator
        Where you enter the total amount
     you enter the number to split the bill
and you are given choice whether to tip 10%, 12%, 15% or 20%
        ''')

total = float(input("\nEnter the total amount of bill: "))
split = int(input("\nEnter the number of people to split the bill: "))
tip = int(input("\nWhat percentages of tip would you like to give? 10, 12, 15 or 20: "))
perPersonCharge = 0
if tip==10:
    perPersonCharge = (total*1.1)/split
elif tip==12:
    perPersonCharge = (total*1.12)/split
elif tip==15:
    perPersonCharge = (total*1.15)/split
elif tip==20:
    perPersonCharge = (total*1.2)/split
else:
    print("\nEnter the tip either 10, 12, 15 or 20 percentages!!")
if perPersonCharge>0:
    print("\nEach person should pay: ", round(perPersonCharge,1))




