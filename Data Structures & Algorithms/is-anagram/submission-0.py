class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for char_s in s:
            count[ord(char_s) - ord('a')] += 1
        for char_t in t:
            count[ord(char_t) - ord('a')] -= 1
        
        for c in count:
            if c != 0:
                return False
        return True

        