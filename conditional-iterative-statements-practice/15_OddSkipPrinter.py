# Question:
# Problem 6: Odd Number Printer with Skip
# Print odd numbers from 1 to 30, skipping multiples of 5.

for i in range(1, 31):
    if i % 2 == 0:
        continue
    if i % 5 == 0:
        continue
    print(i)