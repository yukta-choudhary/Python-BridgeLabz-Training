# Question:
# Problem 1: Customer Region Tracker
# Return a sorted list of unique regions.

data = input("Enter regions (comma separated): ")
regions = data.split(",")

unique_regions = list(set(regions))
unique_regions.sort()

print("Unique Sorted Regions:", unique_regions)