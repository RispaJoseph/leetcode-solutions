class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        new = []
        xor_val = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j]) <= min(nums[i],nums[j]):
                    if (nums[j],nums[i]) not in new:
                        new.append((nums[i],nums[j])) 
        for i in new:
            xor_val.append(i[0] ^ i[1])        
        return (max(xor_val))
        
