from collections import deque

def bfs(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    results = set()
    
    for i in range(5):
        for j in range(5):
            queue = deque([(i, j, grid[i][j])]) 
            
            while queue:
                x, y, number = queue.popleft()
                
                if len(number) == 6:
                    results.add(number)
                    continue
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        queue.append((nx, ny, number + grid[nx][ny]))
    
    return len(results)


grid = [input().split() for _ in range(5)]


print(bfs(grid))
