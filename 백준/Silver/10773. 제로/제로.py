def zero_problem(k, numbers):
    stack = []
    
    for number in numbers:
        if number == 0:
            if stack:  
                stack.pop()
        else:
            stack.append(number)
    
    return sum(stack)


n = int(input())  
numbers = [int(input()) for i in range(n)]  

print(zero_problem(n, numbers))
