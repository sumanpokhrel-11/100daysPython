print('''coffee machine''')

items = {
        'espresso':{
         'water':50,
         'coffee': 18,
         'milk': 0,
         'price': 1.5
         },
         'latte':{
         'water': 200,
         'coffee':24,
         'milk': 150,
         'price': 2.5
         },
         'cappuccino':{
         'water': 250,
         'coffee':24,
         'milk': 100,
         'price': 3
         }
}
names = ['espresso', 'latte', 'cappuccino']

penn = 0.01
dim = 0.1
nicke=0.05
quarte= 0.25

machine = {
     'water':300,
         'coffee': 100,
         'milk': 200,
}

print(items)
print(machine)



water = 300
coffee = 100
milk = 200
anotherCoffee = False
while not anotherCoffee:
    
    def reports():
        print(f"The machine contains water: {water}, coffee: {coffee}, milk: {milk}")
    userChoice = str(input("Enter the name of coffee you want (espresso /  latte / cappuccino): "))

    def resourceChecker(name):
        if milk< items[name]['milk'] or coffee< items[name]['coffee'] or water < items[name]['water']:
            return False
        else:
            return True
    # print report
    if userChoice.lower()=='report':
        reports()
    
    else:
        if resourceChecker(userChoice)==True:
            price =items[userChoice]['price']
            print(f"Please Pay ${price} for your {userChoice} in Coin")
            penny = float(input("Enter the penny: $"))
            dime = float(input("Enter the dime: $"))
            nickel = float(input("Enter the nickel: $"))
            quarter = float(input("Enter the quarter: $"))

        # Calculating the total coin received by the users
            userCoin = penny*penn + dime*dim + nickel*nicke + quarter*quarte
            print(f"The total amount you inserted is: ${round(userCoin, 2)}")


            
            #check transactional successful
            if userCoin ==float(price):
                print("Please wait for 1 minutes for your Coffee")
                print("Here is your Coffee: ☕")
                milk = machine['milk'] - items[userChoice]['milk']
                coffee = machine['coffee'] - items[userChoice]['coffee']
                water = machine['water'] - items[userChoice]['water']

            elif userCoin> float(price):
                userCoin -=price
                print(f"Here is your Return Amount: ${round(userCoin, 2)}")
                print("Please wait for 1 minutes for your Coffee")
                print("Here is your Coffee: ☕")
                milk = machine['milk'] - items[userChoice]['milk']
                coffee = machine['coffee'] - items[userChoice]['coffee']
                water = machine['water'] - items[userChoice]['water']
            else:
                print("Insufficient Coin")
                print(f"Here is your Refundable Amount: ${round(userCoin, 2)}")
        else:
            print(f"Insufficient Resource to make {round(userCoin, 2)}")

    another = str(input("Enter 'yes' to get another coffee: "))
    if another.lower()=='yes':
        anotherCoffee= False
    else:
        anotherCoffee = True