# Question:
# Problem 3: Word Reverser
# Reverse each word in a sentence.

def reverse_words(sentence):
    words = sentence.split()
    result = []
    
    for w in words:
        result.append(w[::-1])
    
    return " ".join(result)

# input
text = input("Enter sentence: ")

print("Reversed:", reverse_words(text))