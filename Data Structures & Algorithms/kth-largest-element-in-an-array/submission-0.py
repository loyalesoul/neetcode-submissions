import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        for x in nums:
            heapq.heappush(max_heap, x)

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return heapq.heappop(max_heap)
