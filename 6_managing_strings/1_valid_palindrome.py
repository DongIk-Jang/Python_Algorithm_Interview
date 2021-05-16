class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs) > 1:
            if strs.pop() != strs.pop(0):
                return False
        
        
        return True

'''
re.sub()과 정규식을 이용해서 슬라이싱을 적용해 해결 가능.

.isalnum() : 모두 alphanumeric인지 판별.(알파벳 혹은 숫자인 경우에 True 반환)
'''