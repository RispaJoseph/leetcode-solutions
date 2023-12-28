class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst = []
        nums1 = nums[:n]
        nums2 = nums[n:]

        for i in range(len(nums1)):
                lst.append(nums1[i])
                lst.append(nums2[i])
        return lst
        
