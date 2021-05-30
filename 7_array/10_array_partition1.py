class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        while nums:
            a = nums.pop()
            b = nums.pop()
            n = min(a, b)
            result += n
        return result

'''
이렇게 했더니 252ms가 나왔다.
하지만 이 문제는 단 한줄로 파이썬다운 방식으로 풀 수 있다.
'''

def arrayPairSum2(nums):
    return sum(sorted(nums)[::2])