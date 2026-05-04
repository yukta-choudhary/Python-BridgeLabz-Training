# Question:
# Problem 4: Data Normalizer
# Convert names to lowercase and remove spaces.

def normalize_names(name_list):
    return [name.strip().lower() for name in name_list]

# input
names = input("Enter names (comma separated): ").split(",")

print("Normalized:", normalize_names(names))