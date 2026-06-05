import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    
    if not input_data:
        return

    num_test_cases = int(input_data[0])
    for i in range(1, num_test_cases + 1):
        if i < len(input_data):
            line = input_data[i]
        else:
            line = ""
            
        if is_balanced(line):
            print("Yes")
        else:
            print("No")

def is_balanced(s):
    stack = []
    
    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
            
    return len(stack) == 0

if __name__ == '__main__':
    solve()