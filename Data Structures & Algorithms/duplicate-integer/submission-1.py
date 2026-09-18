class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()

        # 1, not in duplicate -> add(1)
        # 2, not in duplicate -> add(2)
        # 3, not in duplicate -> add(3)
        # 3, in duplicate -> return True
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)
        return False