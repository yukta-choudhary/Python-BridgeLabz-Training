# Question:
# Problem 8: Analytics Utility Package
# Return average, max, min.

def get_stats(data):
    avg = sum(data) / len(data)
    return {
        "average": avg,
        "max": max(data),
        "min": min(data)
    }

# input
nums = list(map(int, input("Enter numbers: ").split(",")))

print(get_stats(nums))