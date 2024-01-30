print("""Welcome to the number Guessing Game.
      ------Guess the number between 1 to 100------
      -----2 options are given i.e. Easy and Hard-------
      --------Easy level contains 10 available guesses whereas Hard level contains 5 attempts to guess-----""")


import random
def check(): 
    '''return if the guessed number is exact or wrong based on multiple attempts'''  
    randomNumber = random.randint(1,100) 
    level = str(input("Enter the lever of difficulty, 'easy' or 'hard' :"))
    attempt = 0
    if level.lower()=='easy':
        attempt = 10
    else:
        attempt = 5
    while attempt !=0:
        guess = int(input("Enter a number between 1 to 100: "))
        attempt = attempt - 1
        if guess>randomNumber:
            print("Too high")
            print(f"Attempt remainings are {attempt}")
        elif guess<randomNumber:
            print("Too low")
            print(f"Attempt remainings are {attempt}")
        else:
            print("You won")
            break
    if attempt==0:
        return("You ran out of attempts better luck next time")
    else:
        return("Hurry")

print(check())
def again():
        '''return True if the users want to play again '''
        play_again = str(input("Enter 'y' to play again: "))
        if play_again.lower() =='y':
            return True
        else:
            return False
while again():
    check()
