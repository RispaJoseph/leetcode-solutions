class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                a = max(str(nums[i]))
                b = max(str(nums[j]))

                if a==b:
                    s.append(nums[i] + nums[j])

        if len(s) != 0:
            return max(s)
        else:
            return -1
