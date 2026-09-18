class Solution:
    def rob(self, nums: List[int]) -> int:
        state0 = state1 = 0
        for i in range(len(nums)):
            temp = max(state1, state0 + nums[i])
            state0 = state1
            state1 = temp
        return state1
        