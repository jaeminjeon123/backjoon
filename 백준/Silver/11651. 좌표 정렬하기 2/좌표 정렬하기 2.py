def solve():
    n = int(input())
    real = []
    
    for I in range(n):
        x, y = map(int, input().split())
        real.append((x, y))
    real.sort(key=lambda i: (i[1], i[0]))
    for i in real:
        print(i[0], i[1])

solve()
