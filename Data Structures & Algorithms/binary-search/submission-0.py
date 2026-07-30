class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            i = left + (right - left) // 2
            if target == nums[i]:
                return i
            elif target > nums[i]:
                left = i + 1
            else:
                right = i
        return -1
