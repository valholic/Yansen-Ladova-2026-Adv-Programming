import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    
    if not input_data:
        return
        
    line_idx = 0
    case_num = 1
    
    while line_idx < len(input_data):
        try:
            num_words = int(input_data[line_idx].strip())
        except ValueError:
            break 
            
        line_idx += 1
        cool_word_count = 0
        
        for _ in range(num_words):
            if line_idx >= len(input_data):
                break
                
            word = input_data[line_idx].strip()
            line_idx += 1
            
            freq_map = {}
            for char in word:
                freq_map[char] = freq_map.get(char, 0) + 1
                
            if len(freq_map) < 2:
                continue
                
            frequencies = list(freq_map.values())
            unique_frequencies = set(frequencies)
            
            if len(frequencies) == len(unique_frequencies):
                cool_word_count += 1
                
        print(f"Case {case_num}: {cool_word_count}")
        case_num += 1

if __name__ == '__main__':
    solve()