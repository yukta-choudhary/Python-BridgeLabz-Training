# Question:
# Problem 4: URL Parser
# Separate base URL and path

def parse_url(url):
    parts = url.split("/")
    
    base = parts[0] + "//" + parts[2]
    path = "/" + "/".join(parts[3:])
    
    return base, path

# input
url = input("Enter URL: ")

base, path = parse_url(url)

print("Base URL:", base)
print("Path:", path)