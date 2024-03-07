print('''--------Black Jack-------------''')

import random
cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10']
# print((cards))
bet_available = 5000
print(f"The available bet amount is: ${bet_available}")

def betFunction(bet_available, bet_amount):
    
    bet_available -= bet_amount
    return bet_available

# print (betFunction(bet_available, bet_amount))
total_user_card = 0 
total_dealer_card = 0 
wannaPlay = 'yes'


while wannaPlay=='yes' and bet_available>0:
    user = []
    dealer = []
    bet_amount = int(input("How much do you want to place bet eg. $10, $100, $500, $1000 : $"))
    bet_available = betFunction(bet_available, bet_amount)
    def chooseCard():
        card = random.choice(cards)
        return card
    first_time_shuffle = True
    betFunction(bet_available, bet_amount)
    deal = str(input("Enter 'Yes' to deal else 'No' to hit: "))
    while deal.lower() =='yes':
        if first_time_shuffle ==True:
            
            if deal.lower() =='yes':
                # for user
                for i in range(2):
                    user.append(chooseCard())
                    total_user_card = total_user_card + int(user[i])
                print(user)
                print(total_user_card)
                # for dealer
                for i in range(2):
                    dealer.append(chooseCard()) # use append to add items in the list
                    total_dealer_card = total_dealer_card +int(dealer[i])
                print(dealer[0])
                first_time_shuffle = False


                def result():
                    '''Checks who won the game!!! '''
                    if total_user_card> 21:
                        print( f"Dealer Wins with values {dealer}")
                        return False
                    elif total_dealer_card>21:
                        print(f"You Won!! with values {user}")
                        return True
                    elif (21 - total_dealer_card)< (21- total_user_card):
                        print(f"Dealer Won with values {total_dealer_card} and cards {dealer}")
                        return False
                    elif(21-total_user_card) <(21 - total_dealer_card):
                        print(f"You Won with values {total_user_card} and cards {user}")
                        return True
                  

        else:
            if deal.lower() == 'yes':
                for i in range(1):
                    user.append(chooseCard())
                    total_dealer_card + int(user[i])
                print(user)
                print(total_user_card)
                for i in range(1):
                    dealer.append(chooseCard())
                    total_dealer_card+= int(dealer[i])
                print(dealer[0])
            else:
                result()
        if result():
            bet_available = bet_available + 2*bet_amount
        elif not result():
                bet_available =bet_available 
        else:
                bet_available = bet_available + bet_amount
        wannaplay = input("Enter 'yes' to play again: ")
        print(f"The available bet is: ${bet_available}")
        if wannaplay.lower() =='no':
            break 






