class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        a = s.split()
        for i in a:
            d[i[-1]] = i[:-1]
        b = sorted(d)
        c = [d[key] for key in b]
        d = " ".join(c)
        return d
