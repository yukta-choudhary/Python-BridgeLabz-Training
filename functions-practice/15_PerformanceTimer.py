# Question:
# Problem 6: Performance Timer
# Measure execution time of a function.

import time

def measure_time(func):
    start = time.time()
    func()
    end = time.time()
    print("Execution time:", (end - start), "seconds")

# example usage
measure_time(lambda: sum(range(100000)))