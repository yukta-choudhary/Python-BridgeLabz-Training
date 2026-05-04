# Taking input in a tuple

n = int(input("Enter number of project codes: "))

codes = []
for i in range(n):
    code = input("Enter code: ")
    codes.append(code)

project_tuple = tuple(codes)

print("Tuple is:", project_tuple)