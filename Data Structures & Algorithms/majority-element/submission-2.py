class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        # always contained majority elements -> we can just find the most frequent element
        res = maxCount = 0
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res
        
        
        