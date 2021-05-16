class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

'''
원래는 s = s[::-1]만 써도 되는데 리트코드에서
이 문제에 대해 공간 복잡도를 O(1)로 제한 해
s[:] = s[::-1]로 트릭을 써서 해결할 수 있다고 한다.

혹은 s.reverse()를 사용해도 된다.
'''