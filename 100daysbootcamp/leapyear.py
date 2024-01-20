print("""leap year
if the year is evenly divisible by 4
except the year is evenly divisible by 100
unless the year is evenly divisible by 400""")

year = int(input("\nEnter the year to check: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"The year {year} is leap year")
        else:
            print(f"The year {year} is not leap year")
    else:
        print(f"The year {year} is leap year")
else:
    print(f"The year {year} is not leap year")