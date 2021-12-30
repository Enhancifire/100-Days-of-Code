with open("Day 21/names.txt") as names:
    namelist = names.readlines()
    noOfNames = len(namelist)
    for name in namelist:
        filename = name.strip("\n")
        startingLetter = f"""Dear {filename},

You are invited to my birthday this Saturday.

Hope you can make it!

Faiz
"""

        f = open(f"Day 21/Mails/{filename}.txt", "w")
        f.write(startingLetter)
