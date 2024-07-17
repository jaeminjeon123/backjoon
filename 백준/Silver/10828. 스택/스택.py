def stack_operations(commands):
    stack = []
    results = []
    for command in commands:
        if command.startswith("push"):
            _, value = command.split()
            stack.append(int(value))
        elif command == "pop":
            if stack:
                results.append(stack.pop())
            else:
                results.append(-1)
        elif command == "size":
            results.append(len(stack))
        elif command == "empty":
            if stack:
                results.append(0)
            else:
                results.append(1)
        elif command == "top":
            if stack:
                results.append(stack[-1])
            else:
                results.append(-1)
    return results


n = int(input())
commands = [input()for _ in range(n)]
results = stack_operations(commands)
    
   
for result in results:
    print(result)