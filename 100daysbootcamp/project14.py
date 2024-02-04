#display art
print('''

╦ ╦╦╔═╗╦ ╦╔═╗╦═╗  ╦  ╔═╗╦ ╦╔═╗╦═╗  ╔═╗╔═╗╔╦╗╔═╗
╠═╣║║ ╦╠═╣║╣ ╠╦╝  ║  ║ ║║║║║╣ ╠╦╝  ║ ╦╠═╣║║║║╣ 
╩ ╩╩╚═╝╩ ╩╚═╝╩╚═  ╩═╝╚═╝╚╩╝╚═╝╩╚═  ╚═╝╩ ╩╩ ╩╚═╝

''')
import random, os
from project14s import objects

#generate a random search value from the list
playAgain = ''


def play():
    '''this function let's you play if you want to play even after you lose'''
    score = 0

    b = random.choice(objects)
    loopGame = True
    while loopGame:
        a = b
        b = random.choice(objects)

        while a == b:
            b = random.choice(objects)
        aName = a['name']
        bName = b['name']
        aValue = a['value']
        bValue = b['value']

        print(aName)
        print(bName)
        guess = str(input(f'Enter "a" for {aName} "b" for {bName}:  '))
        guess = guess.lower()


        def checker(guess, aValue, bValue):
            '''this function checks if the correct guess is a or b'''
            if aValue>=bValue:                
                return guess =='a'
            else:
                return guess =='b'
            
            
        isCorrect = checker(guess, aValue, bValue)
        if isCorrect:
            score +=1
            os.system('cls')
            print("--------You are correct!----------")
            print(f"Your score is {score}")
            print(f'''  
                        The no. of searches for {aName} is  {aValue}
                        The no. of searches for {bName} is  {bValue}
    ''')
            
        else:
            print(f"""
                        -------------You are Wrong----------
                        The no. of searches for {aName} is  {aValue}
                        The no. of searches for {bName} is  {bValue}
                        Score is: {score}
                        You lose!!!!!!""")
            global playAgain
            playAgain  = str(input("Enter 'y' to Play again: else type anything but 'y': "))
            break


play()


if playAgain=='y':
    play()





    #format the search data into printable format

    #ask user for a guess

    #check if user is correct

    ##get no.of search for each search item
    ## use if statement to chieck if user is correct

    # give user feedback on their guess


    #score keeping

    #make the game repeatable

    #making search item at position B become the next item at position A

    #clear the screen between rounds