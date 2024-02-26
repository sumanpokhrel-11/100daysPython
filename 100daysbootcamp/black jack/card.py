import random
from result import Result
class Card(Result):
    
    def __init__(self):
        super().__init__()
        self.cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10']
        self.total_dealer_card = 0
        self.total_user_card = 0
    def chooseCard(self):
        self.card = random.choice(self.cards)
        return self.card
    
    def cardShuffle(self):
        # for user
        for i in range(2):
            self.user.append(self.chooseCard())
            self.total_user_card = self.total_user_card + int(self.user[i])
        print(self.user)
        print(self.total_user_card)
        # for dealer
        for i in range(2):
            self.dealer.append(self.chooseCard()) # use append to add items in the list
            self.total_dealer_card = self.total_dealer_card +int(self.dealer[i])
        print(self.dealer[0])

    def cardShuffle2(self):
        for i in range(1):
            self.user.append(self.chooseCard())
            self.total_user_card += int(self.user[i])
            print(self.user)
            print(self.total_user_card)
        for i in range(1):
            self.dealer.append(self.chooseCard())
            self.total_dealer_card+= int(self.dealer[i])
            print(self.dealer[0]) 