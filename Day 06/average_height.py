student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for i in student_heights:
    total_height += i

print(round(total_height /len(student_heights)))