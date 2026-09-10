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
    a_dictionary = {"key": "value"}
    print(a_dictionary["asasa"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")


# ---------Raising your own Exceptions----------

height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Enter a realistic height")

bmi = weight / height**2

print(bmi)


# ---------JSON (Javascript Object Notation)--------------
#
# JSON Library Commands
# 1.  json.dump(new data, opened file, indent number) -> Writes to a json file.
# 2.  json.load(opened file) -> Reads from a json file and returns a python dictionary
# 3.  json.update() --> Updates existing json dictionary with new data

# opened file = with open("filename.json", 'r' or 'w') as variable_name

# Updating:
# new_data = python dictionary of data
# with open('data.json','r') as data_file:
#     data = json.load(data_file)    -- This brings in current json dictionary.
#     data.update(new_data)          -- This adds the new_data to the existing data.
# with open('data.json', 'w') as data_file:
#     data.dump(data, data_file, indent=4)  -- This updates the data.json file with updated data.
