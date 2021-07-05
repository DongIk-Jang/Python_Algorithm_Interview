def countLargestGroup(n):
    group = {}
    for i in range(1, n+1):
        num = 0
        for n in str(i):
            num += int(n)
        group[num] = group.get(num, [i])
        group[num].append(i)

    sorting = list(group.items())
    sorting.sort(key=lambda x : len(x[1]), reverse=True)
    answer = 0
    for i, j in sorting:
        if len(j) == len(sorting[0][1]):
            answer += 1

    return answer

print(countLargestGroup(13))