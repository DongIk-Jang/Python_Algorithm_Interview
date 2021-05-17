class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]
    
        if len(s) <2 or s == s[::-1] :
            return s
    
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)

        return result

'''
이 문제는 최장 공통 부분 문자열과 더불어 다이나믹 프로그래밍으로 풀 수 있는
전형적인 문제이지만, 이 문제의 경우 더 직관적이고 빠른 방식으로 해결할 수 있는데,
그것이 투 포인터를 슬라이딩 윈도우처럼 이동시키는 방식이다.
'''