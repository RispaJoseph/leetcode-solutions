class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        count = 0
        for i in nums:
            if i > min_num and i < max_num:
                count+=1
        return count
