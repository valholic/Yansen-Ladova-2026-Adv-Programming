import sys

def main():
    for line in sys.stdin:
        a, b = map(int, line.split())
        
        if a == -1 and b == -1:
            break
            
        direct_dist = abs(a - b)
        
        wrap_dist = 100 - direct_dist
        print(min(direct_dist, wrap_dist))

if __name__ == '__main__':
    main()