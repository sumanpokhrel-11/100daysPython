
print("----------Secret Auction----------------")
import os
moreBidding = True
while moreBidding == True:
    name = str(input("What is Your Name?: "))
    bid_amount = int(input("How much bid do you want to place?: $"))

    bidder = {}
    bidder[name] = bid_amount
    other_bidder = input("Are there any other biddes? 'Yes' or 'No': ")
    if other_bidder.lower() =="no":
        moreBidding = False
    else:
        os.system('cls')

for bidName in bidder:
    highest = 0
    amount = bidder[bidName]
    if amount>highest:
        highest = amount
        win = bidName
    print(f"{bidName} is the highest bidder with the bid ${highest}")

        
