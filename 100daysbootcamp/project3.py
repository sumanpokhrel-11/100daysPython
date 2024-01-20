print("""---------------Welcome to the clsTreasure Hunt-------------------
---------you are given choices whether to go this way or that way or to attack or wait------- 
------------based on that you will move forward towards treasure or die--------------
-----------if you're lucky enough, you will eventually get the treasure--------------""")

def start():
    play = input("\nAre you ready to hunt the treasure? {Y/N}: ")
    if play.lower()=="y":
        return True
    else:
        return False

treasure = 0
health= 100
if start()==False:
    print(f"You have collected {treasure} treasure")
elif health ==0:
    print("------------You are dead--------")
else:
    print("""----------Let's the hunt begin------------
    ------------you are in the middle of the jungle--------
    ---------you have to find the way to the treasure following your instincts and your guts--------
    -------there are multiple enemies in the way which are deadly enough to kill you in a moment--------
    -------where some enemies may lose your health by some point------------
    --------if your health reaches to zero you're dead---------------
    -------------if you found the treasure you won----------------------
          -----------so let's gooooooooooooooo---------------------""")
    
    choice1 = input("\n Make a move either to left or right(L/R): ")
    if choice1.lower() == "l":
        print("Venomous Snake bite you")
        health = 0
    if choice1.lower() =='r':
        print("You've reached the sea shore")
        print("""---You see a boat there ---
              ---it could be a trap or ride to the treasure---
              ---think wisely---""")
        choice2 = input("\Do you want to take the boat or not? (Y/N): ")
        if choice2.lower()=='n':
            print("Wrong Choice!! next boat will arive full of other treasure hunter which will kill you")
            health = 0
        if choice2.lower()=="y":
            print("Great Choice!! Let's move onto the next journey")
            print("""---After taking the boat to the next shore, you see a forest----
                  ----in the bank you see a direction towards forest---
                  ---choose if you want to go to the next shore or follow the direction towards forest---""")
            choice3 = input("Do you want to go inside the forest or not? (Y/N): ")
            if choice3.lower()=="n":
                print("Bad choice!! You will never find the treasure outside that forest")
            if choice3.lower()=="y":
                print("Oh! What a brave choice. Let's see what you destiny awaits")
                print("""---You go deep inside the forest and you are tired---
                  ---you see a mushroom which could be edible or poisonous---""")
                choice4 = input("Do you want to eat the mushroom?(Y/N): ")
                if choice4.lower()=='y':
                    print("The mushroom was poisonous, you died!!!")
                if choice4.lower()=="n":
                    print("Good choice, we should not be desperate in this situation")
                    print("""---Now you finally reach in the center of the forest---
                  ---there is a statue of the king---
                  ---the treasure could be buried beneath the statue or it could be a trap---""")
                
        
                    choice5 = input("Do you want to dig the statue?(Y/N): ")
                    if choice5.lower() =='y':
                        print("""--------------You found the treasure--------------
                  -----------------------------------------------------
                  -----------------------------------------------------
                  -------------------YOU WON---------------------------
                  -----------------------------------------------------""")
                    else:
                        print("You will never found the treasure at any other place!!!")
                        print("""--------------You Lose--------------------""")