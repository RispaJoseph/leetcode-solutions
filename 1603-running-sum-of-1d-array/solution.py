class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        a = 0 
        for i in range(len(nums)):
            a += nums[i]
            lst.append(a)
        return lst
