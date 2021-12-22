from prettytable import PrettyTable

x = PrettyTable()
x.add_column("City Name", ["Chopda", "Jalgaon", "Pune"])
x.add_column("Distance from Chopda", [0, 40, 400])
print (x)

