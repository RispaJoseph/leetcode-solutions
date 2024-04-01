class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_of_str = len(s)
        i = 0

        for j in range(len(t)):
            if i < len_of_str and t[j] == s[i]:
                i += 1

        return i == len_of_str
                
