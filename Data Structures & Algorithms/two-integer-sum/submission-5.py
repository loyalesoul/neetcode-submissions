class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = [0,1]
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):       
                if nums[i]+nums[j] == target:
                    r[0]=i
                    r[1]=j
                    return r
