# Question:
# Scenario: Process customer feedback scores.
# Task: Calculate average and print satisfaction level.

n = int(input("Enter number of feedback scores: "))

scores = []

for i in range(n):
    score = float(input("Enter score: "))
    scores.append(score)

total = 0
for s in scores:
    total += s

avg = total / n

print("Average:", avg)

if avg >= 4.0:
    print("High Satisfaction")
else:
    print("Needs Improvement")