class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, prev_i = stack.pop()
                ans[prev_i] = i - prev_i
            stack.append((t, i))

        return ans