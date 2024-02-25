lines = [input() for i in range(5)]
result = ""
max_length = max(len(i) for i in lines)
for i in range(max_length):
    for j in lines:
        if i < len(j):
            result =result+j[i]
print(result)
