class Solution:
    def splitNum(self, num: int) -> int:
        num = str(num)
        num = sorted(num)

        odd = ""
        even = ""

        for i in range(len(num)):
            if i%2!=0:
                odd += num[i]
            else:
                even += num[i]

        result = int(odd) + int(even)
        return result
        
