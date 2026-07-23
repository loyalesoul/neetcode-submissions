from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        counts = Counter(s)
        countt = Counter(t)
        if counts == countt:
            return True
        return False


        
