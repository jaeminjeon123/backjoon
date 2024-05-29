def cal(numbers):
    prime_count = 0

    for i in numbers:
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count =count+ 1
        if count == 2:
            prime_count =prime_count+ 1

    return prime_count

n = int(input()) 
numbers = list(map(int, input().split())) 

print(cal(numbers))
