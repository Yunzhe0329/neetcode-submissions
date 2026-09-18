class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, path):
            if i == n:
                res.append(path)
                return
            # 不選，直接往下走
            dfs(i + 1, path)
            # 選了再往下走
            dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return res
        # Time - O(n * 2 ^ n)
        # Space - O(n ^ 2)