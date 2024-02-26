
class Bet:
    def __init__(self):
        self.bet_available = int(5000)

    def betFunction(self,bet_available, bet_amount):
        self.bet_amount = int(input("How much do you want to place bet eg. $10, $100, $500, $1000 : $"))
        self.bet_available = bet_available
        self.bet_amount = bet_amount
        self.bet_available -= self.bet_amount
        return self.bet_available
    