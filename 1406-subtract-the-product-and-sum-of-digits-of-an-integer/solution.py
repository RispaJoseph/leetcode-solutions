class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = str(n)
        a = 1
        for i in lst:
            a = a*int(i)

        b = 0
        for i in lst:
            b = b+int(i)

        result = a - b
        return result
        
