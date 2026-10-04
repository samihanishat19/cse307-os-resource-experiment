import time

# Fixed workload parameters
SIZE = 8_000_000
ROUNDS = 5

print("Starting fixed memory/CPU workload...")

start = time.time()

# Allocate a large list in memory
data = list(range(SIZE))

# Perform repeated computation on the same data
total = 0

for r in range(ROUNDS):
    for x in data:
        total += x % 100

end = time.time()

print("Result:", total)
print("Execution time:", round(end - start, 2), "seconds")
