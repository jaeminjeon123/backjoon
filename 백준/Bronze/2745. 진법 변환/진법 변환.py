def base_to_decimal(number, base):
    return int(number, base)

number, base = input().split()
base = int(base)
result = base_to_decimal(number, base)
print(result)
