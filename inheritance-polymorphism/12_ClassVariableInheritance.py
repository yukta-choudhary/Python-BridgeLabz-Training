# Problem 12: Class Variable Inheritance
# Scenario: Shared company name
# Task: Access class variable from subclasses

class Company:

    # Class variable
    name = "TechCorp"


class HR(Company):
    pass


class IT(Company):
    pass


# Printing class variable
print(HR.name, IT.name)