# Question:
# Problem 1: Personalized Greeting Function
# Write a function generate_greeting(name) that returns a greeting message.

def generate_greeting(name):
    return "Hello, " + name + "! Welcome back!"

# input
name = input("Enter name: ")

print(generate_greeting(name))