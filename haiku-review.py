import sys

def count_syllables(line):
    vowels = set("aeiouy")
    syllables = 0
    in_vowel_sequence = False
    
    for char in line:
        if char in vowels:
            if not in_vowel_sequence:
                syllables += 1
                in_vowel_sequence = True
        else:
            in_vowel_sequence = False
    return syllables

def solve():
    for line in sys.stdin:
        line = line.strip()
        if line == "e/o/i":
            break
            
        parts = line.split('/')
        expected = [5, 7, 5]
        result = 'Y'
        
        for i in range(3):
            if count_syllables(parts[i]) != expected[i]:
                result = str(i + 1)
                break
        print(result)

if __name__ == '__main__':
    solve()