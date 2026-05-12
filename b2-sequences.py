# After
import sys

data = list(map(int, sys.stdin.read().split()))
idx = 0
case = 0
while idx < len(data):
    n = data[idx]
    idx += 1
    b = data[idx:idx+n]
    idx += n
    case += 1
    ok = True
    
    if b[0] < 1:
        ok = False
    for i in range(1, n):
        if b[i] <= b[i-1]:
            ok = False
            break
    if ok:
        seen = set()
        for i in range(n):
            for j in range(i, n):
                s = b[i] + b[j]
                if s in seen:
                    ok = False
                    break
                seen.add(s)
            if not ok:
                break
    print(f"Case #{case}: It is {'a' if ok else 'not a'} B2-Sequence.")

# Before
def is_b2_sequence(seq):
    if len(seq) == 0 or seq[0] < 1:
        return False

    for i in range(1, len(seq)):
        if seq[i] <= seq[i - 1]:
            return False

    seen_sums = set()
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            s = seq[i] + seq[j]
            if s in seen_sums:
                return False
            seen_sums.add(s)

    return True

data = list(map(int, input().split()))

if is_b2_sequence(data):
    print("It is a B2-Sequence.")   
else:
    print("It is not a B2-Sequence.")