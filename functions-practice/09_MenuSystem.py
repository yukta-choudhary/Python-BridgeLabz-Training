# Question:
# Problem 9: Function-Based Menu System
# Display menu and take user choice.

def display_menu(options):
    for key in options:
        print(key + ". " + options[key])
    
    choice = input("Select an option: ")
    
    if choice in options:
        print("You selected:", options[choice])
    else:
        print("Invalid choice")

# menu data
options = {
    "1": "Start Process",
    "2": "Stop Process"
}

display_menu(options)