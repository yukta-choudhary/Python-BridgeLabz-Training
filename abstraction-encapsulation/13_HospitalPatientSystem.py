# Problem 13: Hospital Patient System

class Patient:

    def __init__(self, name, disease):
        self.__name = name
        self.__disease = disease

    # Method to show limited information
    def get_info(self):
        return "Patient: " + self.__name + " | Disease: Confidential"


# Taking input from the user
name = input("Enter patient name: ")
disease = input("Enter disease: ")

p = Patient(name, disease)

print(p.get_info())