from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l_s1 = len(s1)
        right = l_s1

        c_s1 = Counter(s1)
        while right <= len(s2):
            left = right - l_s1
            if c_s1 == Counter(s2[left:right]):
                return True
            else:
                right += 1

        return False
