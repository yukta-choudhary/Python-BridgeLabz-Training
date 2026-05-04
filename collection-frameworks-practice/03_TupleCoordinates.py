# Question:
# Problem 3: Tuple-Based Coordinates
# Print coordinates using tuple unpacking.

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
z = int(input("Enter Z: "))

coords = (x, y, z)

a, b, c = coords

print("Coordinates: X=", a, ", Y=", b, ", Z=", c)