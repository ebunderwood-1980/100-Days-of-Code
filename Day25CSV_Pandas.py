# CSV Data and using Panda

# A way to store tabular data.  Stands for comma separated values.

# with open("weather_data.csv") as data_file:
#     lines = data_file.readlines()

# cleaned_list = [item.strip() for item in lines]

# print(cleaned_list)

import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


# Pandas = Python data analysis
# Data Frame is whole table
# Series is a column

import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()

temp_list = data["temp"].to_list()

print(data_dict)
print(temp_list)

print(f"Average temperature is {sum(temp_list) / len(temp_list)}")
print(f"Average Pandas Temperature is {data['temp'].mean()}")
print(f"Max of the Pandas Temperature is {data['temp'].max()}")

# Can also access series by data.day, data.condition, data.temp.

# How to get hold of rows of data.
print(f"Row = {data[data.day == 'Monday']}")  # Prints out entire Monday row.
max_temp = data[
    data.temp == data.temp.max()
]  # Prints out entire row that contains the hottest temperature.
print(f"Max temp row is:  \n{max_temp}")

monday = data[data.day == "Monday"]
monday_temp = monday.temp
adjusted_temp = (monday_temp * 1.8) + 32
print(f"Adjusted temperature = {adjusted_temp}")

# Create a dataframe from scratch
score_dict = {
    "students": ["Eric", "Tomack", "Nyxie"],
    "scores": [76, 56, 65],
}

# Turns my dictionary into a dataframe and then saves that dataframe in .csv format into a file
my_dataframe = pandas.DataFrame(score_dict)
data.to_csv("student_data.csv")
