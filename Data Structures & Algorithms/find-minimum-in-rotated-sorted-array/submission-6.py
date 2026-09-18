class Solution:
    def findMin(self, nums: List[int]) -> int:
        # sorted array -> sequence
        l, r = 0, len(nums) - 1
        current_min = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                current_min = min(current_min, nums[l])
                break
            mid = (l + r) // 2
            current_min = min(current_min, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return current_min
