class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int(''.join(map(str,digits)))
        digits += 1
        digits = list(map(int,str(digits)))
        return digits

