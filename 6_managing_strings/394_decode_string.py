# string = 3 * 'a' + 2 * 'bc'
# print(string)

def decodeString(s):
    stack = []
    temp = ''
    num = 0
    answer = ''
    parent = {']' : '['}
    for i in s:
        if i not in parent:
            stack.append(i)
        else:
            if len(stack) > 0:
                if stack[-1] == parent[i]:
                    if stack[-1].isnumeric():
                        num = int(stack.pop())
                    else:
                        temp += stack.pop()
            else:
                answer += num * temp
    answer = str(stack) + answer
    return answer

s = "3[a]2[bc]"
s = "3[a2[c]]"
print(decodeString(s))
            
    

