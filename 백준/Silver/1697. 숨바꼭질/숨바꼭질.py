import sys
from collections import deque

def bfs(start, target):
    max_pos = 100000  # 위치의 최대값을 100000으로 설정
    visited = [False] * (max_pos + 1)  # 방문 여부를 추적하기 위한 리스트
    queue = deque([(start, 0)])  # 큐 초기화, (현재 위치, 소요 시간)을 저장

    while queue:
        start, time = queue.popleft()  # 큐에서 현재 위치와 소요 시간 꺼내기

        if start == target:  # 목표 위치에 도달한 경우
            return time  # 소요 시간 반환

        # 다음 가능한 위치들 탐색
        for next_pos in (start - 1, start + 1, start * 2):
            if 0 <= next_pos <= max_pos and not visited[next_pos]:  # 다음 위치가 범위 내에 있고 방문하지 않은 경우
                visited[next_pos] = True  # 방문 표시
                queue.append((next_pos, time + 1))  # 큐에 추가 (다음 위치, 소요 시간 +
            

n,k=map(int,input().split())
result=bfs(n,k)
print(result)
