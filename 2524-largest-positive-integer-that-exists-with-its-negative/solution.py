class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        lst = []
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if -(nums[i]) in nums:
                lst.append(nums[i])
                return lst[0]
    
        return -1
                
