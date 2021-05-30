from itertools import combinations

def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = set()
    nums = sorted(nums)
    comb = combinations(nums, 3)
    for i, j, k in comb:
        if i + j+ k == 0:
            result.add((i,j,k))
    result = map(list, result)
    return list(result)

"""
이렇게 시도를 했으나 이렇게 하면 time limit exceeded가 뜬다.
더 빠르게 계산할 수 있는 방법으로 투 포인터로 합을 계산하는 방법이 있다.
"""

def threeSum2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        print(left, right)
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left +1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return result

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum2(nums))