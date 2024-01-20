
print('''------------Hangman Game---------------''')
import random
pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

# for pic in pics:
#     print(pic)

round = 0
choiceLeft= 7
word = random.choice(words)
# print(word)
blanks = len(word)
dash= []
for blank in range(0, blanks):
    dash += '_'
print(dash)
guessedWord = ''
# dass = '_'
while(dash!=list(word) and round<choiceLeft):

    guess = input("Enter a letter to Guess: ")
    guess.lower()
    if guess in word:
        for i in range(len(word)):
            letter = word[i]
            if guess == letter:

                dash[i] = (guess)
        print(dash)

    elif guess not in word:
        round +=1
        print(dash)
        print(pics[round-1])
    else:
         break
    

if dash == list(word):
        print("----------hurrey! You Won----------")
if round==choiceLeft:
     "---------YOU LOSE----------------"

    


