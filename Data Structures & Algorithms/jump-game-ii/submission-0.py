class Solution:
    def jump(self, nums: List[int]) -> int:
        max_range = 0
        bound = 0
        n = len(nums)
        result = 0
        if n == 0:
            return 0
        if n == 1:
            return 0
        for i in range(n):
            max_range = max(max_range, i + nums[i])

            if max_range >= n - 1:
                result += 1
                break
            if i == bound:
                result += 1
                bound = max_range
        return result
                        