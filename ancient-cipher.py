import sys

def solve():
    # Read all lines from standard input
    input_data = sys.stdin.read().split()
    
    # Process pairs of strings
    i = 0
    while i < len(input_data):
        s1 = input_data[i]
        s2 = input_data[i+1]
        i += 2
        
        # If lengths differ, it's impossible (though problem says equal length)
        if len(s1) != len(s2):
            print("NO")
            continue
            
        # Count occurrences of each letter A-Z
        count1 = [0] * 26
        count2 = [0] * 26
        
        for char in s1:
            count1[ord(char) - ord('A')] += 1
        for char in s2:
            count2[ord(char) - ord('A')] += 1
            
        # Sort the frequency counts
        count1.sort()
        count2.sort()
        
        # Compare the distribution of frequencies
        if count1 == count2:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()