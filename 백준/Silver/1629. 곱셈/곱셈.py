def power(a, b, c):
    result = 1
    base = a % c  

    while b > 0:
        if b % 2 == 1:  
            result = (result * base) % c
        base = (base * base) % c  
        b =b//2  

    return result

a, b, c = map(int, input().split())
print(power(a, b, c))
