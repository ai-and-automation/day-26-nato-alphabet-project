# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 26 - Intermediate - List Comprehension
# NATO Alphabet Project

import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# new_dict = {index: {'Name': row['Name'], 'Age': row['Age'], 'Score': row['Score']} for index, row in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

# Ask user for the word that needs to be transcribed into phonetic code
word = input("Enter a word: ").upper()
# word = "TEST" # testing
# print(f"word = {word}") # testing

# Import the Nato Phonetic Alphabet
nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(f"nato_phonetic:\n{nato_phonetic}") # testing

# new_dict = {row['letter']: row['code'] for index, row in df.iterrows()}

# Create a dictionary from the NATO phonetic alphabet DataFrame
nato_dict = {row["letter"]: row["code"] for (index, row) in nato_phonetic.iterrows() if row.letter in word}
# or nato_dict = {row.letter: row.code for (index, row) in nato_phonetic.iterrows()}
# print(f"nato_dict = {nato_dict}") # testing

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Map each letter in the word to its NATO phonetic code
word_phonetic = [nato_dict[letter] for letter in word]
print(word_phonetic)

# Another way of doing it with a for loop
# word_phonetic = []
# for letter in word:
#      #print(letter) # testing
#     code = nato_phonetic[nato_phonetic["letter"] == letter].code.item()
#     # print(code) # testing
#     word_phonetic.append(code)
# print(word_phonetic)