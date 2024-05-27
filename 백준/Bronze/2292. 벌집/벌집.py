def find_steps(n):
    if n == 1:
        return 1
    layer = 1
    range_end = 1
    while n > range_end:
        range_end += 6 * layer
        layer += 1
    return layer

n = int(input())
print(find_steps(n))
