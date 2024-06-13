class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = [e for e in s if e.isalpha()][::-1]
        for i in range(len(s)):
            if s[i].isalpha() == False:
                ans.insert(i,s[i])
        return "".join(chr for chr in ans)
        
