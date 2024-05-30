def cal(n):
    for i in range(1, n):
        sum_of_digits = sum(map(int, str(i)))
        if i + sum_of_digits == n:
            return i
    return 0

n = int(input())
print(cal(n))
