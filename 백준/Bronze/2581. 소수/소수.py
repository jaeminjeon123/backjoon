def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())

primes = [i for i in range(M, N + 1) if prime(i)]

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
