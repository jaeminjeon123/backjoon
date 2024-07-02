
from collections import deque

def josephus_problem(n, k):
    q = deque(range(1, n + 1))
    result = []
    
    while q:
        q.rotate(-k + 1)
        result.append(q.popleft())
    
    return result

n, k = map(int, input().split())
result = josephus_problem(n, k)
print("<" + ", ".join(map(str, result)) + ">")

