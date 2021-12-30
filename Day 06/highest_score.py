scores = input("Please input the scores: ").split(", ")

for i in range(0, len(scores)):
    scores[i] = int(scores[i])

highest_score = 0

for i in scores:
    if i > highest_score:
        highest_score = i

print(highest_score)