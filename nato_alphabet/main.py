# student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# # Looping through dictionaries:
# for key, value in student_dict.items():
#     # Access key and value
#     pass

# import pandas

# student_data_frame = pandas.DataFrame(student_dict)

# # Loop through rows of a data frame
# for index, row in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# # TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

# Import CSV using pandas
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Take nato_csv dataframe and turn it into a dictionary {'A': 'Alfa'}
nato_dictionary = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
# Get the user input word

# Create the nato translation.
while True:
    try:
        user_word = input("Please enter the word you would like translated:  ").upper()
        nato_translation = [nato_dictionary[letter] for letter in user_word]
    except KeyError:
        print("Letters only please")
    else:
        print(nato_translation)
        break

# ------------Alternate Solution-----
# def generate_solution():
#    word = input("Enter a word:  ").upper()
#    try:
#        output_list = [nato_dictionary[letter] for letter in user_word]
#    except KeyError:
#        print("Sorry, only letters please")
#        generate_solution()
#    else:
#        print(output_list)
#
# generate_solution()
