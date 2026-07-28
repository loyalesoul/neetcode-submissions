class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            h_left, h_right = heights[left], heights[right]

            if h_left < h_right:
                area = (right - left) * h_left
                left += 1
            else:
                area = (right - left) * h_right
                right -= 1

            if area > max_area:
                max_area = area

        return max_area
