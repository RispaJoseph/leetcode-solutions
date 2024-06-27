sys.set_int_max_str_digits(10**6)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = ''.join(map(str, num))
        num = int(num)
        num = num + k
        new = [int(digit) for digit in str(num)]
        return new
        
