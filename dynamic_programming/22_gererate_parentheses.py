def generateParenthesis(n):
    answer = []
    parentheses = {
        ')':n,
        '(':n
        }
    print(parentheses)
    while parentheses[')'] > 0:
        temp = ''
        if parentheses['('] > 0:
            temp += '('
            parentheses['('] -= 1
            print(temp)
            print(parentheses)
        else:
            temp += ')'
            parentheses[')'] -= 1
    answer.append(temp)
    return answer
        
print(generateParenthesis(3))
