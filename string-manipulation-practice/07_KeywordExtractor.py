# Question:
# Problem 7: Resume Keyword Extractor
# Extract keywords like Python, Django

def extract_keywords(text, keywords):
    result = []
    
    words = text.lower().split()
    
    for key in keywords:
        if key.lower() in words:
            result.append(key)
    
    return result

# input
resume = input("Enter resume text: ")
keywords = ["Python", "Django"]

print("Found Keywords:", extract_keywords(resume, keywords))