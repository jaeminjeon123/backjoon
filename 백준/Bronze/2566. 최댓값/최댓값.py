A = [list(map(int, input().split())) for i in range(9)]

maxA = A[0][0]
max_index = (0, 0) 

for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] > maxA:
            maxA = A[i][j]
            max_index = (i, j) 

print(maxA)
print(max_index[0] + 1, max_index[1] + 1)  
