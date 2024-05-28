def find_fraction(N):
    num = 1  # 대각선의 숫자
    while N > num:
        N -= num
        num += 1
    
    if num % 2 == 0:
        numerator = N
        denominator = num - N + 1
    else:
        numerator = num - N + 1
        denominator = N
    
    return f"{numerator}/{denominator}"

N = int(input())
print(find_fraction(N))
