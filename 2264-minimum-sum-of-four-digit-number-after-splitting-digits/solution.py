class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        num = sorted(num)
        st1 = ""
        st2 = ""
        st1 += num[1]+num[3]
        st2 += num[0]+num[2]
        sum = int(st1)+int(st2)
        return sum        
