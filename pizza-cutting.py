# Before
def cut_pizza(lines):
    if lines < 0:
        return 0
    return (lines * (lines + 1)) // 2 + 1

lines = int(input())
print(cut_pizza(lines))

# After
def cut_pizza(n):
    return (n * (n + 1)) // 2 + 1

while True:
    try:
        n = int(input())
        
        if n < 0:
            continue
        
        print(cut_pizza(n))
        
    except EOFError:
        break