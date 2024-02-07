class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        res = []
        for i in s:
            res.append(s.count(i))

        if len(set(res)) == 1:
            return True
        else:
            return False



        
