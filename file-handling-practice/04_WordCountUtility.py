# Problem 4: Word Count Utility
# Scenario: Count number of words in error_report.txt
# Task: Read file and print total number of words

def count_words():
    with open("error_report.txt", "r") as file:
        content = file.read()
        words = content.split()
        print("Total Words:", len(words))

count_words()