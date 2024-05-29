def cal(a, b):
    if a < b and b % a == 0:
        return "factor"
    elif a > b and a % b == 0:
        return "multiple"
    else:
        return "neither"

a, b = map(int, input().split())

while a != 0 and b != 0:
    print(cal(a, b))
    a, b = map(int, input().split())

