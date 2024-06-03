def find_666_movie(n):
    count = 0
    num = 666
    
    while True:
        if '666' in str(num):
            count += 1
            if count == n:
                return num
        num += 1

# 입력 예시
n = int(input())

# 결과 출력
print(find_666_movie(n))
