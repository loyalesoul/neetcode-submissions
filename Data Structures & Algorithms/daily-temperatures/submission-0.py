class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_i = stack.pop()
                ans[prev_i] = i - prev_i

            stack.append(i)
        return ans