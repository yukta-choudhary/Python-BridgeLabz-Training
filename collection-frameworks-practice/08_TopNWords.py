# Question:
# Problem 8: Top-N Frequent Words
# Return top N frequent words.

from collections import Counter

text = input("Enter text: ")
n = int(input("Enter N: "))

words = text.split()

count = Counter(words)

print("Top Words:", count.most_common(n))