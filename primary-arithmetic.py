#Before
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    carry_count = 0
    while a > 0 or b > 0:
        d1 = a % 10
        d2 = b % 10
        s = d1 + d2   # BUG: forgot + carry
        if s >= 10:
            carry_count += 1
        a //= 10
        b //= 10
    if carry_count == 0:
        print("No carry operation.")
    elif carry_count == 1:
        print("1 carry operation.")
    else:
        print(f"{carry_count} carry operations.")

#After
def count_carry(a, b):
    carry = 0
    count = 0
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0 or j >= 0:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        total = digit_a + digit_b + carry
        
        if total >= 10:
            carry = 1
            count += 1
        else:
            carry = 0
        
        i -= 1
        j -= 1
    return count

while True:
    a, b = input().split()
    if a == "0" and b == "0":
        break
    result = count_carry(a, b)
    if result == 0:
        print("No carry operation.")
    elif result == 1:
        print("1 carry operation.")
    else:
        print(f"{result} carry operations.")