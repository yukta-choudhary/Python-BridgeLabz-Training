# Problem 12: Read-only Configuration Class

class Config:

    def __init__(self, version):
        self.__version = version

    # Getter method
    def get_version(self):
        return self.__version


# Taking input from the user
version = input("Enter version: ")

c = Config(version)

print(c.get_version())