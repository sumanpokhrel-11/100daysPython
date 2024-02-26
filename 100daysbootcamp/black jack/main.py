print('''--------Black Jack-------------''')
from result import Result
from card import Card
from bet import Bet
cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10']
# print((cards))
result = Result()
card = Card()
print(f"The available bet amount is: $5000")
bet = Bet()

# print (betFunction(bet_available, bet_amount))

def wannaPlay():
        '''this functions checks if the user wants to play or not'''
        play = str(input("Enter 'yes' to play again: ")).lower()
        if play == "yes":
            return True
        else:
             return False
play = True
while play and bet.bet_available >=10:    
   
    first_time_shuffle = True
    # betFunction(bet_available, bet_amount)
    

    deal = str(input("Enter 'Yes' to deal else 'No' to hit: ")).lower()
    while deal.lower() =='yes':
        
        if first_time_shuffle:
            card.cardShuffle()

            first_time_shuffle = False
     

        else:
            if deal.lower() == 'yes':
                card.cardShuffle2()
            else:
                break
        deal = str(input("Enter 'Yes' to deal else 'No' to hit: ")).lower()
        if deal == 'yes':
            continue
        else:
            result.result()
            result.calculation()
        
    play = wannaPlay()
    print(f"The available bet is: ${bet.bet_available}")


print(result.result())
print(result.calculation())




