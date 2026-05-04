# Question:
# Problem 6: CSV Text Cleaner
# Clean unwanted symbols and spaces

def clean_text(text):
    text = text.replace("!!", "")
    text = text.replace(",,", ",")
    
    parts = text.split(",")
    
    clean_parts = []
    for p in parts:
        p = p.strip()
        if p != "":
            clean_parts.append(p)
    
    return ", ".join(clean_parts)

# input
data = input("Enter CSV text: ")

print("Cleaned text:", clean_text(data))