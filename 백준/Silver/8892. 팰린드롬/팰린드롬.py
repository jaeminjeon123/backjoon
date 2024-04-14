def check(w):
    left= 0
    right = len(w) - 1

    while left < right:
        if w[left] != w[right]:
            return False

        left =left+ 1
        right =right- 1

    return True

n=int(input())
for tc in range(n):
    k = int(input())
    words = [input() for i in range(k)]

    flag = False
    count = 0

    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            word = words[i] + words[j]

            if check(word):
                count = word
                flag = True
                break

        if flag == True:
            break

    print(count)