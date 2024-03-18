class Solution:
    def reverseVowels(self, s: str) -> str:
        result = []
        ans = ""
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i in vowels:
                result.append(i)
        for i in s:
            if i in vowels:
                ans += result.pop()
            else:
                ans += i
        return ans

        
