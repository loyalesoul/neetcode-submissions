class Solution:

  def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    def dfs(i, current_path):
      res.append(current_path.copy())

      for j in range(i, len(nums)):
        if j > i and nums[j] == nums[j - 1]:
          continue

        current_path.append(nums[j])
        dfs(j + 1, current_path)
        current_path.pop()

    dfs(0, [])
    return res