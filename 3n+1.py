# Before
def step(n, count=0):
    if n == 1:
        return count + 1
    elif n % 2 == 0:
        return step(n // 2, count + 1)
    elif n % 2 == 1:
        return step(3 * n + 1, count + 1)

i = int(input())
j = int(input())
cycle_length = []

for m in range(i, j):
    cycle_length.append(step(m))

print(f"{i} {j} {max(cycle_length)}")

# After
import sys

cache = {1: 1}

def collatz_length(n):
    original = n
    count = 0

    while n not in cache:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1

    cache[original] = count + cache[n]
    return cache[original]


for line in sys.stdin:
    i, j = map(int, line.split())
    start, end = i, j

    if i > j:
        i, j = j, i

    max_len = 0

    for n in range(i, j + 1):
        max_len = max(max_len, collatz_length(n))

    print(start, end, max_len)