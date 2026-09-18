class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        maximum_sub = dp[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            maximum_sub = max(maximum_sub, dp[i])
            print(dp)
        return maximum_sub
            