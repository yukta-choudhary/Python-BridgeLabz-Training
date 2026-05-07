# Problem 17: Secure User Account System

class User:

    def __init__(self, username, password):
        self.username = username
        self.__password = password

    # Method to verify password
    def verify_password(self, password):

        if password == self.__password:
            return True
        else:
            return False


# Taking input from the user
username = input("Enter username: ")
password = input("Enter password: ")

u = User(username, password)

check_password = input("Enter password to verify: ")

print(u.verify_password(check_password))