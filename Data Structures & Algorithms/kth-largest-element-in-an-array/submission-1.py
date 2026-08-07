import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = k - 1

        def quickselect(left: int, right: int) -> int:
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            store_idx = left
            for i in range(left, right):
                if nums[i] > pivot:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1

            nums[store_idx], nums[right] = nums[right], nums[store_idx]

            if store_idx == target_idx:
                return nums[store_idx]
            elif store_idx < target_idx:
                return quickselect(store_idx + 1, right)
            else:
                return quickselect(left, store_idx - 1)

        return quickselect(0, len(nums) - 1)
