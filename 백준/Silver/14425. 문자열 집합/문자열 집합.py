
N, M = map(int, input().split())
S = set()
for _ in range(N):
    S.add(input().strip())

count = 0
for i in range(M):
    if input().strip() in S:
        count += 1

print(count)

