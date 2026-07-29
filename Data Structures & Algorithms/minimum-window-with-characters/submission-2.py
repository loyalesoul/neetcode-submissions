from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        target_counts = Counter(t)
        required = len(target_counts)

        window = {}
        formed = 0

        left = 0
        min_len = float("inf")
        ans_bounds = (0, 0)

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in target_counts and window[char] == target_counts[char]:
                formed += 1

            while formed == required:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    ans_bounds = (left, right + 1)

                left_char = s[left]
                window[left_char] -= 1
                if left_char in target_counts and window[left_char] < target_counts[left_char]:
                    formed -= 1

                left += 1

        return s[ans_bounds[0] : ans_bounds[1]] if min_len != float("inf") else ""
