class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_range = 0

        for i in range(n):
            if i > max_range:
                return False
            max_range = max(max_range, i + nums[i])
            if max_range >= (n + 1):
                return True
        return True