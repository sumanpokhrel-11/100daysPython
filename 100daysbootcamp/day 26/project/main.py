import pandas as pd

data = pd.read_csv('100daysbootcamp\day 26\project\phonetic_alphabet.csv')
# print(data.code)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = str(input("Enter a word:  ")).upper()
final = [nato[letter] for letter in user_input]

print(final)