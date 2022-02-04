try:
    file = open("a_file.txt")

except FileNotFoundError as e:
    print(e)
    file = open("a_file.txt", "w")

except KeyError as error:
    print(error)

else:
    content = file.read()
    print()

finally:
    raise TypeError("Made up error just to bug you")
