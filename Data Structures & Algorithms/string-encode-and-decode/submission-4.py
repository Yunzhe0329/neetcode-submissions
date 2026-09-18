class Solution:

    def encode(self, strs: List[str]) -> str:
        # Hello -> encode() -> 5#Hello
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0

        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            res.append(s[r + 1: r + 1 + length])
            l = r + 1 + length
        return res
            
        