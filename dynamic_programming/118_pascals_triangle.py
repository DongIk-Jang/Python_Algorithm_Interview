# def generate(numRows):
#     answer = [[1], [1,1]]
#     i = 1
#     while i + 1 < numRows:
#         for j in answer[i]:
#             if (j+1) <= len(answer[i]):
#             answer.append()

#     for i in range(1, numRows+1):
#         pass

def test(numRows):
    answer = [[1]]
    i = 2
    while i <= numRows:
        temp = [1]
        for num in range(i):
            if num + 1 < i - 1:
                temp.append(answer[i-2][num]+answer[i-2][num+1])
            else:
                temp.append(1)
        temp.pop()
        answer.append(temp)
        i += 1
    return answer

print(test(5))