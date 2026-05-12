from collections import deque

def solve():
    while True:
        try:
            line = input().split()
            if not line: break
            start_x, start_y = map(int, line)
            if start_x == 0 and start_y == 0: break
            
            end_x, end_y = map(int, input().split())

            # wall_map[(x, y, direction)] = True if there is a wall
            # Directions: 0: North, 1: East, 2: South, 3: West
            walls = set()
            
            for _ in range(3):
                x1, y1, x2, y2 = map(int, input().split())
                if x1 == x2: # Vertical wall
                    for y in range(min(y1, y2) + 1, max(y1, y2) + 1):
                        # Wall is between column x1 and x1+1
                        walls.add((x1, y, 1)) # Wall is to the East of column x1
                        walls.add((x1 + 1, y, 3)) # Wall is to the West of column x1 + 1
                else: # Horizontal wall
                    for x in range(min(x1, x2) + 1, max(x1, x2) + 1):
                        # Wall is between row y1 and y1+1
                        walls.add((x, y1, 2)) # Wall is to the South of row y1
                        walls.add((x, y1 + 1, 0)) # Wall is to the North of row y1 + 1

            # BFS setup
            queue = deque([(start_x, start_y, "")])
            visited = set([(start_x, start_y)])
            
            # DX, DY for N, E, S, W
            moves = [(0, -1, 'N'), (1, 0, 'E'), (0, 1, 'S'), (-1, 0, 'W')]

            while queue:
                cx, cy, path = queue.popleft()
                
                if cx == end_x and cy == end_y:
                    print(path)
                    break
                
                for i, (dx, dy, direction) in enumerate(moves):
                    nx, ny = cx + dx, cy + dy
                    
                    # Check grid boundaries
                    if 1 <= nx <= 6 and 1 <= ny <= 6:
                        # Check if a wall exists in that direction
                        if (cx, cy, i) not in walls and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny, path + direction))
                            
        except EOFError:
            break

if __name__ == "__main__":
    solve()