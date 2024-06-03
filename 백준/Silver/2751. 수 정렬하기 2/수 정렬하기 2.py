import sys

# 입력 받기
input = sys.stdin.read
data = input().split()

# 첫 번째 값은 숫자의 개수
n = int(data[0])

# 나머지 값들은 정렬할 숫자들
numbers = list(map(int, data[1:]))

# 정렬
numbers.sort()

# 출력
for number in numbers:
    print(number)
