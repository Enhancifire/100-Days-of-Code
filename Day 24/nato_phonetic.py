import pandas

nato_dict = pandas.read_csv("Day 24/nato_phonetic_alphabet.csv")

data_list = {row.letter:row.code for (index, row) in nato_dict.iterrows()}

# print(data_list)

name = input("Please enter your name: ").upper()
# print(name)

name_list = [data_list[letter] for letter in name]

print(name_list)