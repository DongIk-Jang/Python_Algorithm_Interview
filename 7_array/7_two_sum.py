from itertools import combinations

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = combinations(nums, 2)
        for i, j in temp:
            if i + j == target:
                a = nums.index(i)
                nums[a] = ''
                b = nums.index(j)
                return [a, b]

'''
내 풀이는 제일 비효율적인 풀이였구나..ㅎㅎ
이렇게 모든 조합을 확인해보는 방법을 브루트포스(Brute-Force)라고 한다.

아래는 간결하고 빠른 해답
'''
def twoSum2(self, nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

'''
만약 문제에서 구하라는 것이 인덱스가 아닌 그냥 두 숫자라면
투 포인터를 이용할 수 있다.
투 포인터는 우선 주어진 nums를 오름차순으로 정렬한 후
가장 앞 포인터와 가장 뒤 포인터를 더해서 target보다 크면
오른쪽 포인터를 한 칸 앞으로 이동하고
target보다 작다면 왼쪽 포인터를 한 칸 뒤로 이동해가며
target과 같아지는 때의 포인터가 가리키는 숫자를 알아내는 방식이다.
'''

