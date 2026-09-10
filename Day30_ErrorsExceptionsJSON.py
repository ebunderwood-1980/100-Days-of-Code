# --------Types of Excpetions-----------

# FileNotFound Error:
# with open("a_file.txt") as file:
#     file.read()

# KeyError:
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]
#

# TypeError:
#  text = "abc"
#  print(text+5)
#

# IndexError:
# fruit_list = ["apple", "pear", "grapes"]
# fruit = fruit_list[3]

# ------Catching Exceptions (try, except, else, finally)-----

# Try:  Something that might cause an excpeption
# Except:  Do this if there was an exception
# Else:  Do this if there was no exception
# Finally:  Do this no matter what happens

try:
    file = open("a_file.txt")
except:
    file = open("a_file.txt", "w")
    file.write("Something")
