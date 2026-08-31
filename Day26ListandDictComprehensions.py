# List and Dictionary Comprehensions

"""
Usage:  new_list = [new_item for item in list]
    new_item is the operation you would like proformed on each item in the list

    The list really means anything that is iterable.
"""

# Example
numbers = [1, 2, 3]
new_list = [
    item + 1 for item in numbers
]  # Goes through numbers and adds one to every item, stores in new_list
print(new_list)

letters = "Eric"
letters_list = [letter for letter in letters]  # Creates a list of letters [E, R, I, C]
print(letters_list)

range_doubled = [number * 2 for number in range(1, 5)]
print(range_doubled)


#  List comprehension with conditionals
names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
short_names = [
    name for name in names if len(name) < 5
]  # Only prints out names if their length is less than 5 characters
print(short_names)

upper_names = [
    name.upper() for name in names if len(name) > 5
]  # Prints out all the names in the list that are longer than 5 letters in all capital letters
print(upper_names)

# Grabs a list of numbers from two files and prints out overlap using list comprehensions
with open("file1.txt") as file:
    file1 = file.readlines()

with open("file2.txt") as file:
    file2 = file.readlines()

file2_int = [int(num) for num in file2]
file1_int = [int(num) for num in file1]

result = [int(num) for num in file1 if num in file2]

print(result)


# ----------------------------------------------------------
# Dictionary Comprehensions
#
# Usage:
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
#
# ----------------------------------------------------------
import random

student_scores = {
    student: random.randint(1, 100) for student in names
}  # Creates dictionary with names from names and assigning a randome score to value

passed_students = {
    student: score for (student, score) in student_scores.items() if score >= 60
}  # Finds all students from student_scores and only pulls out the ones that have a score above 60
print(passed_students)


# ----------------------------------------------------------------
# Looping over pandas data frames
#
# ----------------------------------------------------------------

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# Looping through Dictionaries
for key, values in student_dict.items():
    print(values)

# Looping through Data Frames
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for index, row in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
