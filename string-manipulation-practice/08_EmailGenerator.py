# Question:
# Problem 8: Template-driven Email Generator
# Replace placeholders using data

def generate_email(template, data):
    return template.format(name=data["name"], order_id=data["order_id"])

# input
template = input("Enter template: ")

name = input("Enter name: ")
order_id = input("Enter order id: ")

data = {
    "name": name,
    "order_id": order_id
}

print("Generated Email:", generate_email(template, data))