class Solution:

  def generateParenthesis(self, n: int) -> list[str]:
    res = []

    def dfs(left_count, right_count, current_str):
      if left_count == n and right_count == n:
        res.append(current_str)
        return

      if left_count < n:
        dfs(left_count + 1, right_count, current_str + "(")

      if right_count < left_count:
        dfs(left_count, right_count + 1, current_str + ")")

    dfs(0, 0, "")
    return res