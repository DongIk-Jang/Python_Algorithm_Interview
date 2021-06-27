class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_dict = dict()
        for s in stones:
            stone_dict[s] = stone_dict.get(s, 0) + 1
          
        answer = 0
        for j in jewels:
            if j in stone_dict:
                answer += stone_dict[j]
                
        return answer

