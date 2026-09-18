class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use set to avoid duplicate element
        numSet = set(nums)
        longest = 0

        for num in nums:
            # find the start of seq.
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest