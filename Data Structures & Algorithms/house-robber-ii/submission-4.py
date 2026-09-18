class Solution:
    # handle base case of house rob
    def help(self, nums: List[int]) -> int:
        if not nums:
            return False
        if len(nums) <= 1:
            return nums[0]
        n = len(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
    
    # handle cycles
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.help(nums[1:]), self.help(nums[:-1]))
        