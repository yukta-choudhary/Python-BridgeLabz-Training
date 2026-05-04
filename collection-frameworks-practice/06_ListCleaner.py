# Question:
# Problem 6: List Comprehension Cleaner
# Remove empty or null values.

data = input("Enter values (comma separated, use None for null): ").split(",")

clean_list = [x for x in data if x != "" and x != "None"]

print("Cleaned List:", clean_list)