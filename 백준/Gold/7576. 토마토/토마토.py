from collections import deque

def bfs(grid, ripe_tomatoes, n, m):
    # 상하좌우 네 방향을 정의
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 익은 토마토들의 위치를 담은 큐 초기화
    queue = deque(ripe_tomatoes)
    
    # 모든 토마토가 익는 데 걸리는 일수를 카운트하기 위한 변수
    days = -1

    while queue:
        days += 1
        # 현재 큐의 크기만큼 순회 (하루 단위로 익은 토마토 전파)
        for i in range(len(queue)):
            x, y = queue.popleft()
            # 네 방향으로 탐색
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 범위 내에 있고, 익지 않은 토마토가 있는 경우
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                    # 토마토를 익은 상태로 변경
                    grid[nx][ny] = 1
                    # 익은 토마토의 위치를 큐에 추가
                    queue.append((nx, ny))
    
    # 모든 토마토가 익었는지 확인
    for row in grid:
        if 0 in row:
            return -1  # 익지 않은 토마토가 있으면 -1 반환
    return days  # 모든 토마토가 익은 데 걸린 일수 반환

def main():
    # 입력 받기
    m, n = map(int, input().split())
    # 토마토 상자 상태 입력 받기
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    # 초기 익은 토마토들의 위치 찾기
    ripe_tomatoes = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]
   
    # BFS를 통해 결과 계산
    result = bfs(grid, ripe_tomatoes, n, m)
    # 결과 출력
    print(result)

# main 함수 호출
main()
