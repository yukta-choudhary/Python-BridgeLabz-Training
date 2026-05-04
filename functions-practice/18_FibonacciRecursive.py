# Question:
# Problem 9: Recursive Fibonacci Series Generator
# Generate Fibonacci series using recursion.

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def generate_fibonacci(n):
    result = []
    for i in range(n):
        result.append(fib(i))
    return result

# input
n = int(input("Enter number of terms: "))

print("Fibonacci:", generate_fibonacci(n))