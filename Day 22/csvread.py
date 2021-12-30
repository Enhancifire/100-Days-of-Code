import pandas as p
import csv

# with open("Day 22/weather_data.csv", "r") as csv:
#     data = csv.readlines()
#     print(data)

with open("Day 22/weather_data.csv", "r") as dataFile:
    data = csv.reader(dataFile)
    temperature = []

    for row in data:
        temperature.append(row[1])
    