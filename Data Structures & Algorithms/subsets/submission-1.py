class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        
        def backtracking(i):
            if i == n:
                res.append(sol[:])
                return
            # 不選擇，直接往下走
            backtracking(i + 1)
            # 選擇後，往下走
            sol.append(nums[i])
            backtracking(i + 1)
            sol.pop()
        backtracking(0)
        return res
        # Time Complexity - O(n * 2^n)
        # Space - (n)