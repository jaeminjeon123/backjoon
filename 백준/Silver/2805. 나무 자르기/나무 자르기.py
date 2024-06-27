n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)


result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    
   
    for tree in trees:
        if tree > mid:
            total += tree - mid
    
    
    if total < m:
        end = mid - 1
   
    else:
        result = mid
        start = mid + 1
        
print(result)