class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        unicode_s = sum(ord(char) for char in s)
        unicode_t = sum(ord(char) for char in t)

        return chr(unicode_t - unicode_s)

        # ord - ordinal
        # chr - character

        
