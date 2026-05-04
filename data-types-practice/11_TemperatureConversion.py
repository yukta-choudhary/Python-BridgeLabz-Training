# Question:
# Convert user-input temperature from string to float and print both Celsius and Fahrenheit equivalents.

temp = input("Enter temperature in Celsius: ")

celsius = float(temp)
fahrenheit = (celsius * 9/5) + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)