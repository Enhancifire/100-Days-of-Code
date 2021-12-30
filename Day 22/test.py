import pandas

data = pandas.read_csv("Day 22/weather_data.csv")
# print(data)

dic_data = data.to_dict()
print(dic_data)

# mean = data["temp"].mean()
# print(mean)

# max = data.temp.max()
# print(max)

# Get data in row
# monday = data[data.day == "Monday"]
# montemp = int(monday.temp) * 9/5 + 32
# print(montemp)

