from bet import Bet
class Result(Bet):
    def __init__(self):
        super().__init__()
        self.total_user_card = 0
        self.total_dealer_card = 0
        self.user = []
        self.dealer = []

    def result(self):
        '''Checks who won the game!!! '''
        if self.total_user_card> 21:
            print( f"Dealer Wins with values {self.dealer}")
            return False
        elif self.total_dealer_card>21:
            print(f"You Won!! with values {self.user}")
            return True
        elif (21 - self.total_dealer_card)< (21- self.total_user_card):
            print(f"Dealer Won with values {self.total_dealer_card} and cards {self.dealer}")
            return False
        elif(21-self.total_user_card) <(21 - self.total_dealer_card):
            print(f"You Won with values {self.total_user_card} and cards {self.user}")
            return True
        
    def calculation(self):
        if self.result():
            self.bet_available = self.bet_available + 2*self.bet_amount
        elif not self.result():
                self.bet_available =self.bet_available 
        else:
                self.bet_available = self.bet_available + self.bet_amount