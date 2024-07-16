def find_max_distance(houses, routers):
    houses.sort()
    left = 1  
    right = houses[-1] - houses[0] 

    result = 0

    while left <= right:
        mid = (left + right) // 2
        count = 1 
        last_router_position = houses[0]

        for i in range(1, len(houses)):
            if houses[i] - last_router_position >= mid:
                count += 1
                last_router_position = houses[i]
                if count == routers:
                    break

        if count >= routers:
            result = mid
            left = mid + 1  
        else:
            right = mid - 1  

    return result

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
print(find_max_distance(houses, C))