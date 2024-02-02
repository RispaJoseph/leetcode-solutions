class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a = []
        b = []
        c = ""

        for i in s:
            a.append(i)

        for i in a:
            if (i=="1"):
                a.remove(i)
                b.append(i)
                break
        a.sort()
        a.reverse()
        a.extend(b)

        c = c.join(a)

        return c
        
