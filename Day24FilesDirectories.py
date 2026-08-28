# Reading or Writing to a File

# READING
with open("my_text.txt") as file:
    content = file.read()  # Contents data type will be a string.
    print(content)

# WRITING:
with open(
    "my_write.txt", mode="w"
) as file:  # If file is not already open, it will create from scratch.
    file.write("New text.")  # New text variable always needs to be a string.

#  Modes:  Read='r', Write='w' (this replaces existing text), Append='a'


# Paths
# Absolute file paths always start at the root (C: in windows, / in Mac/Linux)
# Relative file paths start in the current working directory.
#       ./<filename> means look in current folder (./- Optional) for filename <filename>.
#       ../<filename> means look one directory above (.//) for filename <filename>
#
# Jumping Up Multiple Directories:  ../.. (2)  or ../../.. (3) etc.
