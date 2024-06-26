class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        new = []
        for i in nums:
            if i in new:
                return i
            else:
                new.append(i)
        
