# Before
number = int(input("Enter a number: ")) 
first_number = number 
seen = [] 
while True: 
    total = 0 
    while number > 0: 
        temp = number % 10 
        total += temp ** 2 
        number = number // 10 
    if total == 1: 
        print(f"{first_number} is a Happy number!") 
        break 
    if total in seen: 
        print(f"{first_number} is an Unhappy number.") 
        break 
    seen.append(total) 
    number = total

# After
def is_happy(n):
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    
    return n == 1

t = int(input())

for i in range(1, t+1):
    n = int(input())
    
    if is_happy(n):
        print(f"Case #{i}: {n} is a Happy number.")
    else:
        print(f"Case #{i}: {n} is an Unhappy number.")