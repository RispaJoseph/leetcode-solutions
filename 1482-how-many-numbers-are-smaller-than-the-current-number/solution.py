class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        sort = sorted(nums)
        for i in nums:
            result.append(sort.index(i))
        return result
        
