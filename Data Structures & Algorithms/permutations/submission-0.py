class Solution:

  def permute(self, nums: list[int]) -> list[list[int]]:
    res = []

    def dfs(current_path):
      if len(current_path) == len(nums):
        res.append(current_path.copy())
        return

      for num in nums:
        if num not in current_path:
          current_path.append(num)
          dfs(current_path)
          current_path.pop()

    dfs([])
    return res