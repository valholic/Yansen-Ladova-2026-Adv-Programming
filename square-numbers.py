import math

total = 0

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    for i in range(a, b + 1):
        if math.sqrt(i).is_integer():
            total += 1
    print(total)
    total = 0