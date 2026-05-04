# Question:
# Implement a program that reads a list of values from a CSV-like string "23,45,67,12"
# Convert them to integers and calculate both mean and maximum value.

data = input("Enter numbers separated by comma: ")

nums = list(map(int, data.split(",")))

mean = sum(nums) / len(nums)
maximum = max(nums)

print("Mean:", mean)
print("Maximum:", maximum)