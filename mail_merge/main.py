# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# TODO: Pull all names out of ./Input/Names/invited_names.txt and put into a list.  Strip whitespace from every item in the list.
with open("./Input/Names/invited_names.txt") as input_file:
    names_list = input_file.readlines()

cleaned_list = [item.strip() for item in names_list]

# TODO Pull out the letter out of ./Input/Letters/starting_letter and store it in template
with open("./Input/Letters/starting_letter.txt") as template_file:
    letter_template = template_file.read()


# TODO For each name in name list, pull out name, paste it in template, and save to ./Output/ReadyToSend/letter_for_<person>.txt

for name in cleaned_list:
    new_letter = letter_template.replace("[name]", name)
    new_filename = f"letter_for_{name}.txt"
    with open(f"./Output/ReadyToSend/{new_filename}", mode="w") as file:
        file.write(new_letter)

# TODO Collect your loot!
