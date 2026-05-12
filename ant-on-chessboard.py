# Before
def position(sec):
    x = 1
    y = 1

    for i in range(1, sec):
        if i % 4 == 1:
            y += 1
        elif i % 4 == 2:
            x += 1
        elif i % 4 == 3:
            y -= 1
        else:
            x -= 1

    return (x, y)

result = position(int(input()))
print(result[0], result[1])

# After
import math
import sys

def solve():
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        k = math.ceil(math.sqrt(n))
        prev_k = k - 1
        end_prev = prev_k * prev_k
        
        mid = end_prev + k

        if k % 2 != 0:
            if n <= mid:
                x, y = k, n - end_prev
            else:
                x, y = k - (n - mid), k
        else:
            if n <= mid:
                x, y = n - end_prev, k
            else:
                x, y = k, k - (n - mid)
        
        print(f"{x} {y}")

if __name__ == "__main__":
    solve()