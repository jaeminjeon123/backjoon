from collections import deque

def bfs(n, m, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    distance = [[0] * m for _ in range(n)]
    distance[0][0] = 1

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '1':
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
                
                if nx == n-1 and ny == m-1:
                    return distance[nx][ny]
    
    return -1

# 입력
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# 결과 출력
print(bfs(n, m, grid))