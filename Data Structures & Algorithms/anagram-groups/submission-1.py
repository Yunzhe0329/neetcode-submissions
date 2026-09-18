class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str not in hash_map:
                hash_map[sorted_str] = []
                print(hash_map)
            hash_map[sorted_str].append(s)
        return list(hash_map.values())
        # Time - O(n * klogk)
        # Space - O(n * k)