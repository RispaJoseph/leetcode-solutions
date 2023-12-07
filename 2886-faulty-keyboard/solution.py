class Solution:
    def finalString(self, s: str) -> str:
        str = ""
        for j in s:
            if(j=="i"):
                str=str[::-1]
            else:
                str+=j
        return str
        
                

