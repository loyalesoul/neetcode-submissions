class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, current_combo, current_target):
            if current_target == 0:
                res.append(current_combo.copy())
                return

            if current_target < 0 or i == len(nums):
                return

            current_combo.append(nums[i])
            dfs(i, current_combo, current_target - nums[i])
            current_combo.pop()

            dfs(i + 1, current_combo, current_target)

        dfs(0, [], target)
        return res
