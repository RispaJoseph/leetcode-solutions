class Solution:
    def reverseWords(self, s: str) -> str:
        splited_str = s.split()
        reversed_lst = splited_str[::-1]
        return ' '.join(reversed_lst)
        
