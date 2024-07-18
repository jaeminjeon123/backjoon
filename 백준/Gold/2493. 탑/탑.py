def top(n, heights):
    stack = []
    results = [0] * n 
    for i in range(n):
        while stack and heights[i] >= heights[stack[-1]]:
            stack.pop()
        if stack:
            results[i] = stack[-1] + 1  
        stack.append(i)

    return results


n = int(input())
heights = list(map(int, input().split()))
results = top(n, heights)
print(' '.join(map(str, results)))
