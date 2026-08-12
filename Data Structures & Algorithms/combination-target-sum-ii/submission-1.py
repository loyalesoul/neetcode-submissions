class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, current_combo, current_target):
            if current_target == 0:
                res.append(current_combo.copy())
                return

            if current_target < 0 or i == len(candidates):
                return

            current_combo.append(candidates[i])
            dfs(i + 1, current_combo, current_target - candidates[i])
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i = i + 1
            current_combo.pop()
            dfs(i + 1, current_combo, current_target)

        dfs(0, [], target)
        return res
