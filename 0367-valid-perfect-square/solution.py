class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        num = math.sqrt(num)
        if num.is_integer():
            num = int(num)
        if type(num) == int:
            return True
        else:
            return False
        
