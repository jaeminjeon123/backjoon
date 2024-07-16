def hero(a, b, level):
    level.sort()  

   
    left, right = level[0], level[0] + b

    while left <= right:
        mid = (left + right) // 2
        count = 0

        for l in level:
            if l < mid:
                count += mid - l

        if count <= b:
            left = mid + 1  
        else:
            right = mid - 1 

    return right 


a, b = map(int, input().split())
level = [int(input()) for _ in range(a)]
print(hero(a, b, level))
