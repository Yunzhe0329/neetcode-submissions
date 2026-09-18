class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
            if hashMap.get(num, 0) > 1:
                return True 
        print(hashMap)
        return False