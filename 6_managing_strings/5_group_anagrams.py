import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        anagram = {}
        for w in strs:
            k = ''.join(sorted(w))
            anagram[k] = anagram.get(k, [])
            anagram[k].append(w)
        
        for a in anagram:
            result.append(anagram[a])
        
        return result

'''
더 명료한 풀이
anagrams = collections.defaultdict(list)로 지정해주면
get을 사용하지 않고도 KeyError 없이 바로 없는 key값에 새로운 value를 추가할 수 있다.

또한 return할 때 그냥 anagrams.values()를 해주면
전체 value들이 리스트로 묶여서 리턴돼서 따로 리스트에 담아줄 필요가 없다.
'''