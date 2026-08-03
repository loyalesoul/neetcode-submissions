class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        low, high = 0, M * N - 1

        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // N][mid % N]

            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
