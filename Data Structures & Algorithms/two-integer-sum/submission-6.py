class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen and seen[diff] != i:
                return [i, seen[diff]]