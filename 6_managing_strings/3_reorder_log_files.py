class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters = []
        digits = []
        for l in logs:
            if l.split()[1].isdigit():
                digits.append(l)
            else:
                letters.append(l)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

'''
새로 알게 된 것

.isdigit() : 숫자로 이루어져 있는 지 판별해주는 함수

sort(key=a, b) : a로 정렬 후, a에 대해 동일 우선순위인 항목에 대해서 b로 정렬
'''