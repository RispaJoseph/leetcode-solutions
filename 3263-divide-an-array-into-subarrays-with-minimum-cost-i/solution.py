class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = nums[0]
        nums = nums[1:]
        nums.sort()
        return (n + nums[0] + nums[1])
