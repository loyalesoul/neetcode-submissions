class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_set = set()
        hash_set.update(nums)
        for i in range(len(nums) + 1):
            if i not in hash_set:
                return i
        return 0
