class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = [nums[0]]
        for i in range(1, len(nums)):
            if arr[-1] != nums[i]:
                arr.append(nums[i])
        result = 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1] or arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                result += 1
        return result
