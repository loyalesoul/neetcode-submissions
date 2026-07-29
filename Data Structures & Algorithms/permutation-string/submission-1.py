from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        c_s1 = Counter(s1)
        window = Counter(s2[:n])

        if c_s1 == window:
            return True

        for right in range(n, m):
            left_char = s2[right - n]
            right_char = s2[right]

            window[right_char] += 1
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            if window == c_s1:
                return True

        return False
