from collections import deque

def bfs(N, K):
    # 최대 위치 값 설정
    max_pos = 100000
    # 시간을 저장할 배열 초기화 (최대값보다 큰 값으로 초기화)
    time = [float('inf')] * (max_pos + 1)
    # 시작 위치의 시간은 0
    time[N] = 0
    
    # 덱을 이용한 BFS 초기화
    dq = deque([N])
    
    while dq:
        current = dq.popleft()
        
        # 순간이동의 경우 시간 0으로 앞에 추가
        if 2 * current <= max_pos and time[2 * current] > time[current]:
            time[2 * current] = time[current]
            dq.appendleft(2 * current)
        
        # 앞으로 가는 경우 시간 +1로 뒤에 추가
        if current + 1 <= max_pos and time[current + 1] > time[current] + 1:
            time[current + 1] = time[current] + 1
            dq.append(current + 1)
        
        # 뒤로 가는 경우 시간 +1로 뒤에 추가
        if current - 1 >= 0 and time[current - 1] > time[current] + 1:
            time[current - 1] = time[current] + 1
            dq.append(current - 1)
    
    return time[K]

# 입력 예제
N, K = map(int, input().split())

# 결과 출력
print(bfs(N, K))
