class Solution:
    def toHex(self, num: int) -> str:
        if num >= 0:
            return str(hex(num)[2:])
        else:
            positive_num = (1 << 32) + num
            hexa = hex(positive_num)[2:]
            return str(hexa)

