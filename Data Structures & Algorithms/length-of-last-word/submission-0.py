class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = i = 0
        while i < len(s):
            # s[i] == ' ' -> i keep moving without change length
            if s[i] == ' ':
                while i < len(s) and s[i] == ' ':
                    i += 1
                if i == len(s):
                    return length
                # go through spaces -> initialize length to 0 to count next string
                length = 0
            else:
                length += 1
                i += 1
        return length
                
