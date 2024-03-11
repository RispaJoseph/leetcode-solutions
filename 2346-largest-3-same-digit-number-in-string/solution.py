class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a = ''
        for i in range(2,len(num)):
            if num[i] == num[i-1] == num[i-2]:
                a = max(a, num[i-2: i+1 ])
        return a
                


        
        
