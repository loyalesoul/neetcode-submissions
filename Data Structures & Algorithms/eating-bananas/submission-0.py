from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            total_hours = sum(math.ceil(x / mid) for x in piles)

            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
