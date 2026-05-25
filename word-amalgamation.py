import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    
    iterator = iter(input_data)
    
    dictionary_words = []
    for line in iterator:
        line = line.strip()
        if line == "XXXXXX":
            break
        if line:
            dictionary_words.append(line)

    dictionary_words.sort()
    anagram_map = {}
    for word in dictionary_words:
        sorted_key = "".join(sorted(word))
        if sorted_key not in anagram_map:
            anagram_map[sorted_key] = []
        anagram_map[sorted_key].append(word)
        
    for line in iterator:
        line = line.strip()
        if line == "XXXXXX":
            break
        if not line:
            continue
            
        scrambled_word = line
        sorted_scrambled = "".join(sorted(scrambled_word))
        
        if sorted_scrambled in anagram_map:
            for matched_word in anagram_map[sorted_scrambled]:
                print(matched_word)
        else:
            print("NOT A VALID WORD")
            
        print("******")

if __name__ == "__main__":
    solve()