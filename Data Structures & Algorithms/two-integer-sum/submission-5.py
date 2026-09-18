class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build a hashmap {<nums[i]>:<position(i)>}
        n = len(nums)
        seen = {}
        
        for i in range(n):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i
        return []
        
        # case : [3, 4, 5, 6], target = 7
        # i = 0, diff = 4, not in seen, seen[3] = 0 {3 : 0, }
        # i = 1, diff = 3, in seen, return[0, 1]
        # Time - O(n)
        # Space - O(n)