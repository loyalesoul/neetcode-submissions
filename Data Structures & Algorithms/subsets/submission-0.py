class Solution:

  def subsets(self, nums: list[int]) -> list[list[int]]:
    res = []
    current_subset = []

    def dfs(i):
      if i == len(nums):
        res.append(current_subset.copy())
        return

      current_subset.append(nums[i])
      dfs(i + 1)

      current_subset.pop()
      dfs(i + 1)
    dfs(0)
    return res