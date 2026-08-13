class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def dfs(i, current_path):
            # Base Case: Reached the end of string 🎯
            if i == len(s):
                res.append(current_path.copy())
                return

            for j in range(i, len(s)):
                substring = s[i : j + 1]

                # Only explore if the slice is a palindrome 🔄
                if substring == substring[::-1]:
                    current_path.append(substring)  # 1. ADD
                    dfs(j + 1, current_path)  # 2. EXPLORE
                    current_path.pop()  # 3. UNDO (Backtrack)

        dfs(0, [])
        return res
