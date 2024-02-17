class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        s = 0
        new = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i<j<k and nums[i] < nums[j] and nums[k] < nums[j]:
                         s = nums[i] + nums[j] + nums[k]
                         new.append(s)
        if new:
            return min(new)
        else:
            return -1
