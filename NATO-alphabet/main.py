import pandas
# read csv file
nato_phonetic_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# Create a dictionary
phonetic_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet_df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

# don't have to convert it to a list
# list(answer.upper())

def convert_to_alphabet():
    answer = input("Tell me a word: ").upper()
    try:
        answer_alphabet = [phonetic_alphabet_dict[letter] for letter in answer]
        print(answer_alphabet)
    except KeyError:
        print("Sorry, only accept letters from the alphabet.")
        convert_to_alphabet()


convert_to_alphabet()
