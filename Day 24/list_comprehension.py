import pandas as pd

student_dict = {
    "student": ["Faiz", "Atultul", "Jahil"],
    "score": [98, 76, 69],
}

student_data_frame = pd.DataFrame(student_dict)

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

for (index, row) in student_data_frame.iterrows():
    print(row.student)