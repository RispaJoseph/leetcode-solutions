class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums.sort()
        nums1, nums2 = [], []
        for i in range(len(nums)):
            if i%2:
                nums2.append(nums[i])
            else: 
                nums1.append(nums[i])
        if len(nums1) == len(set(nums1)) == len(nums2) == len(set(nums2)):
            return True
        else: 
            return False

        
