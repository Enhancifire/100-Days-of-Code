print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, 0r 15? "))
people = float(input("How many people to split the bill? "))

output = (bill / people) * tip/100
output = (bill / people) + output

print("Each person should pay: $" + str(round(output, 2)))
