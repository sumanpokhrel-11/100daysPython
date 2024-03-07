print("""Pizza Ordering System
Enter the size for pizza for example (S, M, L)=>(small, medium, large)
Enter if you want pepperoni or not(Y,N)=> (Yes, No)
Enter if you want extra cheeze or not (Y,N)=>(Yes, NO)
Small pizza: $15
Large Pizza: $25
Medium Pizza: $20
Pepperoni for small pizza: +$2
Pepperoni for medium or large pizza: +$5
Extra cheese for any size pizza: +$1""")

size = input("\n What size pizza do you want?(S, M, L): ")
pepperoni = input("Do you want pepperoni? (Y/N): ")
cheese = input("Do you want extra cheese? (Y/N): ")

sm = 15
md= 20
lg = 25
pepSm = 2
pepML= 5
cese = 1
size = size.upper()
pepperoni = pepperoni.upper()
cheese = cheese.upper()
def validateInput():
    if ((size=="S" or size =="M" or size =="L") and (pepperoni=='Y' or pepperoni=='N') and (cheese=='Y' or cheese =='N')):
        return True
    else:
        return False
price = 0
if validateInput()==True:
    if size =="S":
        if pepperoni =="Y":
            if cheese =="Y":
                price= sm + pepSm + cese
            else:
                price = sm + pepSm
        elif pepperoni =="N" and cheese == "Y":
            price = sm + cese
        else:
            price = sm
    if size =="M":
        if pepperoni =="Y":
            if cheese =="Y":
                price= md + pepML + cese
            else:
                price = md + pepML
        elif pepperoni =="N" and cheese == "Y":
            price = md + cese
        else:
            price = md
    
    if size =="L":
        if pepperoni =="Y":
            if cheese =="Y":
                price= lg + pepML + cese
            else:
                price = lg + pepML
        elif pepperoni =="N" and cheese == "Y":
            price = lg + cese
        else:
            price = lg

    print(f"Your bill is : ${price}")

else:
    print("Enter the valid Input!!")

    
    

