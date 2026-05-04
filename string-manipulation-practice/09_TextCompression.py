# Question:
# Problem 9: Text Compression Simulation
# Replace repeating characters with char + count

def compress(text):
    result = ""
    count = 1
    
    for i in range(len(text)):
        if i < len(text) - 1 and text[i] == text[i+1]:
            count += 1
        else:
            result += text[i] + str(count)
            count = 1
    
    return result

# input
text = input("Enter text: ")

print("Compressed text:", compress(text))