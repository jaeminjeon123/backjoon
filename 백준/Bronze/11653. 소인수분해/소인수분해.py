def cal(a):
    
    factors = []

    while a % 2 == 0:
        factors.append(2)
        a = a // 2

   
    while a % 3 == 0:
        factors.append(3)
        a = a // 3

    
    spe = 5
    while spe * spe <= a:
        while a % spe == 0:
            factors.append(spe)
            a = a // spe
        spe += 2  # 다음 소수 후보로 넘어감

    # 마지막으로 남은 소수 처리
    if a > 1:
        factors.append(a)

    return factors

a = int(input())

factors = cal(a)
for i in factors:
    print(i)