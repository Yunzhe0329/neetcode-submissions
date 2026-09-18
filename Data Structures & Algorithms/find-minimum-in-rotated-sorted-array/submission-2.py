class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            middle = (l + r) // 2
            res = min(res, nums[middle])
            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle - 1
        return res