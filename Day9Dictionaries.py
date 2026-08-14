# Dictionary Example
programming_dictionary = {
    "bug": "An error in a program that prevents the program from running as expected",
    "function": "A piece of code that you can easily call over and over again",
    "loop": "The action of doing something over and over again",
}

print(programming_dictionary["function"])

programming_dictionary["third thing"] = "This is a fourth thing"
print(programming_dictionary)

# Wiping out a dictionary
# programming_dictionary = {}

# Looping through a dictionary to print keys.
for key in programming_dictionary:
    print(programming_dictionary[key])
    print(key)

# Grading paradigm
student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60,
}

student_grades = {}

for key in student_scores:
    if 90 <= student_scores[key] <= 100:
        student_grades[key] = "A"
    elif 80 <= student_scores[key] <= 89:
        student_grades[key] = "B"
    elif 70 <= student_scores[key] <= 79:
        student_grades[key] = "C"
    elif 60 <= student_scores[key] <= 69:
        student_grades[key] = "D"
    else:
        student_grades[key] = "F"

print(f"Student Dictionary\n{student_grades}")


# Nesting lists in dictionaries.
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
}

# Print Lille
print(f"This should be Lille:  {travel_log['France'][1]}")

# Print out D
nested_list = ["A", "B", ["C", "D"]]
print(f"This should be D:  {nested_list[2][1]}")
