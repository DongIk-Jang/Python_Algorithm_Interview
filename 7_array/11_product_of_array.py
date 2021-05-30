class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result1 = []
        l = 1
        for i in range(len(nums)):
            result1.append(l)
            l = l * nums[i]
        
        result2 = []
        r = 1
        for i in range(len(nums)-1, -1, -1):
            result2.append(r)
            r = r * nums[i]
        result2 = result2[::-1]
        
        return list(map(lambda x, y : x * y, result1, result2))

'''
나눗셈을 사용할 수 없으니 현재 인덱스를 제외한 왼쪽 부분과 오른쪽부분에 대한
곱을 각각 리스트로 만들어 마지막에 합쳐줬는데 result2부분은 굳이 리스트로 만들지 않고
result1에 합쳐버릴 수 있다.

그런데 리트코드에서 runtime이나 memory에서 크게 차이가 나지는 않는 것 같다.
runtime은 똑같은 것 같고 memory는 아래 방법이 0.7MB 적게 사용됐다.
'''

def productExceptSelf2(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    out = []
    p = 1
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    
    p = 1
    for i in range(len(nums)-1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out