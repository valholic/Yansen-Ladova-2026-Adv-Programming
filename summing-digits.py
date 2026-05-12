while True:
    n = input()
    
    if n == "0":
        break
    
    while len(n) > 1:
        digits_sum = sum(int(digit) for digit in n)
        n = str(digits_sum)
    
    print(n)