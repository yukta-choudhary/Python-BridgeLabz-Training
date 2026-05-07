# Problem 6: Encapsulated Vehicle Info

class Vehicle:

    def __init__(self, engine_number):
        self.__engine_number = engine_number

    # Getter method
    def get_engine_info(self):
        return "Engine Number: " + self.__engine_number


# Taking input from the user
engine_no = input("Enter engine number: ")

v = Vehicle(engine_no)

print(v.get_engine_info())