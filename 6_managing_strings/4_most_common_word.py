import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        
        return max(counts, key=counts.get)
    
    '''
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

    위와 같이 Counter의 most_common() 메서드를 통해 답을 구할수도 있다.

    a = ["a", "b", "a", "c", "d"]
    print(collections.Counter(a))

    >> Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1})
    '''

    
