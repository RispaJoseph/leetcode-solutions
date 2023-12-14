class Solution:
    def largestOddNumber(self, num: str) -> str:
        largest_odd = ""
        current = ""
        
        for digit in num:
            current += digit
            if int(digit) % 2 == 1:
                largest_odd = current
        
        return largest_odd


