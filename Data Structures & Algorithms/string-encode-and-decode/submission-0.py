class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # i = position

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # count the length of string
            res.append(s[j + 1 : j + 1 + length]) # j + 1 is the head of string
            i = j + 1 + length # update the pointer i
        return res

