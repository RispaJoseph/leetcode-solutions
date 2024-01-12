class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        m = 0
        while m != 1 and m != 4:
            m = sum(int(i)**2 for i in n)
            n = str(m)
        if m == 1:
            return True
        else: 
            return False
        
