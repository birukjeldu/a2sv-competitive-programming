class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] = nums[left] * 2
                nums[right] = 0
            
                
            left += 1
            right = left + 1
            
            
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1
                
            
            
        
        return nums