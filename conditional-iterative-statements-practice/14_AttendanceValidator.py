# Question:
# Problem 5: Attendance Validator
# Categorize attendance percentage.

attendance = int(input("Enter attendance percentage: "))

if attendance >= 90:
    print("Excellent")
elif attendance >= 75:
    print("Satisfactory")
else:
    print("Poor")