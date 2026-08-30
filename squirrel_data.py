import pandas

data = pandas.read_csv("furry_data.csv")

grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

print(f"Grey = {grey}, Red = {red}, Black = {black}")

color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black],
}

output_data = pandas.DataFrame(color_dict)
output_data.to_csv("squirrel_output.csv")
