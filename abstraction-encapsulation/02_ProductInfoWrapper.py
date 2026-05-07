# Problem 2: Product Info Wrapper

class Product:

    def __init__(self, name, product_id):
        self.name = name
        self.__id = product_id

    # Getter method
    def get_id(self):
        return self.__id


# Taking input from the user
name = input("Enter product name: ")
product_id = int(input("Enter product ID: "))

p = Product(name, product_id)

print(p.get_id())