class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        for i in range(0, len(s), k):
            l = s[i:i+k]
            res.append(l + (k-len(l)) * fill)
        return res

        
