from itertools import combinations


def cal(cards, m):
    max_sum = 0
    for combo in combinations(cards, 3):
        current_sum = sum(combo)
        if current_sum <= m and current_sum > max_sum:
            max_sum = current_sum
    return max_sum

n, m = map(int, input().split())
cards = list(map(int, input().split()))

print(cal(cards, m))
