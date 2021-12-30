import pandas as p

data = p.read_csv("Day 22/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cinnamonSquirrelsLen = len(data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].to_list())
greySquirrelsLen = len(data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].to_list())
blackSquirrelsLen = len(data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].to_list())

print(f"{cinnamonSquirrelsLen = }")
print(f"{greySquirrelsLen = }")
print(f"{blackSquirrelsLen = }")

new_data = {
    'Fur Color': {
        0: "Cinnamon",
        1: "Gray",
        2: "Black",
    },
    'Count': {
        0: cinnamonSquirrelsLen,
        1: greySquirrelsLen,
        2: blackSquirrelsLen,
    }
}

newDF = p.DataFrame(new_data)

newDF.to_csv("Day 22/SquirrelCount.csv")