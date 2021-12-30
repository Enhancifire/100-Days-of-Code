import pandas as pd

data = pd.read_excel("Day 22/Teens Favorite Apps.xlsx")

# print(data)

appData = data[data.App == "Snapchat"]
print(appData)

# meanofSnap = data[data.App == "Snapchat"].max()
# print(meanofSnap)