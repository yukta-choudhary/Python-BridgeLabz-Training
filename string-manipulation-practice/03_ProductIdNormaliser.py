# Question:
# Problem 3: Product ID Normalizer
# Standardize IDs to format "PROD-XXX"

def normalize_ids(id_list):
    result = []
    
    for item in id_list:
        item = item.replace("_", "-")
        item = item.upper()
        result.append(item)
    
    return result

# input
data = input("Enter product IDs (comma separated): ")
ids = data.split(",")

print("Normalized IDs:", normalize_ids(ids))