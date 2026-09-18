class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        middle = l + (r-l) // 2

        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            return self.binary_search(middle+1, r, nums, target)
        
        return self.binary_search(l, middle-1, nums, target)
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums)-1, nums, target)