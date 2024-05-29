def cal(a, b):
    first = []
    for i in range(1, a + 1):
        if a % i == 0:
            first.append(i)

    if b - 1 < len(first):
        return first[b - 1]
    else:
        return 0
       
a, b = map(int, input().split())
print(cal(a, b))
