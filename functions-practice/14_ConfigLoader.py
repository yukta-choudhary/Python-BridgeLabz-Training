# Question:
# Problem 5: Config Loader
# Return value from dictionary or default.

def load_config(config, key, default_value=None):
    if key in config:
        return config[key]
    return default_value

# input
config = {}
n = int(input("Enter number of config items: "))

for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    config[k] = v

key = input("Enter key to search: ")

print("Value:", load_config(config, key, "Not Found"))