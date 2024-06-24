# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}

word = input("Enter a word: ").upper()
output_list = [nato_alphabet[letter] for letter in word]
print(output_list)
