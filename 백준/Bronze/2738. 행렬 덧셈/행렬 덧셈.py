N, M = map(int, input().split())


A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]
C = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]

for row in C: print(' '.join(map(str, row)))