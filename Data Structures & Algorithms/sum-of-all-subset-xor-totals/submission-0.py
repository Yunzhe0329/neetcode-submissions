class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def DFS(index, total):
            if index == len(nums):
                return total
            return DFS(index + 1, total ^ nums[index]) + DFS(index + 1, total)
        return DFS(0, 0)