# Scenario: A project dashboard contains a tuple of project codes.
# Task: Display all project codes and verify that the tuple is immutable.
# Hint: Try modifying one element and observe the result.*

project_tuple = ("P101", "P102", "P103")

# displaying project codes
print("Project Codes are:")
for code in project_tuple:
    print(code)

# trying to modify tuple (immutability check)
try:
    project_tuple[0] = "NEWCODE"
except TypeError as e:
    print("\nTuple is immutable!")
    print("Error:", e)