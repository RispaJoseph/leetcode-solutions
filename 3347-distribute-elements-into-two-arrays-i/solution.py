class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []

        a1 = nums.pop(0)
        arr1.append(a1)
        a2 = nums.pop(0)
        arr2.append(a2)

        for i in range(len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1+arr2

        
