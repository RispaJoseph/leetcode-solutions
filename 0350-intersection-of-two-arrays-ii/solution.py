class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = list(set(nums1) & set(nums2))
        result = []
        for i in common:
            result.extend([i] * min(nums1.count(i), nums2.count(i)))
        return result
