from collections import Counter
def topKFrequent(nums, k):
    cnt = Counter()
    for num in nums:
        cnt[num] += 1
    print(cnt)
    most_common = cnt.most_common(k)
    answer = list()
    for i, j in most_common:
        answer.append(i)
    return answer

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))