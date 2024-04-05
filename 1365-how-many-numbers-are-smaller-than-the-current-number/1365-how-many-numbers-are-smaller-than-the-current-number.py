class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        small = [0] * len(nums)
        for i in range(len(nums)):
            current = nums[i]
            count = 0
            for j in range(len(nums)): 
                if current > nums[j]:
                    count += 1
            small[i] = count
            count = 0
        
        return small
        