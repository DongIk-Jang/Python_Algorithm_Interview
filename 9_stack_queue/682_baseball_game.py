def calPoints(ops):
    stack = []
    for i in ops:
        print(stack)
        if i == 'C':
            stack.pop()
        elif i == 'D':
            temp = stack[-1] * 2
            stack.append(temp)
        elif i == '+':
            plus = stack[-1] + stack[-2]
            stack.append(plus)
        else:
            stack.append(int(i))
    
    return sum(stack)

ops = ["5","2","C","D","+"]
print(calPoints(ops))