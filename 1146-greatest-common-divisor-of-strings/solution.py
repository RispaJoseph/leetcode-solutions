class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        while str1 != str2:
            if len(str1) > len(str2):
                str1 = str1[len(str2):]
            else: 
                str2 = str2[len(str1):]
        return str1
