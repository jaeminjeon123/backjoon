# 회원 수 입력받기
N = int(input())

# 회원 정보 입력받기
members = []
for _ in range(N):
    age, name = input().split()
    members.append((int(age), name))
    
# 나이순으로 정렬 (나이가 같으면 입력 순서를 유지함)
members.sort(key=lambda member: member[0])

# 결과 출력
for member in members:
    print(member[0], member[1])
