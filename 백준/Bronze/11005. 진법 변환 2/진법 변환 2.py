def decimal_to_base(n, base):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    if n == 0:
        return "0"
    
    while n > 0:
        result = chars[n % base] + result
        n //= base
    
    return result

n, base = map(int, input().split())
result = decimal_to_base(n, base)
print(result)
