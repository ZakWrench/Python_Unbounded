import random
import time
from collections import Counter

start1 = time.perf_counter()
random_numbers = [random.randint(1, 100) for _ in range(5_000_000)]
start1_1 = time.perf_counter()
print(start1_1 - start1)

# Write the numbers to a file
with open("random_numbers.txt", "w") as f:
    for number in random_numbers:
        f.write(str(number) + "\n")

start2 = time.perf_counter()
# Read the numbers from the file and assign them to a single tuple
with open("random_numbers.txt", "r") as f:
    numbers = tuple(int(line.strip()) for line in f)
print(start2 - start1_1)
start3 = time.perf_counter()
with open("random_numbers.txt", "r") as f:
    numbers = []
    while True:
        chunk = f.read(1024)  # read 1024 bytes at a time
        if not chunk:
            break
        numbers.extend(map(int, chunk.split()))
    numbers_tuple = tuple(numbers)
print(start3 - start2)
numbers_to_count = [6, 25, 32, 40, 56, 75, 88, 99]

# Create a Counter object and count the occurrences of the chosen numbers
counts = Counter(numbers_tuple)
occurrences = {number: counts[number] for number in numbers_to_count}

# Print the occurrences of the chosen numbers
print(occurrences)
