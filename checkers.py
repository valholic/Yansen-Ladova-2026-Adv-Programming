import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    num_test_cases = int(input_data[idx])
    idx += 1
    MOD = 1000007
    
    for case_num in range(1, num_test_cases + 1):
        n = int(input_data[idx])
        idx += 1
        grid = []
        start_r, start_c = -1, -1
        
        for r in range(n):
            row_str = input_data[idx]
            idx += 1
            grid.append(row_str)
            if 'W' in row_str:
                start_r, start_c = r, row_str.find('W')
        
        # dp[r][c] = number of ways to reach cell (r, c)
        dp = [[0] * n for _ in range(n)]
        dp[start_r][start_c] = 1
        
        # Process rows from bottom to top
        for r in range(start_r, 0, -1):
            for c in range(n):
                if dp[r][c] == 0:
                    continue
                
                # Try moving/jumping left-up and right-up
                for dc in [-1, 1]:
                    nr, nc = r - 1, c + dc
                    
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == '.':
                            # Regular move
                            dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
                        elif grid[nr][nc] == 'B':
                            # Attempt jump
                            jr, jc = r - 2, c + (dc * 2)
                            if 0 <= jr < n and 0 <= jc < n and grid[jr][jc] == '.':
                                dp[jr][jc] = (dp[jr][jc] + dp[r][c]) % MOD
        
        # The answer is the sum of all paths reaching the top row (row 0)
        total_paths = sum(dp[0]) % MOD
        print(f"Case {case_num}: {total_paths}")

if __name__ == "__main__":
    solve()