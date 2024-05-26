def calculate_coins(cents):
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents
    return quarters, dimes, nickels, pennies


T = int(input())
results = []

for _ in range(T):
    cents = int(input())
    results.append(calculate_coins(cents))


for result in results:
    print(result[0], result[1], result[2], result[3])
