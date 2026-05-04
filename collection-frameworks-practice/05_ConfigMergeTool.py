# Question:
# Problem 5: Configuration Merge Tool
# Merge multiple config dictionaries.

config1 = {}
config2 = {}

n1 = int(input("Enter number of items in config1: "))
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    config1[key] = value

n2 = int(input("Enter number of items in config2: "))
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    config2[key] = value

# merging
config1.update(config2)

print("Merged Config:", config1)