# this project is not complete there is something needed to fix 
# like once you play this game and you are asked if you wanna play this game
# instead of replaying the game this program exit
#  and one more feature can be added in this like the number of times this games


print("""--------------ROCK PAPER SCISSOR---------------
    -------LET'S PLAY THE GAME---------------------
    -------RULES--------------------
    -------ROCK BEATS SCISSOR--------------
    -------SCISSOR BEATS PAPER---------------
    --------PAPER BEATS ROCK-----------------""")

import random
values = ['r', 'p','s']
score = 0
def wannaPlay():
    play= input("Do you want to play this game?(Y/N)")
    if play.lower() =='y':
        return True
if wannaPlay() ==False:
    print("OKAY SOME OTHER TIME MATE!!")
else:
    print("---Let's the game begin---")
    choice = input("\n Choose one (Rock or Paper or Scissor ) as (R/P/S): ")
    choice = choice.lower()
    aiChoice = random.choice(values)
    # Conditions for games
    if choice=='r' and aiChoice =='r':
        choice = input("\n Choose one (Rock or Paper or Scissor ) as (R/P/S): ")
        choice = choice.lower()
        aiChoice = random.choice(values)
        
    elif choice =='r' and aiChoice =='p':
        score = score
        print("You Lose.... Your score is: ", score)
        wannaPlay()
    elif choice =='p' and aiChoice =='p':
        choice = input("\n Choose one (Rock or Paper or Scissor ) as (R/P/S): ")
        choice = choice.lower()
        aiChoice = random.choice(values)
        
    elif choice =='s' and aiChoice =='s':
       
       choice = input("\n Choose one (Rock or Paper or Scissor ) as (R/P/S): ")
       choice = choice.lower()
       aiChoice = random.choice(values)
    elif choice =='p' and aiChoice=='s':
        score = score
        print("You Lose.... Your score is: ", score)
        wannaPlay()
    elif choice =='s' and aiChoice=='r':
        score = score
        print("You Lose.... Your score is: ", score)
        wannaPlay()
    elif(choice =='r' and aiChoice =='s') or(choice=='p' and aiChoice=='r') or(choice=='s' and aiChoice=='p'):

        score = score +1
        print("----------Hurrey! YOU WON")
        print("-------Score =>",score)
        wannaPlay()
    else:
        print("Wrong Input")
        wannaPlay()


