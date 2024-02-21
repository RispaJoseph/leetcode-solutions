class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > ans:
                ans += 1
        return ans
