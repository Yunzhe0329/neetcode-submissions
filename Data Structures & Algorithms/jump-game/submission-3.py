class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_range = 0 # how far it can jump

        for i in range(n):
            if i > max_range: # cannot jump to next position
                return False
            max_range = max(max_range, i + nums[i]) 
            if max_range >= (n + 1): # if max_range > (n + 1) means it can jump all the way throgh the array
                return True
        return True