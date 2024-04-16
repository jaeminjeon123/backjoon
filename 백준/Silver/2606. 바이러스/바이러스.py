from collections import deque

V = int(input())
E = int(input())

# 인접 행렬 초기화
adj = [[0] * (V + 1) for _ in range(V + 1)]

# 간선 정보 입력받기
for _ in range(E):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

# BFS 설정
queue = deque([1])  # 시작 노드 (예를 들어 1번 노드에서 시작)
visited = set()

while queue:
    cur = queue.popleft()
    visited.add(cur)

    for nxt in range(1, V + 1):
        if adj[cur][nxt] == 1 and nxt not in visited:  # 인접하고 방문하지 않았다면
            visited.add(nxt)
            queue.append(nxt)

print(len(visited) - 1)  # 시작 노드를 제외한 방문한 노드의 수
