# Problem 11: Temperature Converter Class
# Scenario: Convert temperature values
# Task: Convert Celsius and Fahrenheit

class Temperature:

    def to_celsius(self, f):
        return (f - 32) * 5 / 9

    def to_fahrenheit(self, c):
        return (c * 9 / 5) + 32


# Creating object
t = Temperature()

# Printing converted value
print(t.to_fahrenheit(0))