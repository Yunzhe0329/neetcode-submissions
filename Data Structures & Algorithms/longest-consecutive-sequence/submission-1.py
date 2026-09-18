class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in numSet: # if don't have left neighbor -> start of seq.
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
                
