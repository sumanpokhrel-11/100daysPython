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
def condition(user_choice, ai_choice):
    pass
# def wannaPlay():
#     play= input("Do you want to play this game?(Y/N)")
#     if play.lower() =='y':
#         return True
play = True
attempt = 0
while play:
    wanna_play= input("Do you want to play this game?(Y/N)")
    if wanna_play.lower() == 'y':
        play = True
        attempt +=1
    else:
        play = False
        break
        
    print("---Let's the game begin---")
    choice = input("\n Choose one (Rock or Paper or Scissor ) as (R/P/S): ").lower()
    aiChoice = random.choice(values)
    # Conditions for games
    if choice== aiChoice:
        print("Same choice! Tied")
        score = score
        if attempt==0:
            attempt = 0
        else:
            attempt -=1
        print(f"score is: {score}/{attempt}")
        
    elif choice =='r' and aiChoice =='p':
        score = score
        print(f"You Lose.... Your score is: {score}/{attempt}")
        # wannaPlay()
    
    elif choice =='p' and aiChoice=='s':
        score = score
        print(f"You Lose.... Your score is: {score}/{attempt}")

        # wannaPlay()
    elif choice =='s' and aiChoice=='r':
        score = score
        print(f"You Lose.... Your score is: {score}/{attempt}")
        # wannaPlay()
    elif(choice =='r' and aiChoice =='s') or(choice=='p' and aiChoice=='r') or(choice=='s' and aiChoice=='p'):

        score = score +1
        print("----------Hurrey! YOU WON")
        print(f"-------Score => {score}/{attempt}") 
        # wannaPlay()
    else:
        print("Wrong Input")
        # wannaPlay()


