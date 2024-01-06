class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        r = []
        t = ""
        for i in range(len(s)):
            if i < k:
                r.append(s[i])
        t = ' '.join(r)
        return t
        
