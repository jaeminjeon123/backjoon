import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def add_fractions(n1, d1, n2, d2):
    
    common_denominator = lcm(d1, d2)
    n1_adjusted = n1 * (common_denominator // d1)
    n2_adjusted = n2 * (common_denominator // d2)
     
    
    numerator = n1_adjusted + n2_adjusted
    denominator = common_denominator
    
    
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    
    return numerator, denominator

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

result_numerator, result_denominator = add_fractions(n1, d1, n2, d2)
print(result_numerator, result_denominator)