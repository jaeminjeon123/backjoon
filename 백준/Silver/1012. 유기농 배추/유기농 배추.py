import sys
from collections import deque

def bfs(grid, x, y, n, m):
    # 상하좌우 네 방향을 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    grid[x][y] = 0  # 방문 표시
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = 0  # 방문 표시
                queue.append((nx, ny))

t = int(input())
results = []
for _ in range(t):
    # 각 테스트 케이스의 배추밭 정보 입력
    m, n, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1
    
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                bfs(grid, i, j, n, m)
                count += 1
    
    results.append(count)

# 결과 출력
for result in results:
    print(result)
